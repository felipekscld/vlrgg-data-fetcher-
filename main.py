import sys
import os
import pandas as pd

# Adiciona a pasta 'src' ao caminho de importação
sys.path.append(os.path.abspath("src"))

from vlr_api import extrair_endpoint_vlrgg

# Define o endpoint e o caminho de saída
endpoint = "match?q=results"
output_path = "data/matches_results.json"

# Extrai os dados da API
resultado = extrair_endpoint_vlrgg(
    endpoint=endpoint,
    salvar_em=output_path,
    como_dataframe=True
)

# Verifica se o retorno é um DataFrame antes de usá-lo
if isinstance(resultado, pd.DataFrame) and not resultado.empty:
    print(f"✅ {len(resultado)} partidas coletadas com sucesso.\n")
    print(resultado.head())
else:
    print("⚠️ Nenhum dado retornado ou erro na requisição.")