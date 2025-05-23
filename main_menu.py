import sys
import os
import pandas as pd

# Garante que o módulo src/vlr_api.py possa ser importado
sys.path.append(os.path.abspath("src"))
from vlr_api import extrair_endpoint_vlrgg

def escolher_regiao():
    regioes = {
        "1": "na", "2": "eu", "3": "latam", "4": "br", "5": "asia",
        "6": "kr", "7": "oce", "8": "mena", "9": "jp", "10": "tr", "11": "world"
    }
    print("\nRegiões disponíveis:")
    for k, v in regioes.items():
        print(f"{k} - {v.upper()}")
    return regioes.get(input("Escolha a região: "), "world")

def escolher_timespan():
    spans = {"1": "30", "2": "60", "3": "all"}
    print("\nPeríodo (em dias):")
    print("1 - Últimos 30 dias\n2 - Últimos 60 dias\n3 - Todos os tempos")
    return spans.get(input("Escolha o período: "), "30")

def extrair_e_salvar(endpoint, filename):
    os.makedirs("data", exist_ok=True)
    df = extrair_endpoint_vlrgg(endpoint, salvar_em=f"data/{filename}", como_dataframe=True)
    if isinstance(df, pd.DataFrame) and not df.empty:
        print(f"\n✅ {len(df)} registros salvos em 'data/{filename}'")
        print(df.head(10))
    else:
        print(f"\n⚠️ Nenhum dado retornado ou erro na requisição.")

def menu():
    def resultados(): extrair_e_salvar("matches/results", "matches_results.json")
    def futuras(): extrair_e_salvar("matches/upcoming", "matches_upcoming.json")
    def ao_vivo(): extrair_e_salvar("matches/live", "matches_live.json")
    def rankings():
        r = escolher_regiao()
        extrair_e_salvar(f"rankings/{r}", f"rankings_{r}.json")
    def estatisticas():
        r = escolher_regiao()
        t = escolher_timespan()
        extrair_e_salvar(f"stats/{r}/{t}", f"stats_{r}_{t}.json")
    def noticias(): extrair_e_salvar("news", "news.json")
    def health(): extrair_e_salvar("health", "health.json")

    opcoes = {
        "1": resultados,
        "2": futuras,
        "3": ao_vivo,
        "4": rankings,
        "5": estatisticas,
        "6": noticias,
        "7": health
    }

    print("== MENU VLRGGAPI ==")
    opcoes_txt = {
        "1": "Resultados de partidas",
        "2": "Partidas futuras",
        "3": "Partidas ao vivo",
        "4": "Rankings por região",
        "5": "Estatísticas por região e período",
        "6": "Últimas notícias",
        "7": "Verificar status da API"
    }

    for k, v in opcoes_txt.items():
        print(f"{k} - {v}")

    escolha = input("Escolha uma opção: ")
    acao = opcoes.get(escolha)
    if acao:
        acao()
    else:
        print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()