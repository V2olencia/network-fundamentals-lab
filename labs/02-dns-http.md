# Laboratório 2 — DNS e HTTP

## Objetivo

Observar duas etapas de acesso a um site: resolução de nome e comunicação HTTP.

## Exercício seguro

Use o domínio reservado `example.com`:

```bash
dig example.com
curl -I https://example.com
```

Se `dig` não estiver disponível, use `nslookup example.com`.

## O que observar

- nome consultado e tipo de registro (`A` ou `AAAA`);
- servidor DNS que respondeu;
- código de status HTTP;
- cabeçalhos como `content-type` e `cache-control`;
- diferença entre DNS, endereço IP e URL.

## Perguntas

1. DNS garante que o conteúdo recebido é legítimo?
2. O que o HTTPS protege durante o transporte?
3. Um código HTTP `200` prova que a aplicação é segura?

Resposta esperada em alto nível: cada camada resolve um problema diferente; nenhuma delas, isoladamente, prova segurança completa.
