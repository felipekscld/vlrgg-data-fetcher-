import requests
import pandas as pd
import json
from typing import Union, Optional
from functools import lru_cache
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session with retry strategy
def create_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,  # number of retries
        backoff_factor=1,  # wait 1, 2, 4 seconds between retries
        status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry on
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Global session object
_session = create_session()

@lru_cache(maxsize=128)
def extrair_endpoint_vlrgg(
    endpoint: str,
    salvar_em: Optional[str] = None,
    como_dataframe: bool = False,
    timeout: int = 10
) -> Union[dict, pd.DataFrame, None]:
    """
    Extrai dados da API vlrggapi com cache e retry.
    
    Parâmetros:
    - endpoint: str → ex: "matches/results"
    - salvar_em: str ou None → caminho para salvar o JSON localmente
    - como_dataframe: bool → se True, retorna um DataFrame
    - timeout: int → tempo limite em segundos para a requisição

    Retorna:
    - dict com os dados brutos da API
    - ou DataFrame se como_dataframe=True
    - ou None em caso de erro
    """
    base_url = "https://vlrggapi.vercel.app"
    url = f"{base_url}/{endpoint}"

    try:
        print(f"Tentando acessar: {url}")  
        response = _session.get(url, timeout=timeout)
        response.raise_for_status()
        dados = response.json()

        if isinstance(salvar_em, str):
            with open(salvar_em, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)

        if como_dataframe:
            return _convert_to_dataframe(dados)

        return dados

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        print(f"URL tentada: {url}")  
        return None

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
        return None

def _convert_to_dataframe(dados: Union[dict, list]) -> pd.DataFrame:
    """Helper function to convert API response to DataFrame efficiently."""
    if isinstance(dados, list):
        return pd.DataFrame(dados)
    
    if isinstance(dados, dict):
        # If any value is a list, use it as the data
        for value in dados.values():
            if isinstance(value, list):
                return pd.DataFrame(value)
        # If no lists found, convert the dict itself
        return pd.DataFrame([dados])
    
    raise ValueError("Formato inesperado para conversão em DataFrame")

def clear_cache():
    extrair_endpoint_vlrgg.cache_clear()

# Demonstração: só roda se executar diretamente este arquivo
if __name__ == "__main__":
    data = extrair_endpoint_vlrgg("match?q=results")          # endpoint correto
    data = extrair_endpoint_vlrgg("match?q=results", timeout=15)
    clear_cache()