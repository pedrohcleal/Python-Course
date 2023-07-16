Resumo PY

MANIPUÇÃO DE STRING:

1. Concatenação de strings:
   - `+`: Concatena duas strings.
   - `str.join()`: Concatena uma lista de strings usando um separador.

2. Tamanho e informações sobre strings:
   - `len()`: Retorna o tamanho (número de caracteres) de uma string.
   - `str.lower()`: Retorna uma cópia da string convertida para minúsculas.
   - `str.upper()`: Retorna uma cópia da string convertida para maiúsculas.
   - `str.capitalize()`: Retorna uma cópia da string com a primeira letra em maiúscula.
   - `str.title()`: Retorna uma cópia da string com a primeira letra de cada palavra em maiúscula.

3. Acesso a caracteres e fatiamento de strings:
   - Indexação: Acessa um caractere específico da string usando um índice.
   - Fatiamento: Seleciona uma parte da string com base em intervalos.

4. Busca e substituição:
   - `str.find()`: Retorna o índice da primeira ocorrência de uma substring.
   - `str.rfind()`: Retorna o índice da última ocorrência de uma substring.
   - `str.startswith()`: Verifica se uma string começa com uma substring.
   - `str.endswith()`: Verifica se uma string termina com uma substring.
   - `str.replace()`: Substitui todas as ocorrências de uma substring por outra.

5. Separação e junção:
   - `str.split()`: Divide a string em uma lista de substrings com base em um separador.
   - `str.splitlines()`: Divide a string em uma lista de substrings em quebras de linha.
   - `str.join()`: Concatena uma lista de strings usando a string como separador.

6. Remoção de espaços em branco:
   - `str.strip()`: Remove espaços em branco no início e no final da string.
   - `str.lstrip()`: Remove espaços em branco no início da string.
   - `str.rstrip()`: Remove espaços em branco no final da string.

7. Verificação de tipo de caracteres:
   - `str.isdigit()`: Verifica se a string contém apenas dígitos.
   - `str.isalpha()`: Verifica se a string contém apenas letras.
   - `str.isalnum()`: Verifica se a string contém apenas letras e dígitos.

Comandos de CONDIÇÃO:
Em Python, os comandos de condição são usados para executar blocos de código com base em condições lógicas. Os comandos de condição mais comuns são:

1. Comando `if`:
   O comando `if` é usado para executar um bloco de código se uma condição for avaliada como verdadeira.

   ```python
   if condição:
       # Código a ser executado se a condição for verdadeira
   ```

2. Comando `if...else`:
   O comando `if...else` é usado para executar um bloco de código se a condição for avaliada como verdadeira e outro bloco de código se a condição for avaliada como falsa.

   ```python
   if condição:
       # Código a ser executado se a condição for verdadeira
   else:
       # Código a ser executado se a condição for falsa
   ```

3. Comando `if...elif...else`:
   O comando `if...elif...else` é usado quando há várias condições para serem avaliadas. Ele verifica cada condição sequencialmente e executa o bloco de código associado à primeira condição verdadeira. Se nenhuma das condições for verdadeira, o bloco de código associado a `else` é executado.

   ```python
   if condição1:
       # Código a ser executado se condição1 for verdadeira
   elif condição2:
       # Código a ser executado se condição2 for verdadeira
   else:
       # Código a ser executado se nenhuma das condições anteriores for verdadeira
   ```

4. Operador ternário:
   O operador ternário é uma forma concisa de escrever uma estrutura condicional de uma linha.

   ```python
   variável = valor1 if condição else valor2
   ```


Operadores de atribuição

#são usados para atribuir valores a variáveis. Aqui estão todos os operadores de atribuição disponíveis em Python:

1. Operador de atribuição simples: "="
   Exemplo: ```x = 10```

2. Operador de atribuição com adição: "+="
   Exemplo: ```x += 5``` é equivalente a ```x = x + 5```

3. Operador de atribuição com subtração: "-="
   Exemplo: ```x -= 5``` é equivalente a ```x = x - 5```

4. Operador de atribuição com multiplicação: "*="
   Exemplo: ```x *= 5``` é equivalente a ```x = x * 5```

5. Operador de atribuição com divisão: "/="
   Exemplo: ```x /= 5``` é equivalente a ```x = x / 5```

6. Operador de atribuição com divisão inteira: "//="
   Exemplo: ```x //= 5``` é equivalente a ```x = x // 5```

7. Operador de atribuição com resto: "%="
   Exemplo: ```x %= 5``` é equivalente a ```x = x % 5```

8. Operador de atribuição com exponenciação: "**="
   Exemplo: ```x **= 5``` é equivalente a ```x = x ** 5```

9. Operador de atribuição com operação bitwise AND: "&="
   Exemplo: ```x &= 5``` é equivalente a ```x = x & 5```

10. Operador de atribuição com operação bitwise OR: "|="
    Exemplo: ```x |= 5``` é equivalente a ```x = x | 5```

11. Operador de atribuição com operação bitwise XOR: "^="
    Exemplo: ```x ^= 5``` é equivalente a ```x = x ^ 5```

