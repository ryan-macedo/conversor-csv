"""
Módulo de leitura de arquivos CSV com caching do Streamlit.
"""

import pandas as pd
import streamlit as st

@st.cache_data
def ler_arquivo_csv(caminho_arquivo):
    """Tenta carregar um CSV e retorna um DataFrame ou None.

    O decorator @st.cache_data impede que a mesma operação seja repetida
    durante a mesma sessão, acelerando leituras posteriores.
    """
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except Exception as e:
        # usa a própria interface do Streamlit para mostrar o erro ao usuário
        st.error(f"Erro ao ler o arquivo: {e}")
        return None