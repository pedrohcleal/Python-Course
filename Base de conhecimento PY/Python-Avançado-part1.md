# Python Avançado


## Tipo `array` da lin `array`

A biblioteca `array` do Python fornece um tipo de array que é mais eficiente em termos de memória do que listas para armazenar grandes quantidades de elementos do mesmo tipo. Este tipo de array armazena os elementos em memória contígua, o que pode melhorar o desempenho em termos de tempo e espaço em comparação com listas. 

Aqui está um exemplo básico de como usar a biblioteca `array`:

```python
import array

# Criando um array de inteiros
arr = array.array('i', [1, 2, 3, 4, 5])

print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
print(arr[2])  # Output: 3
```

### Principais Características:
- **Tipos de Dados**: Você deve especificar o tipo de dados dos elementos no array (por exemplo, `'i'` para inteiros, `'f'` para floats).
- **Eficiência**: Os arrays são mais eficientes em termos de memória do que listas quando todos os elementos são do mesmo tipo.
- **Métodos**: Suporta métodos como `append()`, `extend()`, `insert()`, `remove()`, entre outros.

## Módulo `collections`

O módulo `collections` fornece vários tipos de dados alternativos que podem ser usados para armazenar coleções de elementos de maneira eficiente e conveniente. Alguns dos tipos mais comuns são:

### `deque`

`deque` (double-ended queue) é uma estrutura de dados que permite adicionar e remover elementos de ambos os lados de forma eficiente.

```python
from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.appendleft(0)  # Adiciona 0 no início
dq.append(6)  # Adiciona 6 no final

print(dq)  # Output: deque([0, 1, 2, 3, 4, 5, 6])
print(dq.pop())  # Remove e retorna o último elemento, output: 6
print(dq.popleft())  # Remove e retorna o primeiro elemento, output: 0
```

### `defaultdict`

`defaultdict` é um dicionário que retorna um valor padrão se a chave não existir.

```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1

print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1})
```

### `Counter`

`Counter` é uma subclasse de dicionário que é usada para contar objetos hashables.

```python
from collections import Counter

cnt = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(cnt)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})
```

### `namedtuple`

`namedtuple` é uma fábrica de funções para criar subclasses de tuplas com campos nomeados.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p)  # Output: Point(x=10, y=20)
print(p.x)  # Output: 10
print(p.y)  # Output: 20
```

### `OrderedDict`

`OrderedDict` é um dicionário que mantém a ordem de inserção dos elementos.

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

Essas ferramentas fornecem formas mais especializadas e eficientes de trabalhar com coleções de dados em Python.
