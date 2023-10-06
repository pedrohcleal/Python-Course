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

### DictWriter e DictReader

`DictWriter` e `DictReader` são duas classes da biblioteca `csv` do Python que permitem trabalhar com arquivos CSV usando dicionários em vez de listas. Isso pode ser muito útil quando você deseja ler ou escrever dados CSV em que cada linha é representada como um dicionário, onde as chaves são os nomes das colunas e os valores são os dados correspondentes. Essas classes tornam a manipulação de dados CSV mais intuitiva quando você tem informações tabulares com cabeçalhos nomeados.

Aqui está uma descrição de cada uma dessas classes:

1. **`DictWriter` (Escrita de Dados CSV):**
   A classe `DictWriter` é usada para escrever dados em um arquivo CSV usando dicionários como entrada. Isso significa que você pode especificar os dados a serem escritos em cada linha do arquivo CSV usando dicionários onde as chaves correspondem aos nomes das colunas.

   Exemplo de uso do `DictWriter`:

   ```python
   import csv

   dados = [
       {'Nome': 'João', 'Idade': 30, 'Cidade': 'São Paulo'},
       {'Nome': 'Maria', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
       {'Nome': 'Carlos', 'Idade': 35, 'Cidade': 'Belo Horizonte'}
   ]

   with open('dados_dictwriter.csv', 'w', newline='') as arquivo_csv:
       campos = ['Nome', 'Idade', 'Cidade']
       escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
       escritor_csv.writeheader()
       for linha in dados:
           escritor_csv.writerow(linha)
   ```

   Neste exemplo, usamos `DictWriter` para escrever dados em um arquivo CSV, especificando os campos (ou colunas) usando `fieldnames` e escrevendo os dados linha por linha.

2. **`DictReader` (Leitura de Dados CSV):**
   A classe `DictReader` é usada para ler dados de um arquivo CSV em que cada linha é representada como um dicionário. Isso facilita muito a leitura e manipulação de dados, pois você pode acessar os valores por meio de nomes de colunas em vez de índices de lista.

   Exemplo de uso do `DictReader`:

   ```python
   import csv

   with open('dados_dictwriter.csv', 'r') as arquivo_csv:
       leitor_csv = csv.DictReader(arquivo_csv)
       for linha in leitor_csv:
           print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
   ```

   Neste exemplo, usamos `DictReader` para ler os dados do arquivo CSV e acessamos os valores de cada linha usando as chaves dos dicionários correspondentes aos nomes das colunas.

O uso de `DictWriter` e `DictReader` torna a leitura e escrita de dados CSV mais legível e mais fácil de trabalhar, especialmente quando você tem dados CSV com muitas colunas ou precisa realizar manipulações complexas em seus dados tabulares.
