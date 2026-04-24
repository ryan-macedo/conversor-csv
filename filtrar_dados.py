# Filtrar os dados do cliente e da empresa para gerar um relatório personalizado.

# Dados importantes para o cliente:
# E-mail: endereço de e-mail do cliente.
# Estação: identificação da estação de energia.
# Energia em kWh: quantidade de energia consumida.
# Valor Total: custo total do consumo de energia.
# Início (Horário Local): horário de início do consumo.
# Fim (Horário Local): horário de término do consumo.
# Duração: tempo total de consumo.
# Forma de Pagamento: método utilizado para pagamento.
# Benefício do Cupom: desconto aplicado, se houver.
# SoC inicial: estado de carga inicial da bateria.
# SoC final: estado de carga final da bateria.

# Cliente
# A função dados_cliente recebe um DataFrame e retorna apenas as colunas relevantes para o cliente.
def dados_cliente(df):

    # Colunas relevantes para o cliente
    colunas_cliente = [
        'E-mail',
        'Estação', 
        'Energia em kWh', 
        'Valor Total',
        'Início (Horário Local)', 
        'Fim (Horário Local)', 
        'Duração',
        'Forma de Pagamento', 
        'Benefício do Cupom', 
        'SoC inicial',
        'SoC final'
    ]

    # Filtrar o DataFrame para obter apenas as colunas relevantes para o cliente
    df_cliente = df[colunas_cliente]  # Cria um novo DataFrame com as colunas filtradas.

    # Retornar o DataFrame filtrado para o cliente
    return df_cliente