# Python Intermediário part 6

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

## Funções recursivas 

A recursão é um conceito fundamental na programação onde uma função se chama a si mesma para resolver um problema. A ideia é dividir um problema em subproblemas menores e, em seguida, resolver esses subproblemas, muitas vezes de forma idêntica à solução do problema original. No contexto do Python, as funções recursivas são aquelas que se invocam a si mesmas para realizar um determinado cálculo ou tarefa.

A recursividade é útil quando se lida com problemas que podem ser divididos em casos menores e semelhantes. Ela pode tornar o código mais elegante e conciso em alguns casos, mas também é importante usá-la com cuidado, pois pode levar a problemas de desempenho e até causar erros se não for usada corretamente.

Vamos dar uma olhada em um exemplo simples para entender como a recursão funciona em Python:

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120
```

Neste exemplo, a função `fatorial` calcula o fatorial de um número `n`. Ela se chama recursivamente para calcular o fatorial de `n - 1` até atingir o caso base onde `n` é igual a 0. A recursão acontece porque a função chama a si mesma durante a sua execução.

No entanto, é importante ter em mente que a recursão pode levar a problemas como estouro de pilha (quando há muitas chamadas aninhadas, esgotando a memória disponível), portanto, é aconselhável usar recursão com parcimônia e sempre garantir que haja um caso base para encerrar as chamadas recursivas.

Além disso, em alguns casos, a recursão pode ser menos eficiente do que uma abordagem iterativa (usando loops). Portanto, é bom considerar outras alternativas de implementação, dependendo do problema que você está resolvendo.

Em resumo, a recursão em Python permite que as funções chamem a si mesmas para resolver problemas divididos em subproblemas menores. É uma ferramenta poderosa, mas que deve ser usada com cuidado e atenção aos detalhes para evitar problemas de desempenho e lógicos.

## ```Help()```

O comando `help` em Python é uma função embutida que fornece informações e documentação sobre objetos, módulos, classes, métodos e funções disponíveis na linguagem. O objetivo principal do `help` é ajudar os desenvolvedores a entenderem como usar esses elementos corretamente e a obter informações sobre suas funcionalidades.

A sintaxe básica do comando `help` é a seguinte:

```python
help(objeto)
```

Onde `objeto` pode ser qualquer coisa para a qual você deseja obter informações, como uma função, classe, método, módulo ou até mesmo um objeto específico.

Aqui estão alguns exemplos de como usar o comando `help` em Python:

1. Ajuda sobre um objeto embutido:

   ```python
   help(print)
   ```

   Isso fornecerá informações sobre a função `print`, incluindo sua sintaxe e uma breve descrição de como ela funciona.

2. Ajuda sobre um módulo:

   ```python
   import math
   help(math)
   ```

   Isso fornecerá informações sobre o módulo `math`, incluindo uma lista de funções e constantes disponíveis no módulo.

3. Ajuda sobre uma classe:

   ```python
   from datetime import datetime
   help(datetime)
   ```

   Isso fornecerá informações sobre a classe `datetime` do módulo `datetime`, incluindo detalhes sobre seus métodos e atributos.

4. Ajuda sobre um método específico:

   ```python
   lista = [1, 2, 3]
   help(lista.append)
   ```

   Isso fornecerá informações detalhadas sobre o método `append` da lista, incluindo sua sintaxe e uma descrição do que ele faz.

Ao usar o comando `help`, você pode explorar a documentação integrada do Python e obter informações detalhadas sobre os elementos que está usando em seu código, o que pode ser extremamente útil para aprender a usar novas bibliotecas, depurar problemas ou simplesmente entender melhor o funcionamento de determinados componentes do Python.
