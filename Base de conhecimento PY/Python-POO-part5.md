# POO Part5

## Classe Enum

Em Python, a classe `Enum` faz parte do módulo `enum`, que foi introduzido na versão 3.4 da linguagem. Enums são utilizados para criar conjuntos de constantes nomeadas, o que torna o código mais legível e evita erros relacionados a valores mágicos (números ou strings diretamente incorporados no código).

Aqui está uma descrição básica de como usar a classe `Enum` em Python:

1. Importar o módulo `enum`:

   Para começar a usar Enums, você deve importar o módulo `enum`:

   ```python
   from enum import Enum
   ```

2. Definir uma classe Enum:

   Você pode criar uma classe Enum estendendo a classe base `Enum`. Cada membro da enumeração é definido como uma instância dessa classe. Aqui está um exemplo simples:

   ```python
   from enum import Enum

   class DiaDaSemana(Enum):
       SEGUNDA = 1
       TERCA = 2
       QUARTA = 3
       QUINTA = 4
       SEXTA = 5
       SABADO = 6
       DOMINGO = 7
   ```

   Neste exemplo, criamos uma enumeração chamada `DiaDaSemana` com sete membros, cada um representando um dia da semana.

3. Acesso aos membros da enumeração:

   Agora você pode acessar os membros da enumeração como atributos da classe `DiaDaSemana`. Por exemplo:

   ```python
   >>> print(DiaDaSemana.SEGUNDA)
   DiaDaSemana.SEGUNDA
   >>> print(DiaDaSemana.SEGUNDA.value)
   1
   ```

   O atributo `.value` fornece o valor associado a cada membro da enumeração.

4. Comparação de membros da enumeração:

   Você pode comparar membros da enumeração usando operadores de igualdade. Por exemplo:

   ```python
   >>> hoje = DiaDaSemana.SEGUNDA
   >>> amanha = DiaDaSemana.TERCA
   >>> print(hoje == amanha)
   False
   ```

5. Iteração sobre membros da enumeração:

   É possível iterar sobre todos os membros de uma enumeração usando um loop `for`:

   ```python
   for dia in DiaDaSemana:
       print(dia)
   ```

   Isso irá imprimir todos os membros da enumeração na ordem em que foram definidos.

Enums são úteis para tornar o código mais legível e evitar erros de digitação, já que os membros da enumeração são constantes nomeadas e não podem ser reatribuídos acidentalmente. Além disso, eles fornecem uma maneira eficaz de representar valores discretos e bem definidos em seu código Python.

## Dataclasses

As dataclasses são uma feature introduzida no Python 3.7 que simplifica a criação de classes que são principalmente utilizadas para armazenar dados. Elas são uma maneira conveniente de definir classes que têm atributos, métodos especiais (como `__init__`, `__repr__`, `__eq__`, etc.) automaticamente gerados, sem a necessidade de escrever todo o código manualmente. As dataclasses são especialmente úteis em situações em que você deseja criar objetos simples de maneira eficiente.

Aqui estão os principais aspectos das dataclasses em Python:

1. **Decorador `@dataclass`**: Para criar uma dataclass, você deve decorar uma classe com o decorador `@dataclass`. Isso informa ao Python para gerar automaticamente métodos especiais e outros métodos úteis para a classe.

2. **Inicialização automática**: O decorador `@dataclass` gera automaticamente um método `__init__` para a classe, inicializando os atributos da classe a partir dos argumentos passados para o construtor.

3. **Representação textual (`__repr__`)**: A dataclass também gera automaticamente um método `__repr__` que fornece uma representação textual padrão da instância da classe. Isso é útil para depuração e para exibir o objeto de forma legível.

4. **Comparação (`__eq__`, `__ne__`, `__lt__`, etc.)**: A dataclass gera automaticamente métodos de comparação, como `__eq__` (igualdade) e `__ne__` (diferença), com base nos atributos da classe.

5. **Ordenação**: Se você quiser comparar instâncias da classe e ordená-las, a dataclass pode gerar métodos de comparação, como `__lt__` (menor que), `__le__` (menor ou igual a), `__gt__` (maior que) e `__ge__` (maior ou igual a), com base em um ou mais atributos.

6. **Método `__post_init__`**: Você pode definir um método `__post_init__` personalizado em sua dataclass para executar código adicional após a inicialização dos atributos.

