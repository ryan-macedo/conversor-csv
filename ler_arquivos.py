import pandas as pd
import streamlit as st

def ler_arquivo_csv(caminho_arquivo):
    try:
        return pd.read_csv(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None