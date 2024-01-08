# Python Intermediário part 6

## Método `reverse`  e função `reversed()`:

Em Python, o método `reverse()` e a função `reversed()` são utilizados para inverter a ordem dos elementos em uma lista. No entanto, eles têm algumas diferenças importantes em termos de como são aplicados.

### Método `reverse()`:

O método `reverse()` é um método das listas em Python. Ele inverte a ordem dos elementos da lista in-place, ou seja, a própria lista é modificada e nenhum novo objeto é criado. A sintaxe básica é a seguinte:

```python
lista.reverse()
```

Exemplo:

```python
frutas = ['maçã', 'banana', 'laranja']
frutas.reverse()
print(frutas)
```

Saída:

```
['laranja', 'banana', 'maçã']
```

### Função `reversed()`:

A função `reversed()` é uma função embutida que retorna um objeto iterável reverso. Essa função não modifica a lista original; ela cria e retorna um novo objeto iterável reverso. Se você quiser uma lista invertida, pode convertê-la novamente em uma lista usando a função `list()`. A sintaxe básica é a seguinte:

```python
reversed_lista = reversed(iterável)
```

Exemplo:

```python
frutas = ['maçã', 'banana', 'laranja']
frutas_invertidas = list(reversed(frutas))
print(frutas_invertidas)
```

Saída:

```
['laranja', 'banana', 'maçã']
```

Portanto, enquanto o método `reverse()` modifica a lista original, a função `reversed()` cria um novo objeto iterável reverso sem modificar a lista original. A escolha entre eles depende dos requisitos específicos do seu código.


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

## DocStrings

Em Python, uma docstring é uma string de documentação associada a um módulo, função, classe ou método. Ela é usada para descrever o propósito e a funcionalidade do código para ajudar os desenvolvedores a entender como usar e interagir com o código. Docstrings são usadas para documentação interna e podem ser acessadas por meio de várias ferramentas de documentação e IDEs para fornecer informações úteis aos desenvolvedores.

Existem três tipos principais de docstrings em Python:

1. **Docstrings de Módulo**:
   Estas docstrings são usadas para documentar o módulo como um todo. Normalmente, são colocadas no início do arquivo do módulo. Um exemplo de docstring de módulo:

   ```python
   """
   Este é um exemplo de docstring de módulo.
   Ele fornece informações sobre o que este módulo faz.
   """
   ```

2. **Docstrings de Função/Método**:
   Docstrings de função ou método são usadas para documentar uma função ou método específico. Elas são colocadas logo após a definição da função ou método. Aqui está um exemplo:

   ```python
   def calcular_soma(a, b):
       """
       Esta função calcula a soma de dois números.
       
       :param a: O primeiro número.
       :param b: O segundo número.
       :return: A soma de a e b.
       """
       return a + b
   ```

3. **Docstrings de Classe**:
   Docstrings de classe são usadas para documentar uma classe e seus atributos. Elas são colocadas logo após a definição da classe. Aqui está um exemplo:

   ```python
   class Pessoa:
       """
       Esta classe representa uma pessoa com atributos como nome e idade.
       """
       def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade
   ```

As docstrings podem ser acessadas em tempo de execução usando o atributo `__doc__` do objeto, como no seguinte exemplo:

```python
print(calcular_soma.__doc__)  # Exibe a docstring da função calcular_soma
```

Além de servir como documentação legível para humanos, docstrings também podem ser processadas por ferramentas de documentação, como o Sphinx, que permite gerar documentação automática a partir do código-fonte. Portanto, é uma boa prática escrever docstrings claras e informativas para facilitar a compreensão e o uso do seu código Python.

## Type Annotations

Type annotations, em português "anotações de tipo", são uma característica do Python 3 que permite aos desenvolvedores especificar os tipos de variáveis, argumentos de função e valores de retorno de funções, métodos e classes. Embora o Python seja uma linguagem de programação dinamicamente tipada, o uso de type annotations ajuda a tornar o código mais legível, auto-documentado e pode ser útil para detectar erros de tipo durante a análise estática do código.

A sintaxe básica para type annotations envolve o uso do operador de dois pontos (`:`) após o nome da variável, argumento ou valor de retorno, seguido pelo tipo desejado. Aqui estão alguns exemplos:

1. **Anotações de variáveis**:
   
   ```python
   nome: str = "Alice"
   idade: int = 30
   preco: float = 19.99
   ```

2. **Anotações de argumentos de função**:

   ```python
   def calcular_soma(a: int, b: int) -> int:
       return a + b
   ```

3. **Anotações de valores de retorno de função**:

   ```python
   def dividir(a: float, b: float) -> float:
       return a / b
   ```

É importante observar que as anotações de tipo são opcionais e não afetam o comportamento em tempo de execução do código Python. No entanto, elas podem ser usadas por ferramentas e IDEs para fornecer recursos adicionais, como:

- **Deteção de erros de tipo**: Algumas ferramentas de análise estática, como o `mypy`, podem verificar se o código está em conformidade com as anotações de tipo e relatar erros de tipo em tempo de desenvolvimento.

