from ler_arquivos import ler_arquivo_csv
from filtrar_dados import dados_cliente
from gerar_relatorio import gerar_relatorio

# 1. Ler o CSV
df = ler_arquivo_csv("dados/Histórico de cargas - 01_12_2025 a 31_12_2025.csv")

# 2. Verificar se carregou
print(df.head())

# 3. Aplicar filtro
df_filtrado = dados_cliente(df)
arquivo = gerar_relatorio(df_filtrado)
# 4. Ver resultado
print(df_filtrado.head())
print(df_filtrado.columns)

with open("teste.docx", "wb") as f:
    f.write(arquivo.getvalue())