12. Operador de atribuição com operação bitwise de deslocamento à esquerda: "<<="
    Exemplo: ```x <<= 5``` é equivalente a ```x = x << 5```

13. Operador de atribuição com operação bitwise de deslocamento à direita: ">>="
    Exemplo: ```x >>= 5``` é equivalente a ```x = x >> 5```

Esses são os operadores de atribuição em Python, que podem ser usados para atualizar valores de variáveis de forma concisa.


OPERADORES LÓGIOS:
Em Python, existem três operadores lógicos principais: `and`, `or` e `not`. Aqui estão os operadores lógicos e exemplos de seu uso:

1. Operador `and`:
   O operador `and` retorna `True` se todas as expressões forem verdadeiras, caso contrário, retorna `False`.
   
   Exemplo:
   ```python
   a = 10
   b = 5
   c = 7
   
   resultado = (a > b) and (b < c)
   print(resultado)  # Saída: True
   ```

2. Operador `or`:
   O operador `or` retorna `True` se pelo menos uma das expressões for verdadeira, caso contrário, retorna `False`.
   
   Exemplo:
   ```python
   a = 10
   b = 5
   c = 7
   
   resultado = (a > b) or (b > c)
   print(resultado)  # Saída: True
   ```

3. Operador `not`:
   O operador `not` inverte o valor de uma expressão. Se a expressão for verdadeira, o `not` retorna `False`, e se a expressão for falsa, o `not` retorna `True`.
   
   Exemplo:
   ```python
   a = 10
   b = 5
   
   resultado = not (a > b)
   print(resultado)  # Saída: False
   ```


Comandos de comparação

Aqui estão alguns comandos de comparação em Python:

1. Igualdade (`==`): Verifica se dois valores são iguais.
   Exemplo: `2 == 2` retorna `True`.

2. Desigualdade (`!=`): Verifica se dois valores são diferentes.
   Exemplo: `3 != 5` retorna `True`.

3. Maior que (`>`): Verifica se um valor é maior que outro.
   Exemplo: `10 > 5` retorna `True`.

4. Menor que (`<`): Verifica se um valor é menor que outro.
   Exemplo: `3 < 7` retorna `True`.

5. Maior ou igual a (`>=`): Verifica se um valor é maior ou igual a outro.
   Exemplo: `4 >= 4` retorna `True`.

6. Menor ou igual a (`<=`): Verifica se um valor é menor ou igual a outro.
   Exemplo: `6 <= 8` retorna `True`.

7. Pertencimento (`in`): Verifica se um valor está contido em uma sequência (como uma lista, tupla ou string).
   Exemplo: `'a' in 'abcd'` retorna `True`.

8. Não pertencimento (`not in`): Verifica se um valor não está contido em uma sequência.
   Exemplo: `'x' not in ['a', 'b', 'c']` retorna `True`.

9. Identidade (`is`): Verifica se dois objetos têm a mesma identidade (referenciam o mesmo objeto na memória).
   Exemplo: `x is y` retorna `True` se `x` e `y` referenciarem o mesmo objeto.

10. Não identidade (`is not`): Verifica se dois objetos têm identidades diferentes.
    Exemplo: `x is not y` retorna `True` se `x` e `y` referenciarem objetos diferentes.


BIBLIOTECA PANDA

A biblioteca pandas é uma biblioteca poderosa para manipulação e análise de dados em Python. Aqui estão alguns dos principais comandos e recursos disponíveis na biblioteca pandas:

1. `import pandas as pd`: Importa a biblioteca pandas e a renomeia para `pd` para facilitar o uso.

2. Estruturas de Dados:
   - `pd.Series()`: Cria uma série unidimensional, similar a uma coluna em uma planilha do Excel.
   - `pd.DataFrame()`: Cria um DataFrame, uma estrutura bidimensional para dados tabulares, semelhante a uma planilha.

3. Leitura de Dados:
   - `pd.read_csv()`: Lê um arquivo CSV e retorna um DataFrame.
   - `pd.read_excel()`: Lê um arquivo Excel e retorna um DataFrame.
   - `pd.read_sql()`: Lê dados de uma tabela em um banco de dados SQL e retorna um DataFrame.

4. Manipulação de Dados:
   - `df.head()`: Retorna as primeiras linhas do DataFrame.
   - `df.tail()`: Retorna as últimas linhas do DataFrame.
   - `df.info()`: Fornece informações sobre o DataFrame, como tipos de dados e estatísticas básicas.
   - `df.describe()`: Calcula estatísticas descritivas para colunas numéricas do DataFrame.
   - `df.shape`: Retorna o número de linhas e colunas do DataFrame.
   - `df.columns`: Retorna os nomes das colunas do DataFrame.
   - `df.dtypes`: Retorna os tipos de dados das colunas do DataFrame.
   - `df.groupby()`: Agrupa o DataFrame com base em uma ou mais colunas.
   - `df.sort_values()`: Classifica o DataFrame com base em uma ou mais colunas.
   - `df.drop()`: Remove linhas ou colunas específicas do DataFrame.
   - `df.rename()`: Renomeia colunas do DataFrame.
   - `df.merge()`: Combina dois DataFrames com base em uma ou mais colunas em comum.

