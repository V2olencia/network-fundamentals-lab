# Laboratório 1 — TCP/IP e sub-redes

## Objetivo

Relacionar endereço IP, máscara, gateway e rota sem depender de memorização isolada.

## Mapa mental

- enlace: entrega dentro da rede local;
- IP: endereçamento e roteamento entre redes;
- TCP/UDP: transporte entre processos;
- aplicação: protocolos como DNS, HTTP e SSH.

## Exercício seguro

Execute apenas no seu computador:

```bash
ipconfig getifaddr en0              # macOS: IPv4 da interface Wi-Fi
route -n get default                # macOS: rota padrão
python3 subnet_report.py 192.168.10.42/24
```

No Linux, comandos equivalentes são `ip address` e `ip route`.

## Registro de evidência

Anote sem publicar seu IP público nem dados de terceiros:

1. rede normalizada;
2. prefixo e máscara;
3. primeiro e último host;
4. endereço de broadcast;
5. função do gateway padrão.

## Revisão curta

Explique com suas palavras por que `192.168.10.42/24` pertence à rede `192.168.10.0/24` e por que o broadcast não deve ser atribuído a um host.
