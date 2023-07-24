##Resumo PY

##MANIPUÇÃO DE STRING:

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

##Comandos de CONDIÇÃO:
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
##Operadores de repetição:
Os principais comandos de repetição em Python:

1. Loop "while":
O loop "while" executa um bloco de código repetidamente enquanto uma condição especificada for verdadeira.

```python
while condição:
    # código a ser executado enquanto a condição for verdadeira
```

2. Loop "for":
O loop "for" é usado para iterar sobre uma sequência (como uma lista, tupla, string, etc.) ou qualquer objeto iterável.

```python
for elemento in sequência:
    # código a ser executado para cada elemento da sequência
```

3. Comando "range":
A função "range" é usada frequentemente em loops "for" para gerar uma sequência de números.

```python
for i in range(início, fim, passo):
    # código a ser executado para cada valor gerado pela função range
```

4. Comando "break":
O comando "break" é usado para interromper a execução de um loop prematuramente, mesmo que a condição do loop ainda seja verdadeira.

```python
while condição:
    if condição_de_parada:
        break
    # código a ser executado
```

5. Comando "continue":
O comando "continue" é usado para pular para a próxima iteração do loop, ignorando o restante do código dentro do bloco do loop.

```python
for elemento in sequência:
    if condição:
        continue
    # código a ser executado, que será ignorado se a condição for verdadeira
```

Esses são os principais comandos de repetição em Python. Eles permitem que você execute um bloco de código várias vezes ou itere sobre elementos em uma sequência.

##Operadores de atribuição

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


#OPERADORES LÓGIOS:
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


##Comandos de comparação

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

## TRY-EXCEPT
O comando "try-except" em Python é uma estrutura que permite capturar e tratar exceções (erros) que podem ocorrer durante a execução de um bloco de código. É usado para lidar com situações em que você espera que um trecho de código possa gerar um erro e deseja controlar o fluxo do programa nesses casos.

A estrutura básica do comando "try-except" é a seguinte:

```python
try:
    # Bloco de código que pode gerar exceções
    # ...
except ExcecaoTipo1:
    # Tratamento para ExcecaoTipo1
    # ...
except ExcecaoTipo2:
    # Tratamento para ExcecaoTipo2
    # ...
else:
    # Bloco de código executado se nenhuma exceção for gerada
    # ...
finally:
    # Bloco de código executado sempre, independentemente de exceções
    # ...
```

Explicando cada parte:

- O bloco "try" contém o código que pode gerar uma ou mais exceções.
- Os blocos "except" especificam o tipo de exceção que queremos tratar. Podemos ter vários blocos "except" para tratar exceções diferentes. Se uma exceção ocorrer no bloco "try", o fluxo do programa será desviado para o bloco "except" correspondente ao tipo de exceção que foi gerada.
- O bloco "else" é opcional e é executado se nenhuma exceção for gerada no bloco "try". É usado para executar código que deve ser executado somente se nenhuma exceção ocorrer.
- O bloco "finally" também é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É usado para executar código que deve ser executado de qualquer maneira, como a liberação de recursos.

Exemplo:

```python
try:
    x = int(input("Digite um número inteiro: "))
    resultado = 10 / x
    print("O resultado é:", resultado)
except ValueError:
    print("Digite um valor inteiro válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Nenhuma exceção ocorreu.")
finally:
    print("Fim do programa.")
```

Neste exemplo, o bloco "try" tenta converter uma entrada de usuário em um número inteiro e, em seguida, realiza uma operação de divisão. Se um valor não inteiro for inserido ou se ocorrer uma divisão por zero, a exceção correspondente será capturada no bloco "except" apropriado e uma mensagem de erro será exibida. Se nenhuma exceção ocorrer, o bloco "else" será executado. Em qualquer caso, o bloco "finally" será executado para encerrar o programa.

O comando "try-except" é uma ferramenta poderosa para lidar com erros e garantir que o programa continue funcionando mesmo em situações inesperadas. Ele permite um controle mais preciso do fluxo do programa e a implementação de estratégias de tratamento de erros adequadas.

#LISTAS
Em Python, as listas são uma das estruturas de dados mais versáteis e amplamente utilizadas. Elas são coleções ordenadas e mutáveis de elementos, o que significa que você pode armazenar diversos valores diferentes em uma única lista e modificar sua composição ao longo do tempo. As listas são delimitadas por colchetes `[]` e podem conter elementos de tipos diferentes, inclusive outras listas. Abaixo estão algumas características importantes das listas em Python:


