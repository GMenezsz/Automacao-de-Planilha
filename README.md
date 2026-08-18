
# 📊 Automação de Planilhas em Python

Projeto desenvolvido para automatizar a leitura, filtragem e geração de relatórios financeiros a partir de planilhas do Excel utilizando a biblioteca  **Pandas** .

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Pandas** (manipulação e análise de dados)
* **Openpyxl** (motor para leitura e escrita de arquivos `.xlsx`)

## 📁 Estrutura do Projeto

**Plaintext**

```
📦 Automação de Planilhas
 ┣ 📜 main.py                  # Script principal que executa a automação
 ┣ 📜 utils.py                 # Funções auxiliares de processamento e filtros
 ┗ 📜 relatorio_financeiro_vendas.xlsx  # Planilha base de dados (entrada)
```

## ⚙️ Funcionalidades

O script processa o arquivo `relatorio_financeiro_vendas.xlsx` (na aba "Vendas") e gera automaticamente dois novos relatórios separados na mesma pasta:

1. **`Clientes_Pendentes.xlsx`** : Contém apenas os registros com o status de pagamento `Pendente`.
2. **`Clientes_Pagos.xlsx`** : Contém apenas os registros com o status de pagamento `Pago`.

## 🚀 Como Executar

1. Certifique-se de ter o Python e a biblioteca Pandas instalados em sua máquina:
   **Bash**

   ```
   pip install pandas openpyxl
   ```
2. Certifique-se de que o arquivo de dados `relatorio_financeiro_vendas.xlsx` está na mesma pasta do projeto.
3. Execute o script principal
