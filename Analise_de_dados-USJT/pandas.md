# Lib Pandas

A biblioteca Pandas é uma poderosa ferramenta de análise de dados em Python. Ela fornece estruturas de dados e funções para manipulação e análise de conjuntos de dados de forma eficiente. Aqui está uma visão geral das principais características e componentes da biblioteca Pandas:

1. **DataFrame**:
   - O DataFrame é a estrutura de dados principal em Pandas.
   - É uma estrutura bidimensional de tamanho mutável com rótulos de linha e coluna.
   - Os dados em um DataFrame são geralmente tabulares, com linhas representando observações e colunas representando variáveis.

2. **Séries**:
   - Uma Série é uma estrutura de dados unidimensional semelhante a uma matriz, mas com rótulos de eixo.
   - Ela pode conter qualquer tipo de dados e é o tipo de dados fundamental usado em colunas de um DataFrame.

3. **Leitura e Escrita de Dados**:
   - Pandas oferece funções para ler e escrever dados em vários formatos, como CSV, Excel, JSON, SQL, HDF5, entre outros.
   - Essas funções facilitam a importação de dados de diferentes fontes para análise em Python.

4. **Indexação e Seleção**:
   - Pandas fornece várias maneiras poderosas de indexar e selecionar dados em DataFrames e Séries.
   - Isso inclui indexação por rótulo, indexação por posição, indexação booleana e indexação avançada.

5. **Manipulação de Dados**:
   - Pandas oferece uma ampla gama de operações para manipulação de dados, como adicionar ou remover colunas, reestruturar dados, preencher valores ausentes, filtrar dados e realizar operações de agregação.

6. **Agrupamento e Agregação**:
   - Pandas suporta operações de agrupamento para dividir os dados em grupos com base em critérios específicos e, em seguida, aplicar funções de agregação a esses grupos.
   - Isso permite realizar análises resumidas e estatísticas descritivas nos dados.

7. **Visualização de Dados**:
   - Embora Pandas em si não seja uma biblioteca de visualização, ela se integra bem com bibliotecas de visualização como Matplotlib e Seaborn para criar gráficos e visualizações a partir de dados em DataFrames e Séries.

8. **Ferramentas de Tempo**:
   - Pandas possui funcionalidades específicas para lidar com dados de séries temporais, como indexação baseada em tempo, resampling, shifting e rolling window operations.

No geral, a biblioteca Pandas é essencial para qualquer pessoa que trabalhe com análise de dados em Python, oferecendo uma ampla gama de funcionalidades para manipulação e análise eficiente de conjuntos de dados de diferentes tipos e tamanhos.

## exemplos de uso geral da biblioteca Pandas em Python:

1. **Leitura de dados de um arquivo CSV e visualização dos primeiros registros:**

```python
import pandas as pd

# Leitura de dados de um arquivo CSV
dados = pd.read_csv('dados.csv')

# Visualização dos primeiros registros
print(dados.head())
```

2. **Filtragem de dados com base em uma condição:**

```python
# Filtragem de dados para selecionar apenas as linhas onde a coluna 'idade' é maior que 30
dados_filtrados = dados[dados['idade'] > 30]
print(dados_filtrados.head())
```

3. **Adição de uma nova coluna calculada:**

```python
# Adição de uma nova coluna 'idade_em_meses' calculada a partir da coluna 'idade'
dados['idade_em_meses'] = dados['idade'] * 12
print(dados.head())
```

4. **Agrupamento de dados e cálculo de estatísticas resumidas:**

```python
# Agrupamento dos dados por 'cidade' e cálculo da média da coluna 'salario'
salario_medio_por_cidade = dados.groupby('cidade')['salario'].mean()
print(salario_medio_por_cidade)
```

5. **Visualização de dados com gráficos:**

```python
import matplotlib.pyplot as plt

# Visualização dos salários médios por cidade em um gráfico de barras
salario_medio_por_cidade.plot(kind='bar')
plt.title('Salário Médio por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Salário Médio')
plt.show()
```

6. **Trabalhando com séries temporais:**

```python
# Definindo uma série temporal com índice de datas
datas = pd.date_range(start='2024-01-01', end='2024-01-10')
valores = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
serie_temporal = pd.Series(valores, index=datas)

# Resampling para calcular a média semanal
media_semanal = serie_temporal.resample('W').mean()
print(media_semanal)
```

Esses são apenas alguns exemplos básicos de como você pode usar a biblioteca Pandas para manipular e analisar dados em Python. A versatilidade e a riqueza de funcionalidades do Pandas permitem lidar com uma ampla variedade de cenários de análise de dados.

## Em Pandas, é possível iterar sobre linhas ou colunas de um DataFrame usando métodos específicos ou estruturas de controle de fluxo padrão do Python, como loops `for`. Aqui estão algumas maneiras de realizar iteração em linhas ou colunas:

### Iteração sobre linhas:

1. **Usando iterrows():**
   - O método `iterrows()` permite iterar sobre cada linha do DataFrame como uma tupla, onde o primeiro elemento é o índice da linha e o segundo elemento é uma Series representando os valores da linha.

   Exemplo:
   ```python
   for indice, linha in dataframe.iterrows():
       # Para acessar os valores de uma linha
       print("Índice:", indice)
       print("Valores:", linha)
   ```

