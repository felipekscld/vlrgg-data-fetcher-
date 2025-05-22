# vlrgg-data-fetcher
Esse projeto foi uma primeira tentativa de coletar dados do site [vlr.gg](https://www.vlr.gg) para a criação de cenários possíveis de um campeonato de Valorant, por meio de uma API pública não oficial [vlrggapi](https://github.com/axsddlr/vlrggapi).

Após testes, foi identificado que não seria possível fazer o tipo de análise desejada com esse data fetcher, pela falta de especificidade para a simulação. Por isso, essa abordagem foi descontinuada.

## Funções 
- Consumo da API [vlrggapi](https://github.com/axsddlr/vlrggapi)
- Obtenção de resultados de partidas, partidas futuras, partidas ao vivo, rankings por região, stats por região e últimas notícias
- Armazenamento em JSON dos dados

## Como usar
Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o menu principal com:
```
python main_menu.py
```

Você verá o seguinte menu no terminal:
```
== MENU VLRGGAPI ==
1 - Resultados de partidas
2 - Partidas futuras
3 - Partidas ao vivo
4 - Rankings por região
5 - Estatísticas por região e período
6 - Últimas notícias
7 - Verificar status da API
```
> Após a seleção, será salvo um arquivo .json na pasta `data/`

## 📁 Estrutura do projeto
- `data/` - pasta onde os arquivos .json são salvos
- `src/vlr_api.py` – função de extração da API
- `main_menu.py` – menu interativo para acessar a API
- `requirements.txt` – dependências do projeto
- `README.md` – descrição do projeto

## Licença
[Licença MIT](LICENSE)
