# Network Fundamentals Lab

Laboratório introdutório de redes para consolidar conceitos de TCP/IP, sub-redes, DNS, HTTP e ferramentas Linux. O conteúdo combina notas reproduzíveis com uma pequena automação em Python.

## Conteúdo

```text
.
├── subnet_report.py
├── tests/
│   └── test_subnet_report.py
└── labs/
    ├── 01-tcp-ip.md
    ├── 02-dns-http.md
    └── 03-linux-network-tools.md
```

## Ferramenta de sub-redes

O script aceita IPv4 ou IPv6, normaliza bits de host e mostra propriedades da rede.

```bash
python3 subnet_report.py 192.168.10.42/24
python3 subnet_report.py 2001:db8::12/64 --json
```

Ele usa apenas a biblioteca padrão do Python e não envia tráfego para a rede.

## Testes

Requisito: Python 3.10 ou superior.

```bash
python3 -m unittest discover -s tests -v
```

## Limitações honestas

- a ferramenta calcula propriedades; não descobre dispositivos;
- não executa varredura de portas, captura de pacotes nem testes ofensivos;
- os laboratórios são introdutórios e precisam ser complementados com prática autorizada;
- resultados de comandos variam entre macOS e distribuições Linux.

## Uso ético

Execute os exercícios apenas em equipamentos próprios, ambientes de laboratório ou sistemas com autorização explícita. Não publique endereços, nomes de host ou capturas que identifiquem terceiros.

## Próximos passos

- documentar ARP e tabela de vizinhos;
- comparar TCP e UDP com uma captura feita apenas em laboratório;
- acrescentar exercícios de firewall local;
- criar uma matriz de troubleshooting por camada.
