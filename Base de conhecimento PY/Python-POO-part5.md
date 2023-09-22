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