Aqui está um exemplo simples de uma dataclass em Python:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Uso da dataclass
p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1)  # Saída: Point(x=1, y=2)
print(p1 == p2)  # Saída: True
```

Neste exemplo, a dataclass `Point` possui os atributos `x` e `y`, e os métodos especiais, como `__init__`, `__repr__` e `__eq__`, são gerados automaticamente. Isso torna a criação e manipulação de objetos `Point` muito mais simples e concisa.

## __init__ e __pos__init__ em Dataclasses

Na dataclasses do Python, o método `__post_init__` é uma extensão personalizada que você pode definir em sua classe para executar código adicional após a inicialização dos atributos, complementando o método `__init__`. Vamos entender as diferenças entre esses dois métodos:

1. **`__init__`**:
   - O método `__init__` é gerado automaticamente para você quando você utiliza o decorador `@dataclass` em uma classe.
   - Este método é responsável pela inicialização dos atributos da classe a partir dos argumentos passados para o construtor.
   - Ele é chamado automaticamente quando você cria uma instância da classe.
   - Qualquer código de inicialização personalizado que você queira executar deve ser colocado dentro deste método.

2. **`__post_init__`**:
   - O método `__post_init__` é um método personalizado que você pode definir em sua classe dataclass. Ele não é gerado automaticamente.
   - Este método é chamado automaticamente pelo Python após a inicialização dos atributos no método `__init__`.
   - É útil para executar código adicional após a criação da instância, quando todos os atributos já foram inicializados.
   - Você pode usá-lo, por exemplo, para realizar validações ou cálculos que dependem dos valores dos atributos.

Aqui está um exemplo que ilustra como usar `__post_init__` em uma dataclass:

```python
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
    area: int = None

    def __post_init__(self):
        if self.area is None:
            self.area = self.width * self.height

# Uso da dataclass
r = Rectangle(5, 10)
print(r.area)  # Saída: 50

# Outra maneira de usar a dataclass, fornecendo a área explicitamente
r2 = Rectangle(3, 7, 21)
print(r2.area)  # Saída: 21
```

Neste exemplo, a classe `Rectangle` possui três atributos: `width`, `height` e `area`. O cálculo da área é feito automaticamente no método `__post_init__`, caso o valor de `area` não seja fornecido durante a criação da instância.

Em resumo, `__init__` é usado para a inicialização padrão dos atributos, enquanto `__post_init__` é uma maneira de adicionar lógica personalizada após a inicialização padrão dos atributos em uma dataclass.

## Opções em dataclasses

As data classes em Python são uma funcionalidade introduzida na versão 3.7 da linguagem para simplificar a criação de classes que são principalmente usadas para armazenar dados. Elas automatizam a criação de métodos especiais, como `__init__()`, `__repr__()`, `__eq__()`, e `__hash__()`, com base nos campos definidos na classe. Além disso, você pode personalizar ainda mais o comportamento das data classes usando várias opções. Aqui estão algumas das opções que podem ser usadas ao criar data classes em Python:

1. `frozen`:
   Ao definir uma data class como "congelada" (frozen), você torna seus objetos imutáveis, ou seja, seus campos não podem ser modificados após a criação do objeto. Isso é útil para garantir a integridade dos dados e facilitar a comparação de objetos.

   Exemplo:
   ```python
   from dataclasses import dataclass

   @dataclass(frozen=True)
   class Point:
       x: int
       y: int
   ```

2. `init`:
   Você pode desativar a geração automática do método `__init__()` definindo `init=False`. Isso é útil se você deseja fornecer sua própria implementação do método de inicialização.

   Exemplo:
   ```python
   from dataclasses import dataclass

   @dataclass(init=False)
   class Person:
       name: str
       age: int

       def __init__(self, name: str, age: int):
           self.name = name
           self.age = age
   ```

3. `repr`:
   Da mesma forma, você pode desativar a geração automática do método `__repr__()` definindo `repr=False`. Isso permite que você forneça sua própria implementação do método de representação em string.

4. `eq`:
   Você pode desativar a geração automática do método `__eq__()` definindo `eq=False`. Isso permite que você forneça sua própria implementação do método de comparação de igualdade.

5. `order`:
   Ao definir `order=True`, você ativa a geração automática dos métodos `__lt__()`, `__le__()`, `__gt__()`, e `__ge__()`, permitindo que você compare objetos da data class usando operadores de comparação, como `<`, `<=`, `>`, e `>=`.

6. `unsafe_hash`:
   Por padrão, as data classes geram automaticamente um método `__hash__()` seguro, o que é adequado para objetos imutáveis. No entanto, se você quiser desativar a geração automática do método `__hash__()`, pode definir `unsafe_hash=True`.

Essas opções permitem personalizar o comportamento das data classes de acordo com as necessidades específicas do seu programa. Elas fornecem flexibilidade na criação de classes de dados simples e eficazes em Python.

## Valor padrão e field em Dataclasses

Dentro de dataclasses em Python, você pode especificar valores padrão para os atributos de classe usando a opção `default` e personalizar ainda mais os atributos usando o campo `field`. Vamos discutir esses dois conceitos:

1. **Valor Padrão (Default)**:
   - A opção `default` permite que você atribua um valor padrão a um atributo da dataclass, de modo que, se nenhum valor for fornecido durante a criação da instância, o valor padrão será utilizado.
   - Isso é útil quando você deseja fornecer um valor padrão para um atributo, mas ainda deseja permitir que ele seja substituído quando necessário.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int = 0  # Valor padrão de 0 para o atributo y

p1 = Point(1)  # O valor padrão de y (0) será utilizado
print(p1)  # Saída: Point(x=1, y=0)

p2 = Point(2, 3)  # Fornecendo valores para x e y
print(p2)  # Saída: Point(x=2, y=3)
```

