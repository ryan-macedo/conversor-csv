# Criação do agente para converter arquivos .csv em pdf e docx

# Bibliotecas utilizadas:
# Streamlit: biblioteca para criar aplicações web interativas.
# Pandas: biblioteca para manipulação e análise de dados, especialmente para ler arquivos .csv.

# Importação da biblioteca
import streamlit as st

# Importação da biblioteca para arquivos zip
import zipfile
from io import BytesIO # Biblioteca para manipular arquivos em memória

# Importação da função para ler arquivos
# A função ler_arquivo_csv é responsável por ler arquivos .csv e retornar os dados em um DataFrame.
from ler_arquivos import ler_arquivo_csv

# Importação da função para analisar os dados
# A função dados_cliente é utilizada para filtrar e retornar dados relevantes para o cliente.
from filtrar_dados import dados_cliente

# Importação da função para gerar relatórios
from gerar_relatorio import gerar_relatorio


# Interface

# Configuração da página
# Define o título e o layout da página da aplicação Streamlit.
st.set_page_config(page_title="Gerador de Relatórios", layout="wide")

# Texto e títulos
# Define o título principal e um subtítulo para a aplicação.
st.title("Conversor de Arquivos")
st.subheader("Seu agente para ler e descrever sua base de dados\n")

# Criação das colunas
# Cria duas colunas na interface: uma para o chat e outra para o upload de arquivos.
col_chat, col_arquivos = st.columns([2, 1])

# Inserção de dados nas colunas

# Coluna de chat
# Cria um container para a seção de chat.
with col_chat:

    with st.container(border=True):
        st.subheader("Chat")

        st.text_area("Mensagens", value="Aqui aparecerão as mensagens", height=400)

        st.divider()

        # Caixa de input de texto
        st.chat_input()

# Coluna de upload de arquivos
# Cria um container para permitir que o usuário importe um arquivo .CSV para conversão.
with col_arquivos:
    st.subheader("Importe um arquivo .CSV para convertê-lo em .PDF e .DOCX")

    with st.container(border=True):
        arquivo = st.file_uploader("Carregue seu arquivo CSV aqui", type=["csv"])

        if arquivo:
            with col_arquivos:
                df = ler_arquivo_csv(arquivo)
                st.success("Arquivo carregado com sucesso!")

                # Aplicando a função para filtrar os dados do cliente
                st.subheader("Informações relevantes para o cliente:")
                df_clientes = dados_cliente(df)
                st.dataframe(df_clientes.columns)

                col1, col2 = st.columns(2)

                with col1:
                    st.button("📧 Enviar Relatórios por E-mail", use_container_width=True)

                with col2:
                    # Botão para baixar os relatórios em formato ZIP
                    if st.button("📥 Baixar Relatórios (ZIP)", use_container_width=True):
                        
                        # Seleciona os clientes únicos atravésda coluna "E-mail" do DataFrame
                        # .unique() evita duplicatas caso tenha e-mails repetidos
                        clientes = df["E-mail"].unique()

                        # Cria um buffer em memória para armazenar o arquivo ZIP (HD temporário na memória)
                        gravar_zip = BytesIO()

                        # Abre um arquivo ZIP em modo de escrita usando o buffer em memória
                        with zipfile.ZipFile(gravar_zip, "w") as zip_file:

                            # Para cada cliente, filtra os dados, gera um relatório e adiciona ao arquivo ZIP
                            for cliente in clientes:

                                # Filtra os dados do cliente específico para gerar um relatório personalizado
                                df_cliente = df[df["E-mail"] == cliente] 

                                # Gera o relatório em formato Word a partir dos dados filtrados para o cliente e armazena em um arquivo em memória
                                arquivo_docx = gerar_relatorio(df_cliente)

                                nome_arquivo = f"relatorio_{cliente}.docx"

                                zip_file.writestr(nome_arquivo, arquivo_docx.getvalue())

                        gravar_zip.seek(0) # Volta para o início do buffer para garantir que o arquivo ZIP seja lido corretamente
                        
                        # Cria um botão de download para o arquivo ZIP gerado, permitindo que o usuário baixe todos os relatórios de uma vez
                        st.download_button(
                            label="📦 Baixar todos relatórios (ZIP)",
                            data=gravar_zip,
                            file_name="relatorios_clientes.zip",
                            mime="application/zip"
                        )


            with col_chat:
                st.subheader("Visualização do arquivo:")
                st.write("Dados relevantes para a empresa:")
                st.dataframe(df)

        else:
            st.info(
                "Nenhum arquivo carregado. Por favor, carregue um arquivo CSV para continuar."
            )
