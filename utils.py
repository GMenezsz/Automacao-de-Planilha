import pandas as pd


def clientes_pendentes(arquivo):
    dataframe = pd.read_excel(arquivo, sheet_name="Vendas")
    dataframe_pendentes = dataframe[dataframe["Status"] == "Pendente"]
    dataframe_pendentes.to_excel("Clientes_Pendentes.xlsx", index=False)


def clientes_pagos(arquivo):
    dataframe = pd.read_excel(arquivo, sheet_name="Vendas")
    dataframe_pagos = dataframe[dataframe["Status"] == "Pago"]
    dataframe_pagos.to_excel("Clientes_Pagos.xlsx", index=False)