- **Melhor legibilidade e documentação**: As anotações de tipo tornam o código mais fácil de entender e documentam as expectativas de tipo, tornando-o mais auto-explicativo para outros desenvolvedores que possam ler o código.

- **Melhores sugestões de autocompletar**: IDEs, como o Visual Studio Code, podem usar anotações de tipo para fornecer sugestões mais precisas durante a digitação do código.

- **Facilitação da manutenção do código**: As anotações de tipo ajudam a evitar que você mesmo ou outros desenvolvedores cometam erros de tipo ao trabalhar com o código.

- **Documentação automática**: Ferramentas de documentação, como o Sphinx, podem usar anotações de tipo para gerar documentação automática mais detalhada.

É importante observar que as anotações de tipo são uma adição opcional ao Python, e o interpretador Python não faz verificações de tipo em tempo de execução com base nessas anotações. Portanto, a responsabilidade de garantir a conformidade com os tipos especificados recai sobre o desenvolvedor e as ferramentas de análise estática que podem ser usadas durante o desenvolvimento.

## Type hints

Type hints são uma forma de indicar ao interpretador Python o tipo de dados esperado para variáveis, argumentos de função e valores de retorno. Embora Python seja uma linguagem de tipagem dinâmica, ou seja, os tipos são atribuídos em tempo de execução, as type hints fornecem uma maneira de adicionar informações de tipo opcional ao código fonte.

O módulo `typing` introduziu uma série de tipos que podem ser usados para fornecer hints sobre os tipos. Alguns exemplos incluem:

1. **Tipos Básicos:**
   - `int`
   - `float`
   - `str`
   - `bool`

2. **Contêineres Genéricos:**
   - `List[T]`: Lista de elementos do tipo `T`.
   - `Tuple[T1, T2, ...]`: Tupla com elementos dos tipos especificados.
   - `Dict[K, V]`: Dicionário com chaves do tipo `K` e valores do tipo `V`.

3. **Tipos Especiais:**
   - `Any`: Qualquer tipo.
   - `Union[T1, T2, ...]`: Pode ser de qualquer tipo especificado na união.

4. **Tipos de Função:**
   - `Callable[..., ReturnType]`: Representa uma função que pode ser chamada com argumentos do tipo `...` e retorna `ReturnType`.
   - `Optional[T]`: Indica que um valor pode ser do tipo `T` ou `None`.

Ao usar type hints, os desenvolvedores podem tornar o código mais legível e facilitar a manutenção. Além disso, ferramentas externas, como o linter `mypy`, podem verificar o código em busca de inconsistências de tipos antes mesmo de ser executado.

Exemplo de uso de type hints:

```python
def calcular_area(base: float, altura: float) -> float:
    return base * altura

# Uso de type hints em uma lista
def dobrar_elementos(valores: List[int]) -> List[int]:
    return [valor * 2 for valor in valores]
```

Esses hints são opcionais e não afetam o comportamento do código em tempo de execução, mas são valiosos para a legibilidade e manutenção do código, especialmente em projetos grandes e colaborativos.

### MyPy
O `mypy` é um verificador de tipos estático para Python que utiliza type hints para analisar e validar o código em busca de erros relacionados a tipos. Ele é uma ferramenta de análise estática que permite aos desenvolvedores detectar possíveis problemas de tipos antes mesmo de executar o código.

Principais características do `mypy`:

1. **Análise Estática:**
   - O `mypy` analisa o código fonte sem a necessidade de executá-lo. Ele verifica se as type hints estão sendo seguidas corretamente e se não há inconsistências de tipos.

2. **Suporte a Type Hints:**
   - O `mypy` é projetado para trabalhar em conjunto com type hints, que são uma adição ao Python 3.5 e posterior. Ele faz uso dessas dicas de tipo para verificar a consistência do código.

3. **Integração com Editores de Código:**
   - Muitos editores de código, como Visual Studio Code, PyCharm e outros, oferecem integração direta com o `mypy`. Isso permite que os desenvolvedores vejam os erros de tipo enquanto estão escrevendo o código.

4. **Personalização:**
   - O `mypy` oferece opções de configuração que permitem aos desenvolvedores ajustar as verificações de tipos de acordo com as necessidades do projeto.

5. **Suporte a Tipos Avançados:**
   - Além dos tipos básicos, o `mypy` suporta tipos mais avançados, como tipos genéricos, tipos de função e muito mais.

Para utilizar o `mypy`, primeiro, é necessário instalá-lo através do pip:

```bash
pip install mypy
```

Em seguida, é possível executar o `mypy` no código Python, fornecendo o caminho para o arquivo ou diretório que deseja verificar:

```bash
mypy seu_codigo.py
```

O `mypy` gerará mensagens de erro se encontrar problemas relacionados a tipos. Isso pode incluir variáveis com tipos incompatíveis, uso incorreto de funções, entre outros.

O uso do `mypy` é especialmente útil em projetos grandes e complexos, onde a detecção precoce de erros de tipos pode economizar tempo e facilitar a manutenção do código.
