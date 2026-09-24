# Laboratório 3 — Ferramentas de rede no Linux

## Objetivo

Construir uma sequência de diagnóstico que comece pelo estado local antes de culpar a rede externa.

## Roteiro

```bash
ip address
ip route
ss -tulpen
ping -c 4 127.0.0.1
dig example.com
curl -I https://example.com
```

## Ordem de raciocínio

1. a interface tem endereço?
2. existe rota padrão?
3. quais serviços locais estão escutando?
4. a pilha TCP/IP local responde?
5. a resolução DNS funciona?
6. a aplicação remota responde por HTTPS?

## Limite ético

Não faça varreduras, captura de tráfego ou testes em redes e sistemas sem autorização explícita. Registre apenas dados do seu laboratório e remova identificadores antes de publicar evidências.
