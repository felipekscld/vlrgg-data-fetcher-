import requests
import pandas as pd
import json
from typing import Union, Optional

def extrair_endpoint_vlrgg(
    endpoint: str,
    salvar_em: Optional[str] = None,
    como_dataframe: bool = False
) -> Union[dict, pd.DataFrame, None]:
    """
    Extrai dados da API vlrggapi.
    
    Parâmetros:
    - endpoint: str → ex: "matches/results"
    - salvar_em: str ou None → caminho para salvar o JSON localmente
    - como_dataframe: bool → se True, retorna um DataFrame

    Retorna:
    - dict com os dados brutos da API
    - ou DataFrame se como_dataframe=True
    - ou None em caso de erro
    """
    base_url = "https://vlrggapi.vercel.app"
    url = f"{base_url}/{endpoint}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if isinstance(salvar_em, str):
            with open(salvar_em, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)

        if como_dataframe:
            if isinstance(dados, list):
                return pd.DataFrame(dados)
            elif isinstance(dados, dict):
                for key in dados:
                    if isinstance(dados[key], list):
                        return pd.DataFrame(dados[key])
                return pd.DataFrame([dados])
            else:
                raise ValueError("Formato inesperado para conversão em DataFrame")

        return dados

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
        return None