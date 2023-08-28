## filter()
A função `filter()` é outra função integrada em Python que permite filtrar elementos de uma sequência (como uma lista, tupla ou outro iterável) com base em uma função de teste. Ela retorna um iterador contendo os elementos da sequência original que passam no teste definido pela função.

A sintaxe básica da função `filter()` é a seguinte:

```python
filter(função_de_teste, sequência)
```

- `função_de_teste`: Uma função que define o critério de filtragem. Deve retornar `True` para os elementos que você deseja manter na sequência e `False` para os elementos que deseja filtrar.
- `sequência`: A sequência de elementos que você deseja filtrar.

Aqui está um exemplo simples de uso da função `filter()`:

```python
def é_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(é_par, numeros)
numeros_pares_lista = list(numeros_pares)  # Convertendo o iterador resultante em uma lista
print(numeros_pares_lista)  # Saída: [2, 4, 6, 8, 10]
```

No exemplo acima, a função `é_par()` é usada como critério de filtro. A função `filter()` aplica a função `é_par()` a cada elemento da lista `numeros`, retornando apenas os números pares.

Outra forma comum de usar `filter()` é com funções lambda (funções anônimas) para criar filtros simples:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x % 2 == 0, numeros)
numeros_pares_lista = list(numeros_pares)
print(numeros_pares_lista)  # Saída: [2, 4, 6, 8, 10]
```

A função `filter()` é útil quando você deseja extrair elementos de uma sequência com base em algum critério específico, economizando tempo e código comparado a loops explícitos de iteração.

## reduce()
A função `reduce()` também é uma função integrada em Python, mas, diferente das funções `map()` e `filter()`, ela não faz parte das funções built-in a partir do Python 3. A partir da versão 3, a função `reduce()` foi movida para o módulo `functools`, portanto, para usá-la, é necessário importá-la primeiro.

A função `reduce()` é projetada para acumular ou reduzir uma sequência de elementos a um único valor aplicando uma função repetidamente aos elementos da sequência. Ela foi inspirada por uma operação comum em programação funcional chamada "fold" ou "fold/reduce". A ideia é aplicar uma operação binária iterativa a todos os elementos da sequência, acumulando um resultado.

A sintaxe básica da função `reduce()` é a seguinte:

```python
functools.reduce(função, sequência, valor_inicial)
```

- `função`: Uma função que recebe dois argumentos e realiza a operação binária entre eles.
- `sequência`: A sequência de elementos que você deseja reduzir.
- `valor_inicial`: O valor inicial para o acumulador. Esse argumento é opcional.

Aqui está um exemplo simples de uso da função `reduce()`:

```python
from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
soma_total = reduce(soma, numeros)
print(soma_total)  # Saída: 15 (1 + 2 + 3 + 4 + 5)
```

Neste exemplo, a função `soma()` é aplicada repetidamente aos elementos da lista `numeros`, acumulando um valor total.

Se você quiser fornecer um valor inicial para o acumulador, você pode fazer assim:

```python
soma_total_com_inicial = reduce(soma, numeros, 10)
print(soma_total_com_inicial)  # Saída: 25 (10 + 1 + 2 + 3 + 4 + 5)
```

A função `reduce()` pode ser poderosa para situações em que você precisa combinar todos os elementos de uma sequência usando uma operação específica, como cálculos matemáticos ou manipulação de dados. No entanto, observe que a função `reduce()` não é tão comum quanto as funções `map()` e `filter()`, pois sua funcionalidade pode muitas vezes ser atingida de maneira mais clara e legível com loops simples ou list comprehensions.