2. **Usando o índice de linhas diretamente:**
   - Você pode iterar diretamente sobre os índices de linhas e acessar os valores de cada linha usando o método `loc[]`.

   Exemplo:
   ```python
   for indice in dataframe.index:
       # Para acessar os valores de uma linha
       print("Índice:", indice)
       print("Valores:", dataframe.loc[indice])
   ```

### Iteração sobre colunas:

1. **Usando iteritems():**
   - O método `iteritems()` permite iterar sobre cada par de coluna-chave, onde a chave é o nome da coluna e o valor é uma Series representando os valores da coluna.

   Exemplo:
   ```python
   for coluna, serie in dataframe.iteritems():
       # Para acessar os valores de uma coluna
       print("Coluna:", coluna)
       print("Valores:", serie)
   ```

2. **Usando as colunas diretamente:**
   - Você pode iterar diretamente sobre os nomes das colunas e acessar os valores de cada coluna usando a notação de colchetes.

   Exemplo:
   ```python
   for coluna in dataframe.columns:
       # Para acessar os valores de uma coluna
       print("Coluna:", coluna)
       print("Valores:", dataframe[coluna])
   ```

É importante observar que, embora a iteração seja uma abordagem útil em muitos casos, o Pandas é otimizado para operações vetorizadas, que geralmente são mais eficientes e rápidas do que a iteração tradicional. Portanto, sempre que possível, é preferível usar operações vetorizadas em vez de iteração para manipular dados em Pandas.

## Basic

O pandas é uma biblioteca essencial em Python para análise de dados, oferecendo diversas funcionalidades para manipulação, limpeza, visualização e análise de dados. Aqui estão algumas das funções básicas mais usadas no pandas:

### 1. **Importação e Exportação de Dados**
   - `pd.read_csv()`: Lê um arquivo CSV e retorna um DataFrame.
   - `pd.read_excel()`: Lê um arquivo Excel e retorna um DataFrame.
   - `pd.to_csv()`: Exporta um DataFrame para um arquivo CSV.
   - `pd.to_excel()`: Exporta um DataFrame para um arquivo Excel.

### 2. **Criação de DataFrames e Series**
   - `pd.DataFrame()`: Cria um DataFrame a partir de um dicionário, lista, matriz numpy ou outra estrutura de dados.
   - `pd.Series()`: Cria uma Series, que é uma coluna única de dados, a partir de uma lista, dicionário, etc.

### 3. **Visualização de Dados**
   - `df.head()`: Mostra as primeiras linhas do DataFrame.
   - `df.tail()`: Mostra as últimas linhas do DataFrame.
   - `df.info()`: Mostra um resumo informativo sobre o DataFrame.
   - `df.describe()`: Gera estatísticas descritivas sobre o DataFrame.

### 4. **Seleção e Indexação de Dados**
   - `df['coluna']`: Seleciona uma coluna do DataFrame.
   - `df[['coluna1', 'coluna2']]`: Seleciona múltiplas colunas.
   - `df.iloc[]`: Seleção de dados com base em posições (índices inteiros).
   - `df.loc[]`: Seleção de dados com base em rótulos.

### 5. **Manipulação de Dados**
   - `df.drop()`: Remove colunas ou linhas especificadas.
   - `df.rename()`: Renomeia colunas ou índices.
   - `df.sort_values()`: Ordena o DataFrame por valores de uma ou mais colunas.
   - `df.sort_index()`: Ordena o DataFrame pelo índice.

### 6. **Tratamento de Dados Ausentes**
   - `df.isna()`: Retorna um DataFrame booleano indicando valores ausentes.
   - `df.dropna()`: Remove linhas ou colunas com valores ausentes.
   - `df.fillna()`: Preenche valores ausentes com um valor especificado.

### 7. **Operações de Agrupamento e Resumo**
   - `df.groupby()`: Agrupa os dados por uma ou mais colunas.
   - `df.agg()`: Aplica funções de agregação (como soma, média) aos grupos.
   - `df.pivot_table()`: Cria tabelas dinâmicas para resumir os dados.

### 8. **Mesclagem e Combinação de Dados**
   - `pd.merge()`: Mescla dois DataFrames com base em uma chave comum.
   - `pd.concat()`: Concatena múltiplos DataFrames ao longo de um eixo especificado.

### 9. **Aplicação de Funções**
   - `df.apply()`: Aplica uma função a cada coluna ou linha.
   - `df.applymap()`: Aplica uma função a cada elemento de um DataFrame.
   - `df.map()`: Aplica uma função a cada elemento de uma Series.

### 10. **Plotagem de Dados**
   - `df.plot()`: Gera gráficos a partir dos dados do DataFrame usando Matplotlib.

### Exemplo Básico

Aqui está um exemplo básico que demonstra algumas dessas funcionalidades:

```python
import pandas as pd

# Criação de um DataFrame
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 22, 30],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(data)

# Visualização dos dados
print(df.head())

# Seleção de uma coluna
idades = df['Idade']
print(idades)

# Filtragem de dados
adultos = df[df['Idade'] > 25]
print(adultos)

# Adicionando uma nova coluna
df['Ano de Nascimento'] = 2024 - df['Idade']
print(df)

# Agrupamento e resumo
media_idade = df['Idade'].mean()
print(f'Média de idade: {media_idade}')
```

Essas são apenas algumas das muitas funções que o pandas oferece para facilitar a análise e manipulação de dados.