5. Escrita de Dados:
   - `df.to_csv()`: Salva o DataFrame em um arquivo CSV.
   - `df.to_excel()`: Salva o DataFrame em um arquivo Excel.
   - `df.to_sql()`: Salva o DataFrame em uma tabela de um banco de dados SQL.

biblioteca NumPy:

1. `import numpy as np`: Importa a biblioteca NumPy e a renomeia para `np` para facilitar o uso.

2. Arrays NumPy:
   - `np.array()`: Cria um array NumPy multidimensional.
   - `np.zeros()`: Cria um array preenchido com zeros.
   - `np.ones()`: Cria um array preenchido com uns.
   - `np.arange()`: Cria um array com valores espaçados uniformemente dentro de um intervalo.
   - `np.linspace()`: Cria um array com valores espaçados linearmente dentro de um intervalo.
   - `np.random.rand()`: Cria um array com valores aleatórios entre 0 e 1.
   - `np.random.randn()`: Cria um array com valores aleatórios seguindo uma distribuição normal.
   - `np.reshape()`: Modifica a forma de um array.

3. Operações com Arrays:
   - `np.shape()`: Retorna as dimensões de um array.
   - `np.ndim()`: Retorna o número de dimensões de um array.
   - `np.size()`: Retorna o número total de elementos de um array.
   - `np.dtype()`: Retorna o tipo de dados de um array.
   - `np.min()`, `np.max()`: Retorna o valor mínimo e máximo de um array.
   - `np.sum()`: Retorna a soma dos elementos de um array.
   - `np.mean()`: Retorna a média dos elementos de um array.
   - `np.median()`: Retorna a mediana dos elementos de um array.
   - `np.std()`: Retorna o desvio padrão dos elementos de um array.

4. Indexação e Fatiamento de Arrays:
   - Indexação Simples: Acessa elementos individuais de um array.
   - Fatiamento: Seleciona uma parte de um array com base em intervalos.
   - Indexação Booleana: Seleciona elementos com base em condições booleanas.
   - Indexação Avançada: Permite selecionar elementos de um array usando índices ou arrays de índices.

5. Operações Matemáticas:
   - `np.add()`: Adição de elementos de dois arrays.
   - `np.subtract()`: Subtração de elementos de dois arrays.
   - `np.multiply()`: Multiplicação de elementos de dois arrays.
   - `np.divide()`: Divisão de elementos de dois arrays.
   - `np.dot()`: Produto escalar ou multiplicação de matrizes.

6. Funções Matemáticas:
   - `np.sin()`, `np.cos()`, `np.tan()`: Funções trigonométricas.
   - `np.exp()`, `np.log()`, `np.sqrt()`: Funções exponenciais, logarítmicas e raiz quadrada.
   - `np.sum()`, `np.mean()`, `np.median()`: Funções de agregação aplicadas a um array.
  

  Para criar um documento com resumos de Python em seu repositório do GitHub, você pode usar a formatação Markdown. O Markdown é uma linguagem de marcação leve e fácil de usar, adequada para criar conteúdo formatado em plataformas como o GitHub.

Aqui está um exemplo de como você pode criar um documento em Markdown para seus resumos de Python:

1. Crie um novo arquivo no seu repositório do GitHub com a extensão `.md`, por exemplo, `python_resumos.md`.

2. Abra o arquivo em um editor de texto e comece a escrever seu conteúdo.

3. Use os recursos do Markdown para formatar o texto de acordo com suas necessidades. Alguns exemplos comuns são:

   - Cabeçalhos: Use `#` para criar cabeçalhos de diferentes níveis. Por exemplo:
     ```
     # Resumo de Python
     ## Introdução
     ### Estruturas de Controle
     ```

   - Listas: Use `-` ou `*` para criar listas não ordenadas e `1.`, `2.`, etc., para criar listas ordenadas.
     ```
     - Conceitos básicos de Python
     - Variáveis e tipos de dados
     - Estruturas de controle:
       - Condicionais
       - Loops
     ```

   - Formatação de texto: Use `**` ou `__` para negrito e `*` ou `_` para itálico.
     ```
     Python é uma **linguagem de programação** poderosa e de fácil aprendizado.
     ```

   - Blocos de código: Use três backticks (\`) para criar blocos de código.
     ```
     ```python
     def saudacao(nome):
         print(f"Olá, {nome}!")
     ```
     ```

   - Links: Use `[texto do link](URL)` para criar links.
     ```
     Para mais informações, visite a [documentação oficial do Python](https://docs.python.org/3/).
     ```

4. Salve o arquivo e faça o commit no seu repositório do GitHub.

Ao utilizar a formatação Markdown, você pode criar um documento bem estruturado e legível para compartilhar seus resumos de Python em seu repositório do GitHub. 
Certifique-se de revisar a sintaxe Markdown para aproveitar ao máximo os recursos disponíveis.
