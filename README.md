# vlrgg-data-fetcher
Esse projeto foi uma primeira tentativa de coletar dados do site [vlr.gg](https://www.vlr.gg) para a criação de cenários possíveis de um campeonato de Valorant, por meio de uma API pública não oficial [vlrggapi](https://github.com/axsddlr/vlrggapi).

Após testes, foi identificado que não seria possível fazer o tipo de análise desejada com esse data fetcher, pela falta de especificidade para a simulação. Por isso, essa abordagem foi descontinuada.

## Funções 
- Consumo da API [vlrggapi](https://github.com/axsddlr/vlrggapi)
- Obtenção de resultados de partidas, partidas futuras, partidas ao vivo, rankings por região, stats por região e últimas notícias
- Armazenamento em JSON dos dados

## Endpoints disponíveis 
Você pode alterar o valor da variável `endpoint` no script `main.py` para coletar diferentes tipos de dados da API do vlr.gg:


| Descrição                 | Endpoint                                   | Nome sugerido do arquivo          |
|---------------------------|-------------------------------------------|-----------------------------------|
| Resultados                | `match?q=results`                         | `matches_results.json`            |
| Partidas futuras          | `match?q=upcoming`                        | `matches_upcoming.json`           |
| Partidas ao vivo          | `match?q=live_score`                      | `matches_live.json`               |
| Ranking      | `rankings?region=br`                      | `rankings_br.json`                |
| Stats  | `stats?region=br&timespan=all`           | `stats_br_all.json`               |
| Últimas notícias          | `news`                                    | `noticias.json`                   |
| Verificação da API        | `health`                                  | opcional

- O nome do arquivo que você escolher vai ser criado na pasta `data`
> ℹ️ **Para o endpoint** `rankings`, você pode alterar o valor de `region` para:  
> `br`, `na`, `latam`, `eu`, `asia`, `kr`, `oce`, `mena`, `jp`, `tr` ou `world`.

> ℹ️ **Para o endpoint** `stats`, é possível alterar tanto a `region` quanto o `timespan` (em dias como `30`, `90`, `all`, etc.).


## Como executar
Instale as dependências:

```bash
pip install -r requirements.txt
```

E execute o script principal:
```
python main.py
```

## 📁 Estrutura do projeto
- `data/matches_results.json` – partidas coletadas
- `src/vlr_api.py` – funções de acesso à API
- `main.py` – script principal de teste
- `requirements.txt` – dependências do projeto
- `README.md` – descrição do projeto

## Licença
[Licença MIT](LICENSE)
