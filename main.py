import pandas as pd               
import numpy as np                

# Configura o Pandas para mostrar todas as colunas no ecrã sem as ocultar
pd.set_option('display.max_columns', None) 

# Configura a largura máxima de exibição da tabela no terminal para 1000 carateres
pd.set_option('display.width', 1000)        

# Define a função principal que encapsula a lógica do script
def main():
    
    # 1. Carrega os dados brutos
    df_vendas = pd.read_csv("vendas_tech.csv", encoding="utf-8")  # Lê um ficheiro CSV com dados de vendas e guarda-o num DataFrame
    
    # 2. Limpeza e Transformação (tudo direto no df_vendas)
    # Remove a coluna desnecessária
    df_vendas = df_vendas.drop(columns=["Data_Base"])            # Elimina a coluna "Data_Base" do DataFrame por não ser necessária
    
    # Preenche os vazios da coluna Loja
    df_vendas["Loja"] = df_vendas["Loja"].fillna("Loja online")  # Substitui os valores em falta (NaN) na coluna "Loja" por "Loja online"
    
    # Padroniza o texto das lojas (tira espaços extras e deixa a primeira letra maiúscula)
    df_vendas["Loja"] = df_vendas["Loja"].str.strip().str.title() # Remove espaços indesejados nas pontas e formata a primeira letra de cada palavra em maiúscula
    
    # Converte a data para o formato datetime real
    df_vendas["Data"] = pd.to_datetime(df_vendas["Data"], format="%Y-%m-%d") # Converte o texto da data para o formato de data real do Pandas

    # Remover duplicatas
    df_vendas = df_vendas.drop_duplicates(subset=["ID_Pedido"])  # Remove linhas repetidas com base na coluna de identificação do pedido

    # Cria a coluna de faturamento multiplicando quantidade pelo preço unitário
    df_vendas["Faturamento"] = df_vendas["Qtd"] * df_vendas["Preco_Unitario"] 

    # Cria uma coluna condicional: se for "Loja Online", assume esse valor; caso contrário, define como "Presencial"
    df_vendas["Forma_de_Venda"] = np.where(df_vendas["Loja"]=="Loja Online", "Loja Online", "Presencial")

    # Dicionário de equivalências (de-para) para associar cada loja à respetiva região geográfica
    dic_regioes = {
        'São Paulo': "Sudeste", 
        'Belo Horizonte': "Sudeste", 
        'Loja Online': "Online", 
        'Rio De Janeiro': "Sudeste", 
        'Salvador': "Nordeste", 
        'Recife': "Nordeste", 
        'Curitiba': "Sul", 
        'Porto Alegre': "Sul"
    }
    
    # Aplica o dicionário na coluna "Loja" para preencher automaticamente a nova coluna "Região"
    df_vendas["Região"] = df_vendas["Loja"].map(dic_regioes)

    #------------------------------------------------------------------------------------
    #------------ Criando arquivo de vendas das lojas de Belo Horizonte. ----------------
    #------------------------------------------------------------------------------------

    # Filtra o DataFrame principal para criar um novo contendo apenas os registos da loja "Belo Horizonte"
    df_vendas_bh = df_vendas[df_vendas["Loja"]=="Belo Horizonte"]

    # Cria uma cópia independente do DataFrame de BH para formatar os dados apenas para visualização, mantendo o original intacto
    df_bh_formatado = df_vendas_bh.copy()

    # Formata a coluna de preço unitário como texto com o símbolo de Real (R$) para o terminal
    df_bh_formatado["Preco_Unitario"] = df_bh_formatado["Preco_Unitario"].map("R${:,.2f}".format)

    # Formata a coluna de faturamento como texto com o símbolo de Real (R$) para o terminal
    df_bh_formatado["Faturamento"] = df_bh_formatado["Faturamento"].map("R${:,.2f}".format)

    # Exibe a tabela formatada com R$ no terminal
    print(df_bh_formatado)

    # Exporta o DataFrame original (com números puros e sem formatação de texto) para o Excel
    df_vendas_bh.to_excel("Vendas_bh.xlsx", index=False)

    #------------------------------------------------------------------------------------
    #----------------------- Criando arquivo de faturamento das lojas. ------------------
    #------------------------------------------------------------------------------------

    # Agrupa as vendas por loja e soma o faturamento total de cada uma
    analise_lojas = df_vendas[["Loja", "Faturamento"]].groupby("Loja").sum()

    # Ordena o resultado do maior faturamento para o menor
    analise_lojas = analise_lojas.sort_values(by="Faturamento", ascending=False)

    # Reseta o índice para transformar a coluna "Loja" (que virou índice) de volta em uma coluna normal da tabela
    analise_lojas = analise_lojas.reset_index()

    # Cria uma cópia do ranking de lojas para formatar os valores sem afetar os dados numéricos que vão para o Excel
    df_formatado_lojas = analise_lojas.copy()

    # Formata a coluna de faturamento do ranking como moeda Real (R$) exclusivamente para o terminal
    df_formatado_lojas["Faturamento"] = df_formatado_lojas["Faturamento"].map("R${:,.2f}".format)

    # Exibe o ranking formatado no terminal
    print(df_formatado_lojas)

    # Exporta o DataFrame de análise original (com números puros) para o Excel
    analise_lojas.to_excel("Faturamento_lojas.xlsx", index=False)

    # Conta e exibe a quantidade de valores em falta (nulos) restantes em cada coluna do DataFrame principal
    print(df_vendas.isna().sum())

if __name__ == "__main__":
    main()                      # Garante que a função principal é executada ao correr o script