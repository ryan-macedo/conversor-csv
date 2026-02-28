# Importa a biblioteca necessária para criar um documento do Word
from docx import Document

# Função para gerar um relatório em formato Word a partir dos dados filtrados para o cliente.
def gerar_relatorio(df_cliente):

    # Cria o documento Word
    document = Document()

    # Adiciona um título ao documento (level 1 é o título principal)
    document.add_heading('Histórico de Cargas - Cliente', level=1)

    # Descobrir o número de colunas para criar a tabela
    num_colunas = len(df_cliente.columns)

    # Criação de tabela no documento
    tabela = document.add_table(rows=1, cols=num_colunas)

    # Seleciona as células da primeira linha da tabela para adicionar os cabeçalhos
    celulas_cabecalho = tabela.rows[0].cells

    # Adiciona os cabeçalhos da tabela com índices e nomes das colunas
    for i, nome_coluna in enumerate(df_cliente.columns):
         celulas_cabecalho[i].text = nome_coluna

    # Adiciona os dados do DataFrame à tabela
    for indice, linha in df_cliente.iterrows():
         tabela_linha = tabela.add_row().cells  # Adiciona uma nova linha à tabela e obtém as células dessa linha

        # Preenche as células da linha com os valores correspondentes do DataFrame
         for i, valor in enumerate(linha):
             tabela_linha[i].text = str(valor)  # Converte o valor para string e adiciona à célula

    # Salva o documento Word com um nome específico
    document.save('relatorio_cliente.docx')