1. **Criação de listas:**
   Você pode criar uma lista simplesmente especificando seus elementos dentro dos colchetes, separados por vírgulas.
   ```python
   lista_numeros = [1, 2, 3, 4, 5]
   lista_frutas = ['maçã', 'banana', 'laranja']
   lista_mista = [10, 'hello', True, 3.14]
   ```

2. **Indexação:**
   Os elementos de uma lista são acessados por meio de seus índices, onde o primeiro elemento tem índice 0, o segundo tem índice 1 e assim por diante.
   ```python
   lista = ['a', 'b', 'c', 'd']
   elemento1 = lista[0]  # 'a'
   elemento2 = lista[2]  # 'c'
   ```

3. **Tamanho da lista:**
   Você pode obter o número de elementos em uma lista usando a função `len()`.
   ```python
   lista = [1, 2, 3, 4, 5]
   tamanho = len(lista)  # 5
   ```

4. **Operações básicas:**
   As listas suportam várias operações, como concatenação e repetição.
   ```python
   lista1 = [1, 2, 3]
   lista2 = [4, 5]
   concatenada = lista1 + lista2  # [1, 2, 3, 4, 5]
   repetida = lista1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
   ```

5. **Modificação de elementos:**
   As listas são mutáveis, então você pode modificar seus elementos atribuindo novos valores a eles.
   ```python
   lista = ['a', 'b', 'c']
   lista[1] = 'x'
   # lista agora é ['a', 'x', 'c']
   ```

6. **Métodos úteis:**
   As listas possuem diversos métodos úteis, como os que mencionei na resposta anterior (append, extend, insert, remove, pop, index, count, sort, reverse, clear).

7. **Aninhamento de listas:**
   Em Python, você pode criar listas que contenham outras listas, formando uma estrutura de dados mais complexa.
   ```python
   matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   ```
##Métodos na listas

Esses são alguns dos métodos mais comuns para manipulação de listas em Python. Além disso, existem outras funções e recursos úteis, como `len(lista)` para obter o tamanho da lista e `in` para verificar se um elemento está presente na lista.

1. `append(elemento)`: Adiciona um elemento ao final da lista.
```python
lista = [1, 2, 3]
lista.append(4)
# lista agora é [1, 2, 3, 4]
```

2. `extend(outra_lista)`: Adiciona os elementos de outra lista ao final da lista atual.
```python
lista1 = [1, 2, 3]
lista2 = [4, 5]
lista1.extend(lista2)
# lista1 agora é [1, 2, 3, 4, 5]
```

3. `insert(indice, elemento)`: Insere um elemento em um índice específico da lista.
```python
lista = [1, 2, 3]
lista.insert(1, 4)
# lista agora é [1, 4, 2, 3]
```

4. `remove(elemento)`: Remove a primeira ocorrência do elemento na lista.
```python
lista = [1, 2, 3, 2]
lista.remove(2)
# lista agora é [1, 3, 2]
```

5. `pop([indice])`: Remove e retorna o elemento no índice especificado. Se nenhum índice for dado, remove o último elemento da lista.
```python
lista = [1, 2, 3]
elemento_removido = lista.pop(1)
# lista agora é [1, 3], elemento_removido é 2
```

6. `index(elemento)`: Retorna o índice da primeira ocorrência do elemento na lista.
```python
lista = [1, 2, 3, 2]
indice = lista.index(2)
# indice é 1
```

7. `count(elemento)`: Retorna o número de ocorrências do elemento na lista.
```python
lista = [1, 2, 3, 2]
ocorrencias = lista.count(2)
# ocorrencias é 2
```

8. `sort()`: Ordena a lista em ordem crescente. (A lista deve conter elementos do mesmo tipo ou tipos que possam ser comparados.)
```python
lista = [3, 1, 2]
lista.sort()
# lista agora é [1, 2, 3]
```

9. `reverse()`: Inverte a ordem dos elementos na lista.
```python
lista = [1, 2, 3]
lista.reverse()
# lista agora é [3, 2, 1]
```

10. `clear()`: Remove todos os elementos da lista.
```python
lista = [1, 2, 3]
lista.clear()
# lista agora é []
```

As listas são uma parte fundamental da linguagem Python e são amplamente usadas em várias situações, desde o armazenamento de dados simples até a implementação de algoritmos mais complexos. Sua flexibilidade e variedade de métodos tornam-nas uma escolha poderosa para muitos cenários de programação.


#BIBLIOTECA PANDA

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

#biblioteca NumPy:

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
