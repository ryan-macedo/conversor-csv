# Importação da biblioteca pandas para manipular tabelas e arquivos .csv
import pandas as pd

# Função de tratamento de dados
def tratar_dados(df):

    # Energia
    df["Energia em kWh"] = (
        df["Energia em kWh"]
        .replace(["---", "", " "], None)  # limpa inválidos
        .str.replace(",", ".", regex=False)  # corrige decimal
        .astype(float)  # converte
    )

    # Valor Total
    df["Valor Total"] = (
        df["Valor Total"]
        .replace(["---", "", " "], None)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    return df