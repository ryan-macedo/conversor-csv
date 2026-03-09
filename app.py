"""
Aplicação Streamlit para leitura de CSV e geração de relatórios (.docx ou .pdf).
Inclui interface de chat fictícia e permite baixar relatórios individualizados em um ZIP.
"""

# importações de bibliotecas externas necessárias
import streamlit as st
import zipfile  # trabalhar com arquivos ZIP em memória
from io import BytesIO  # buffer de bytes usado para montar o ZIP

# funções utilitárias importadas de outros módulos do projeto
from ler_arquivos import ler_arquivo_csv
from filtrar_dados import dados_cliente
from gerar_relatorio import gerar_relatorio

# Configura a página Streamlit (título e layout)
st.set_page_config(page_title="Gerador de Relatórios", layout="wide")

# Cabeçalho principal da aplicação
st.title("Conversor de Arquivos")
st.subheader("Seu agente para ler e descrever sua base de dados\n")

# Organiza a interface em duas colunas com proporção 2:1
# a coluna esquerda será usada para o chat e a direita para controle de arquivos
col_chat, col_arquivos = st.columns([2, 1])

# --- Seção de chat ---
with col_chat:
    with st.container(border=True):
        st.subheader("Chat")
        st.text_area("Mensagens", value="Aqui aparecerão as mensagens", height=400)
        st.divider()
        # campo de entrada para o usuário enviar mensagens
        st.chat_input()

# --- Seção de upload de arquivos ---
with col_arquivos:
    st.subheader("Importe um arquivo .CSV para convertê-lo em .PDF e .DOCX")
    with st.container(border=True):
        arquivo = st.file_uploader("Carregue seu arquivo CSV aqui", type=["csv"])

        # processa o arquivo quando um usuário o carrega
        if arquivo:
            df = ler_arquivo_csv(arquivo)

            if df is None:
                st.error("Não foi possível ler o arquivo. Verifique o formato.")

            else:
                st.success("Arquivo carregado com sucesso!")

                # mostra sub-dataframe de interesse do cliente
                st.subheader("Informações relevantes para o cliente:")
                df_clientes = dados_cliente(df)
                st.dataframe(df_clientes)

                # painel com botões de ação
                col1, col2 = st.columns(2)

                with col1:
                    st.button("📧 Enviar Relatórios por E-mail", use_container_width=True)

                with col2:
                    # clicar neste botão inicia a criação de um arquivo ZIP
                    # contendo um relatório por cliente
                    if st.button("📥 Fazer download dos relatórios", use_container_width=True):
                        clientes = df["E-mail"].unique()
                        zip_buffer = BytesIO()
                        
                        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                            for cliente in clientes:
                                # filtra os dados apenas daquele cliente
                                df_cliente = df[df["E-mail"] == cliente]
                                arquivo_docx = gerar_relatorio(df_cliente)
                                nome_arquivo = f"relatorio_{cliente}.docx"

                                # arquivo_docx é um BytesIO retornado pela função
                                zip_file.writestr(nome_arquivo, arquivo_docx.getvalue())

                        zip_buffer.seek(0)

                        # disponibiliza o ZIP para download pelo usuário
                        botao_download = st.download_button(
                            label="📦 Baixar todos relatórios (ZIP)",
                            data=zip_buffer,
                            file_name="relatorios_clientes.zip",
                            mime="application/zip"
                        )

            # exibe visualização completa dos dados na coluna de chat
            with col_chat:
                st.subheader("Visualização do arquivo:")
                st.write("Dados relevantes para a empresa:")
                st.dataframe(df)
        else:
            # orientação ao usuário antes de qualquer upload
            st.info(
                "Nenhum arquivo carregado. Por favor, carregue um arquivo CSV para continuar."
            )
