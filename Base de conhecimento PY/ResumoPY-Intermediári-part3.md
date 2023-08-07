# Resumo PYthon intermediário - part 3 

## List Comprehension

A list comprehension é uma construção sintática poderosa e concisa na linguagem de programação Python que permite criar listas de forma eficiente. Ela é usada para criar novas listas aplicando uma expressão a cada elemento de uma sequência (como uma lista, tupla, string, etc.), ao mesmo tempo que permite filtrar os elementos da sequência original com base em uma condição.

A estrutura básica de uma list comprehension é a seguinte:

```python
nova_lista = [expressão for elemento in sequência original if condição]
```

Aqui está uma explicação dos componentes:

- `expressão`: É a operação que você deseja executar em cada elemento da sequência original para criar o novo valor na lista resultante.

- `elemento`: Variável que representa cada elemento da sequência original conforme ela é percorrida.

- `sequência original`: A coleção de elementos sobre a qual você está iterando, como uma lista, tupla ou string.

- `condição` (opcional): Uma expressão booleana que permite filtrar os elementos da sequência original. Apenas os elementos que atendem à condição serão incluídos na lista resultante.

Aqui estão alguns exemplos para ilustrar como as list comprehensions funcionam:

1. Criar uma lista de quadrados dos números de 0 a 9:
```python
quadrados = [x**2 for x in range(10)]
```

2. Filtrar apenas os números pares de uma lista:
```python
numeros_pares = [x for x in range(20) if x % 2 == 0]
```

3. Converter uma lista de strings em uma lista de seus comprimentos correspondentes:
```python
palavras = ['python', 'é', 'incrível']
comprimentos = [len(word) for word in palavras]
```

4. Criar uma lista de números positivos de outra lista:
```python
numeros = [-2, 5, -9, 10, -3, 7]
numeros_positivos = [x for x in numeros if x > 0]
```

As list comprehensions são uma maneira eficiente e legível de criar listas em Python, tornando o código mais conciso e fácil de entender. No entanto, lembre-se de não exagerar na complexidade das expressões e condições dentro das list comprehensions, pois isso pode prejudicar a legibilidade do código.

Em list comprehensions em Python, você pode usar mapeamento e filtragem para criar listas de maneira mais eficiente e concisa. Mapeamento refere-se à aplicação de uma operação a cada elemento da sequência original para criar novos elementos na lista resultante. Filtros envolvem a inclusão seletiva de elementos da sequência original, com base em uma condição.

Vamos explorar esses conceitos em mais detalhes:

### Mapeamento:

Mapeamento envolve a aplicação de uma expressão ou função a cada elemento da sequência original, gerando novos valores que comporão a lista resultante.

Sintaxe para mapeamento em list comprehension:
```python
nova_lista = [expressão(elemento) for elemento in sequência original]
```

Exemplo de mapeamento:
```python
# Criar uma lista de quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
```

### Filtros:

Filtros permitem incluir elementos da sequência original com base em uma condição. Somente os elementos que atendem à condição serão incluídos na lista resultante.

Sintaxe para filtragem em list comprehension:
```python
nova_lista = [expressão for elemento in sequência original if condição]
```

Exemplo de filtragem:
```python
# Filtrar apenas os números pares de uma lista
numeros_pares = [x for x in range(20) if x % 2 == 0]
```

### Mapeamento e Filtros Combinados:

Você também pode combinar mapeamento e filtros em uma única list comprehension para criar listas que atendam a ambos os critérios.

Exemplo de mapeamento e filtragem combinados:
```python
# Criar uma lista dos cubos dos números ímpares de 1 a 10
cubos_impares = [x**3 for x in range(1, 11) if x % 2 != 0]
```

A combinação de mapeamento e filtros em list comprehensions permite que você crie listas de forma eficiente e elegante, reduzindo a necessidade de loops explícitos e tornando o código mais legível.

Lembre-se de que, embora list comprehensions sejam poderosas, você deve usá-las com moderação e considerar a clareza do código. Às vezes, para operações mais complexas ou quando a legibilidade é mais importante, pode ser mais apropriado usar loops regulares ou funções separadas.

## Dict Comprehension

A compreensão de dicionário (dictionary comprehension) é uma construção poderosa em Python que permite criar dicionários de forma concisa e eficiente. Ela é semelhante à compreensão de lista (list comprehension), mas em vez de criar listas, você cria dicionários. A compreensão de dicionário pode ser útil quando você precisa transformar ou filtrar dados para criar um novo dicionário.

A sintaxe básica da compreensão de dicionário é a seguinte:

```python
{chave: valor for item in sequência}
```

Aqui está um exemplo simples para ilustrar o conceito:

```python
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)  # Saída: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Você também pode adicionar uma condição para filtrar os itens antes de adicioná-los ao dicionário:

```python
numbers = [1, 2, 3, 4, 5]
even_squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(even_squares)  # Saída: {2: 4, 4: 16}
```

Além disso, você pode iterar sobre duas sequências simultaneamente usando a função `zip()`:

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {key: value for key, value in zip(keys, values)}
print(combined_dict)  # Saída: {'a': 1, 'b': 2, 'c': 3}
```

Lembre-se de que as chaves em um dicionário devem ser únicas. Se houver chaves duplicadas na compreensão de dicionário, o último valor correspondente será mantido.

A compreensão de dicionário é uma maneira elegante e eficiente de criar dicionários em Python, reduzindo a necessidade de loops explícitos e simplificando o código. Ela é amplamente utilizada em situações onde você precisa transformar ou filtrar dados em um dicionário.

## Set comprehension

A compreensão de conjunto (set comprehension) é uma construção em Python que permite criar conjuntos de forma concisa e eficiente. Assim como as compreensões de lista e dicionário, a compreensão de conjunto permite criar conjuntos a partir de uma expressão iterada. A principal característica dos conjuntos é que eles não permitem duplicatas, ou seja, cada elemento em um conjunto é único.

A sintaxe básica da compreensão de conjunto é semelhante à compreensão de lista e à compreensão de dicionário:

```python
{expressão for item in sequência}
```

Aqui está um exemplo simples para ilustrar o conceito:

```python
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {num ** 2 for num in numbers}
print(unique_squares)  # Saída: {16, 1, 4, 9, 25}
```

Observe que os elementos duplicados foram automaticamente removidos no conjunto resultante.

Você também pode adicionar uma condição para filtrar os itens antes de adicioná-los ao conjunto:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {num ** 2 for num in numbers if num % 2 == 0}
print(even_squares)  # Saída: {64, 4, 100, 16, 36}
```

Assim como nas outras compreensões, você também pode usar a função `zip()` para combinar elementos de duas sequências em um conjunto:

```python
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined_set = {letter + str(number) for letter, number in zip(letters, numbers)}
print(combined_set)  # Saída: {'a1', 'c3', 'b2'}
```

A compreensão de conjunto é uma maneira eficaz de criar conjuntos únicos a partir de expressões iteradas. Ela é útil quando você deseja remover duplicatas e criar coleções de elementos únicos.
