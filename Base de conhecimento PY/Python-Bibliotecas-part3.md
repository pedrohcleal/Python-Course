# Bibliotecas Py part 3

## CSV

CSV, que significa "Comma-Separated Values" (Valores Separados por Vírgula), é um formato comum para armazenar dados tabulares em texto plano. No Python, você pode trabalhar com arquivos CSV usando a biblioteca `csv`, que oferece funcionalidades para ler, escrever e manipular dados nesse formato.

Aqui está uma visão geral das principais operações com arquivos CSV em Python:

1. **Leitura de Arquivos CSV:**
   Para ler dados de um arquivo CSV, você pode usar a classe `csv.reader`. Aqui está um exemplo de como fazer isso:

   ```python
   import csv

   with open('arquivo.csv', 'r') as arquivo_csv:
       leitor_csv = csv.reader(arquivo_csv)
       for linha in leitor_csv:
           print(linha)
   ```

   Isso abrirá o arquivo 'arquivo.csv' e lerá suas linhas como listas de valores, onde os valores são separados por vírgulas.

2. **Escrita em Arquivos CSV:**
   Para escrever dados em um arquivo CSV, você pode usar a classe `csv.writer`. Aqui está um exemplo simples:

   ```python
   import csv

   dados = [
       ['Nome', 'Idade', 'Cidade'],
       ['João', 30, 'São Paulo'],
       ['Maria', 25, 'Rio de Janeiro']
   ]

   with open('arquivo.csv', 'w', newline='') as arquivo_csv:
       escritor_csv = csv.writer(arquivo_csv)
       for linha in dados:
           escritor_csv.writerow(linha)
   ```

   Isso criará um arquivo 'arquivo.csv' com os dados fornecidos, separados por vírgulas.

3. **Manipulação de Dados CSV:**
   A biblioteca `csv` também fornece funcionalidades para manipular dados CSV, como adicionar, modificar ou remover linhas e colunas. Você pode ler os dados em uma estrutura de dados, como uma lista de listas ou um dicionário, fazer as manipulações necessárias e, em seguida, escrever os dados de volta no arquivo CSV.

4. **Configurações Adicionais:**
   A biblioteca `csv` oferece várias opções para personalizar a leitura e a escrita de arquivos CSV, como o delimitador (que nem sempre precisa ser uma vírgula), o caractere de escape e o comportamento de delimitação de aspas.

Em resumo, a biblioteca `csv` do Python é uma ferramenta poderosa para trabalhar com dados em formato CSV. Ela simplifica a leitura, escrita e manipulação de dados tabulares, tornando-a uma escolha popular para tarefas que envolvem processamento de dados CSV.
