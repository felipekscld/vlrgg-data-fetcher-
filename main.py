import sys
import os
import pandas as pd

# Habilita importações do diretório 'src'
sys.path.append(os.path.abspath("src"))
from vlr_api import extrair_endpoint_vlrgg

def extrair_e_salvar(endpoint: str, arquivo: str) -> pd.DataFrame | None:
    os.makedirs("data", exist_ok=True)
    caminho = os.path.join("data", arquivo)

    df = extrair_endpoint_vlrgg(
        endpoint=endpoint,
        salvar_em=caminho,
        como_dataframe=True
    )

    if isinstance(df, pd.DataFrame) and not df.empty:
        print(f"✅ {len(df)} registros extraídos de '{endpoint}'")
        print(df.head(10))
        return df

    print(f"⚠️ Nenhum dado retornado para '{endpoint}'")
    return None

if __name__ == "__main__":
    # ⬇️ TROQUE AQUI: endpoint desejado e nome do arquivo de saída
    endpoint = "rankings?region=br"
    arquivo = "rankings_br.json"

    extrair_e_salvar(endpoint, arquivo)