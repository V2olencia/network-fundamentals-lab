#!/usr/bin/env python3
"""Create a deterministic report for an IPv4 or IPv6 network."""

from __future__ import annotations

import argparse
import ipaddress
import json
from typing import Any


def network_scope(network: ipaddress.IPv4Network | ipaddress.IPv6Network) -> str:
    if network.is_loopback:
        return "loopback"
    if network.is_link_local:
        return "link-local"
    if network.is_multicast:
        return "multicast"
    if network.is_private:
        return "privada"
    if network.is_global:
        return "global"
    if network.is_reserved:
        return "reservada"
    return "especial"


def build_report(cidr: str) -> dict[str, Any]:
    """Return network properties; host bits in the input are normalized."""
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as error:
        raise ValueError(f"CIDR invalido: {cidr}") from error

    report: dict[str, Any] = {
        "input": cidr,
        "version": network.version,
        "network": str(network),
        "network_address": str(network.network_address),
        "prefix_length": network.prefixlen,
        "netmask": str(network.netmask),
        "address_count": network.num_addresses,
        "scope": network_scope(network),
    }

    if isinstance(network, ipaddress.IPv4Network):
        report["broadcast_address"] = str(network.broadcast_address)
        if network.num_addresses > 2:
            report["usable_host_count"] = network.num_addresses - 2
            report["first_usable_host"] = str(network.network_address + 1)
            report["last_usable_host"] = str(network.broadcast_address - 1)
        else:
            report["usable_host_count"] = network.num_addresses
            report["first_usable_host"] = str(network.network_address)
            report["last_usable_host"] = str(network.broadcast_address)
    else:
        report["first_address"] = str(network.network_address)
        report["last_address"] = str(network.broadcast_address)

    return report


def render_text(report: dict[str, Any]) -> str:
    labels = {
        "input": "Entrada",
        "version": "Versao IP",
        "network": "Rede normalizada",
        "network_address": "Endereco de rede",
        "prefix_length": "Prefixo",
        "netmask": "Mascara",
        "address_count": "Total de enderecos",
        "usable_host_count": "Hosts utilizaveis",
        "first_usable_host": "Primeiro host",
        "last_usable_host": "Ultimo host",
        "broadcast_address": "Broadcast",
        "first_address": "Primeiro endereco",
        "last_address": "Ultimo endereco",
        "scope": "Escopo",
    }
    order = [
        "input",
        "version",
        "network",
        "network_address",
        "prefix_length",
        "netmask",
        "address_count",
        "usable_host_count",
        "first_usable_host",
        "last_usable_host",
        "broadcast_address",
        "first_address",
        "last_address",
        "scope",
    ]
    return "\n".join(
        f"{labels[key]}: {report[key]}" for key in order if key in report
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mostra propriedades de uma rede IPv4 ou IPv6."
    )
    parser.add_argument("cidr", help="rede ou host com prefixo, por exemplo 192.168.10.42/24")
    parser.add_argument("--json", action="store_true", help="gera saida JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        report = build_report(args.cidr)
    except ValueError as error:
        print(f"Erro: {error}")
        return 2

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
