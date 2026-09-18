
# 📊 Automação e Análise de Dados de Vendas com Python

Este projeto consiste num script em Python desenvolvido com a biblioteca **Pandas** para automatizar o processo de limpeza, transformação, cruzamento e resumo de dados de vendas, gerando relatórios gerenciais prontos para exportação em formato Excel.

---

## 🚀 Funcionalidades do Script

* **Limpeza de Dados:** Remoção de colunas desnecessárias, tratamento de valores em falta (`fillna`) e eliminação de registos duplicados com base no ID do pedido.
* **Padronização:** Uniformização de texto (espaços e maiúsculas/minúsculas) e conversão de datas para o formato real `datetime`.
* **Criação de Colunas Calculadas:** Cálculo automático do faturamento por linha (`Qtd * Preco_Unitario`) e categorização da forma de venda (Online vs. Presencial).
* **Mapeamento Geográfico:** Associação automatizada de lojas a respetivas regiões geográficas através de dicionários de equivalência (*de-para*).
* **Filtragem e Agrupamento (`Groupby`):** Geração de relatórios segmentados (ex: vendas específicas por loja) e consolidação de dados por faturamento total com ordenação decrescente.
* **Exportação Inteligente:** Preservação de dados numéricos "crus" para relatórios em Excel (`.xlsx`), garantindo total interoperabilidade com fórmulas e tabelas dinâmicas, mantendo a formatação visual com símbolos monetários (`R$`) restrita à exibição no terminal.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python** (versão 3.x recomendada)
* **Pandas** (manipulação e análise de dados)
* **NumPy** (operações lógicas condicionais e numéricas)
* **Openpyxl** (motor de suporte para leitura e escrita de ficheiros Excel)

---

## 📦 Como Instalar e Executar

1. Certifica-se de que tenha o Python instalado no seu sistema.
2. Instala as dependências necessárias executando o seguinte comando no seu terminal:
   ```bash
   pip install pandas numpy openpyxl
   ```