2. **Campo (Field)**:
   - O campo `field` permite que você personalize ainda mais os atributos da dataclass, definindo opções específicas para cada atributo.
   - Você pode usar `field` para configurar coisas como o valor padrão, a ordem de impressão, se o atributo deve ser incluído em métodos gerados automaticamente (como `__eq__` e `__repr__`), entre outros.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=30)  # Valor padrão de 30 para age

p1 = Person("Alice")
print(p1)  # Saída: Person(name='Alice', age=30)

p2 = Person("Bob", 25)
print(p2)  # Saída: Person(name='Bob', age=25)
```

No exemplo acima, o atributo `age` tem um valor padrão definido usando `field(default=30)`, e o valor padrão é usado quando nenhum valor é fornecido. Além disso, você pode personalizar outros aspectos do atributo usando `field`, como a ordem em que os atributos são impressos, o que é útil se você quiser controlar a aparência da representação textual da classe.

Em resumo, os valores padrão e o campo `field` são recursos poderosos das dataclasses em Python que permitem personalizar e tornar suas classes de armazenamento de dados mais flexíveis e eficientes.

## namedtuples POO

Em Python, um namedtuple é uma estrutura de dados especial que faz parte do módulo `collections`. Namedtuples são uma forma de criar classes leves e imutáveis para armazenar dados, onde cada campo (ou atributo) tem um nome associado. Eles são úteis quando você precisa criar objetos simples para armazenar um conjunto fixo de valores relacionados, como coordenadas, registros de banco de dados, pontos em um plano cartesiano, etc.

A principal característica de uma namedtuple é que ela combina a conveniência de um dicionário (acesso aos campos por nome) com a eficiência de uma tupla (imutabilidade). Isso significa que você pode acessar os valores dos campos usando seus nomes, mas não pode modificar esses valores após criar uma instância da namedtuple.

Aqui está como você pode criar e usar namedtuples em Python:

```python
from collections import namedtuple

# Definir uma namedtuple chamada 'Ponto' com campos 'x' e 'y'
Ponto = namedtuple('Ponto', ['x', 'y'])

# Criar uma instância de Ponto
p1 = Ponto(1, 2)

# Acessar os campos por nome
print(p1.x)  # Saída: 1
print(p1.y)  # Saída: 2

# Você também pode acessar os campos usando índices, como em tuplas normais
print(p1[0])  # Saída: 1
print(p1[1])  # Saída: 2

# Namedtuples são imutáveis, então isso não funcionará:
# p1.x = 3  # Isso lançaria um erro 'AttributeError'

# Você pode criar novas instâncias de namedtuples com _replace
p2 = p1._replace(x=3)
print(p2)  # Saída: Ponto(x=3, y=2)
```

Namedtuples são frequentemente usadas para criar classes de dados simples e legíveis, especialmente quando você está lidando com estruturas de dados pequenas e imutáveis. Eles fornecem uma maneira conveniente de nomear os campos dos objetos e garantir que esses objetos não sejam modificados acidentalmente.

## Criando sua própria lista com iterable, iterator e sequence (collections.abc)

Para criar sua própria lista com suporte para iteráveis, iteradores e sequências (usando a biblioteca `collections.abc`), você pode criar uma classe personalizada que herda de `collections.abc.MutableSequence`. Isso fornecerá os métodos necessários para sua classe se comportar como uma sequência mutável. Além disso, você precisará implementar os métodos especiais `__getitem__`, `__setitem__`, `__delitem__`, e `__len__` para que sua classe funcione corretamente.

Aqui está um exemplo de como criar uma lista personalizada:

```python
from collections.abc import MutableSequence

class CustomList(MutableSequence):
    def __init__(self, *args):
        self.elements = list(args)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __delitem__(self, index):
        del self.elements[index]

    def __len__(self):
        return len(self.elements)

    def insert(self, index, value):
        self.elements.insert(index, value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __str__(self):
        return str(self.elements)

# Exemplo de uso:
custom_list = CustomList(1, 2, 3, 4)
print(custom_list)  # Saída: [1, 2, 3, 4]

custom_list.append(5)
print(custom_list)  # Saída: [1, 2, 3, 4, 5]

for item in custom_list:
    print(item)  # Saída: 1 2 3 4 5

print(len(custom_list))  # Saída: 5

custom_list[2] = 6
print(custom_list)  # Saída: [1, 2, 6, 4, 5]

del custom_list[1]
print(custom_list)  # Saída: [1, 6, 4, 5]
```

Neste exemplo, a classe `CustomList` herda de `MutableSequence` e implementa todos os métodos necessários para que a lista personalizada se comporte como uma sequência mutável. Você também pode adicionar métodos personalizados conforme necessário para atender aos requisitos específicos da sua lista personalizada.
