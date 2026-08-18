from utils import clientes_pagos, clientes_pendentes


def main():
    arquivo = "relatorio_financeiro_vendas.xlsx"
    clientes_pendentes(arquivo)
    clientes_pagos(arquivo)
    print("Relatórios gerados com sucesso!")


if __name__ == "__main__":
    main()