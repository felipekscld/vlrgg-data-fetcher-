# vlrgg-data-fetcher
Esse projeto foi uma primeira tentativa de coletar dados do site [vlr.gg](https://www.vlr.gg) para a criação de cenários possíveis de um campeonato de Valorant, por meio de uma API pública não oficial [vlrggapi](https://github.com/axsddlr/vlrggapi).

Após testes, foi identificado que não seria possível fazer o tipo de análise desejada com esse data fetcher, pela falta de dados antigos. Por isso, essa abordagem foi descontinuada.

## Funções 
- Consumo da API [vlrggapi](https://github.com/axsddlr/vlrggapi)
- Obtenção de resultados, partidas futuras, partidas ao vivo, rankings por região, stats por região e últimas notícias
- Armazenamento em JSON dos dados

## Limitações encontradas
- API só retorna jogos recentes
- Não filtra por times específicos

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
