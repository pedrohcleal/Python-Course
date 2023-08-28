# Resumo Python part 5

## Variáveis livres + nonlocal (locals, globals)
Em Python, variáveis são utilizadas para armazenar valores que podem ser acessados e manipulados em diferentes partes do código. As variáveis podem ser divididas em diferentes categorias, como variáveis locais, variáveis globais, variáveis de instância, entre outras. Entre essas categorias, existem também as variáveis livres e a palavra-chave `nonlocal` que afetam o escopo das variáveis.

1. **Variáveis Livres:**
Variáveis livres são aquelas que estão definidas em um escopo superior e são acessíveis a partir de um escopo interno. Em outras palavras, são variáveis globais ou pertencentes a um escopo mais amplo que podem ser usadas dentro de uma função, por exemplo, sem a necessidade de serem passadas como argumentos. As variáveis livres são automaticamente capturadas pelo Python quando você as utiliza dentro de uma função. Aqui está um exemplo:

```python
x = 10  # Variável global

def minha_funcao():
    print(x)  # Acessando a variável global 'x'

minha_funcao()  # Saída: 10
```

2. **Palavra-chave `nonlocal`:**
A palavra-chave `nonlocal` é utilizada para indicar que uma variável pertence ao escopo imediatamente superior ao escopo atual da função, mas não é global. Ela é frequentemente usada em funções aninhadas, quando você precisa modificar uma variável em um escopo acima do escopo local da função atual. Isso é especialmente útil quando há uma variável com o mesmo nome em escopos diferentes.

```python
def exterior():
    y = 20  # Variável no escopo de 'exterior'

    def interior():
        nonlocal y
        y += 5  # Modificando a variável 'y' do escopo exterior
        print(y)

    interior()  # Saída: 25

exterior()
```

3. **Funções `locals()` e `globals()`:**
As funções `locals()` e `globals()` permitem acessar os dicionários de variáveis locais e globais, respectivamente. O dicionário retornado por `locals()` contém todas as variáveis no escopo local da função, enquanto o dicionário retornado por `globals()` contém todas as variáveis no escopo global. Isso pode ser útil para inspecionar ou manipular as variáveis em diferentes escopos.

```python
x = 10  # Variável global

def minha_funcao():
    y = 5  # Variável local
    print(locals())  # Mostra as variáveis locais

print(globals())  # Mostra as variáveis globais
minha_funcao()
```

Em resumo, as variáveis livres e a palavra-chave `nonlocal` afetam o escopo das variáveis em Python. Variáveis livres são aquelas definidas em um escopo superior e podem ser acessadas em escopos internos sem serem passadas como argumentos. A palavra-chave `nonlocal` é usada para modificar variáveis de um escopo superior em funções aninhadas. As funções `locals()` e `globals()` permitem acessar as variáveis em escopos locais e globais, respectivamente.

## Funções decoradoras

Em Python, as funções decoradoras são uma característica poderosa que permitem modificar ou aprimorar o comportamento de outras funções ou métodos. Essa abordagem segue o conceito de "metaprogramação", onde você escreve código que manipula código. Isso é especialmente útil para adicionar funcionalidades comuns, como logging, autenticação, medição de desempenho etc., a várias funções sem repetir o mesmo código em cada uma delas.

Vamos entender o conceito de decoradores passo a passo:

1. **Funções de Ordem Superior:** Em Python, as funções são cidadãos de primeira classe, o que significa que elas podem ser tratadas como qualquer outra variável. Isso inclui passá-las como argumentos para outras funções e retorná-las de funções. Esse recurso é a base para a implementação de decoradores.

2. **Sintaxe de Decorador Básica:**
   ```python
   def decorator_function(original_function):
       def wrapper_function(*args, **kwargs):
           # Código a ser executado antes da função original
           result = original_function(*args, **kwargs)
           # Código a ser executado depois da função original
           return result
       return wrapper_function
   ```

   Nesse exemplo, `decorator_function` é um decorador que recebe uma função original como argumento e retorna uma nova função chamada `wrapper_function` que incorpora a funcionalidade extra. A função `wrapper_function` chama a função original e, opcionalmente, executa código antes e depois dela.

3. **Aplicando Decoradores:**
   Você pode aplicar um decorador a uma função usando a sintaxe de "@" antes da definição da função:
   
   ```python
   @decorator_function
   def my_function():
       # Código da função
   ```

4. **Decoradores com Parâmetros:**
   Os decoradores também podem aceitar argumentos. Isso é útil quando você deseja configurar o comportamento do decorador. A estrutura geral é ligeiramente diferente:

   ```python
   def decorator_with_arguments(arg1, arg2):
       def decorator_function(original_function):
           def wrapper_function(*args, **kwargs):
               # Usar arg1, arg2
               result = original_function(*args, **kwargs)
               return result
           return wrapper_function
       return decorator_function
   ```

   Você aplicaria um decorador com argumentos da seguinte maneira:

   ```python
   @decorator_with_arguments(arg1, arg2)
   def my_function():
       # Código da função
   ```

5. **Ordem de Múltiplos Decoradores:**
   É possível aplicar vários decoradores a uma única função. A ordem em que eles são aplicados é importante e segue da parte interna (mais próxima da função original) para a parte externa. Por exemplo:

   ```python
   @decorator1
   @decorator2
   @decorator3
   def my_function():
       # Código da função
   ```

   Nesse caso, `decorator3` será aplicado primeiro, seguido por `decorator2` e, por fim, `decorator1`.

Decoradores são uma ferramenta poderosa para melhorar a modularidade e a reutilização de código em Python. Eles permitem separar as preocupações, mantendo a funcionalidade adicional fora das funções principais e facilitando a manutenção do código.

## zip & zip_longest

A função `zip()` em Python é utilizada para combinar elementos de duas ou mais sequências (listas, tuplas, etc.) em pares ordenados. Ela cria um iterador que gera tuplas contendo um elemento de cada sequência fornecida. Essa função é frequentemente usada quando você deseja percorrer múltiplas sequências ao mesmo tempo e operar em seus elementos correspondentes.

A sintaxe básica da função `zip()` é a seguinte:

```python
zip(iterable1, iterable2, ...)
```

- `iterable1`, `iterable2`, etc.: São as sequências que você deseja combinar. Isso pode incluir listas, tuplas, strings ou qualquer outra sequência iterável.

Aqui está um exemplo de como a função `zip()` funciona:

```python
nomes = ['Alice', 'Bob', 'Carol']
idades = [25, 30, 28]

for nome, idade in zip(nomes, idades):
    print(nome, idade)
```

Neste exemplo, a função `zip()` combina os elementos de `nomes` e `idades` para criar pares ordenados e o loop `for` percorre esses pares, imprimindo o nome e a idade correspondentes.

É importante notar que se as sequências fornecidas para a função `zip()` tiverem tamanhos diferentes, o iterador gerado será interrompido quando a sequência mais curta for completamente percorrida. Isso significa que os elementos excedentes da sequência mais longa não serão considerados.

Além disso, você pode desempacotar as tuplas geradas pelo `zip()` para obter os elementos individuais:

```python
pares = zip(nomes, idades)
for par in pares:
    nome, idade = par
    print(nome, idade)
```

Ou ainda, usar a desempacotamento direto no loop:

```python
pares = zip(nomes, idades)
for nome, idade in pares:
    print(nome, idade)
```

A função `zip()` é uma ferramenta útil para combinar informações de diferentes fontes de dados e é amplamente usada em Python para simplificar o processamento paralelo de dados.

### zip_longest

O módulo `itertools` em Python oferece uma função chamada `zip_longest()` que é semelhante à função `zip()`, mas lida de maneira mais flexível com sequências de tamanhos diferentes. Além disso, `zip_longest()` permite definir um valor de preenchimento (`fillvalue`) para ser usado quando uma sequência é mais curta do que outras durante a combinação. Essa função é útil quando você deseja garantir que todos os elementos de todas as sequências sejam considerados, preenchendo os espaços vazios com um valor específico.

Aqui está a sintaxe da função `zip_longest()` com o uso do argumento `fillvalue`:

```python
itertools.zip_longest(iterable1, iterable2, ..., fillvalue=None)
```

- `iterable1`, `iterable2`, etc.: As sequências que você deseja combinar.
- `fillvalue`: O valor a ser usado como preenchimento para as sequências mais curtas. O valor padrão é `None`.

Aqui está um exemplo de uso da função `zip_longest()` com o argumento `fillvalue`:

```python
from itertools import zip_longest

nomes = ['Alice', 'Bob', 'Carol']
idades = [25, 30]

for nome, idade in zip_longest(nomes, idades, fillvalue='Desconhecido'):
    print(nome, idade)
```

Neste exemplo, a saída será:

```
Alice 25
Bob 30
Carol Desconhecido
```

## Função Count - itertools

A função `count` da biblioteca `itertools` em Python gera um iterador que produz uma sequência infinita de valores inteiros começando a partir de um valor inicial (padrão é 0) e incrementando em um passo (padrão é 1). Como a sequência é infinita, é necessário limitar o uso dessa função com alguma condição de parada, caso contrário, ela continuará gerando valores indefinidamente.

Aqui está a assinatura básica da função `count`:

```python
itertools.count(start=0, step=1)
```

Parâmetros:
- `start`: Valor inicial da contagem. O padrão é 0.
- `step`: Valor a ser adicionado a cada iteração. O padrão é 1.

Essa função é geralmente usada em combinação com outras funções e ferramentas de programação funcional para criar sequências personalizadas. Por exemplo, você pode usar `count` em conjunto com a função `islice` para criar uma sequência finita de valores, definindo um limite para a contagem.

Aqui está um exemplo de como você poderia usar a função `count`:

```python
import itertools

# Criar um iterador de contagem começando em 5 e incrementando de 2 em 2
contador = itertools.count(start=5, step=2)

# Imprimir os próximos 5 valores da contagem
for _ in range(5):
    print(next(contador))
```

Saída:

```
5
7
9
11
13
```

Neste exemplo, o iterador `contador` gera uma sequência de números ímpares a partir do valor inicial 5, incrementando de 2 em 2. O loop `for` imprime os próximos 5 valores dessa contagem.

Lembre-se de que, como a função `count` gera uma sequência infinita, é importante ter cuidado ao usá-la para evitar loops infinitos e consumir muita memória ou recursos do sistema.

Observe que a sequência `idades` é mais curta do que a sequência `nomes`, mas a função `zip_longest()` preencheu o valor ausente com "Desconhecido".

O uso do `fillvalue` é especialmente útil quando você está lidando com dados tabulares ou estruturas em que é importante manter uma estrutura uniforme, mesmo que algumas informações estejam faltando em certos pontos.

### Qual a diferença entre um objeto iterável e iterador

Em Python, tanto os objetos iteráveis quanto os iteradores estão relacionados à iteração sobre elementos em uma sequência, mas eles têm propósitos e comportamentos ligeiramente diferentes.

1. **Objeto Iterável:**
Um objeto iterável é qualquer objeto que pode ser percorrido ou iterado, ou seja, você pode usar um loop (como `for`) para percorrer seus elementos. Os objetos iteráveis podem ser coleções de elementos, como listas, tuplas, conjuntos e dicionários, mas também podem ser sequências geradas sob demanda, como geradores. Um objeto iterável deve implementar o método especial `__iter__()` que retorna um iterador.

Exemplo de um objeto iterável (lista):

```python
my_list = [1, 2, 3, 4, 5]
```

2. **Iterador:**
Um iterador é um objeto que mantém um estado de iteração e fornece um método `__next__()` para obter o próximo elemento da sequência. Um iterador mantém informações sobre o estado atual da iteração, o que permite retomar de onde parou na próxima chamada do método `__next__()`. Iteradores são frequentemente criados a partir de objetos iteráveis usando o método `iter()`.

Exemplo de um iterador (usando a função `iter()` para criar um iterador a partir da lista anterior):

```python
my_iterator = iter(my_list)
```

Em resumo:
- Um objeto iterável é algo que pode ser percorrido.
- Um iterador é um objeto que mantém o controle do estado de iteração e fornece os próximos elementos.

Um detalhe importante é que, em geral, um objeto iterável pode ser transformado em um iterador usando a função `iter()`. Isso acontece quando você percorre um objeto iterável usando um loop `for`, por exemplo. O loop cria automaticamente um iterador temporário a partir do objeto iterável para realizar a iteração. Portanto, enquanto os iteradores são usados principalmente para iteração controlada e manutenção de estado, os objetos iteráveis são mais comuns na programação cotidiana.

##  Combinations, Permutations e Product da biblioteca Itertools

A biblioteca `itertools` em Python é uma poderosa ferramenta para trabalhar com iterações e permutações de elementos. Ela fornece várias funções que facilitam a geração de combinações, permutações e produtos de sequências. Vamos dar uma olhada nas três funções específicas que você mencionou: `combinations`, `permutations` e `product`.

1. **Combinations:**
A função `combinations` gera todas as combinações possíveis de tamanho específico a partir de uma sequência dada, sem repetir elementos. Ela retorna um objeto iterável que pode ser transformado em uma lista, se necessário.

Exemplo:
```python
from itertools import combinations

seq = [1, 2, 3]
comb = combinations(seq, 2)

for c in comb:
    print(c)
```
Saída:
```
(1, 2)
(1, 3)
(2, 3)
```

2. **Permutations:**
A função `permutations` gera todas as permutações possíveis de uma sequência, com um tamanho específico ou igual ao tamanho da sequência. Ela também retorna um objeto iterável.

Exemplo:
```python
from itertools import permutations

seq = [1, 2, 3]
perm = permutations(seq, 2)

for p in perm:
    print(p)
```
Saída:
```
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```

3. **Product:**
A função `product` calcula o produto cartesiano de duas ou mais sequências, gerando todas as combinações possíveis dos elementos entre as sequências fornecidas. Ela também retorna um objeto iterável.

Exemplo:
```python
from itertools import product

seq1 = [1, 2]
seq2 = ['a', 'b']
prod = product(seq1, seq2)

for p in prod:
    print(p)
```
Saída:
```
(1, 'a')
(1, 'b')
(2, 'a')
(2, 'b')
```

Essas funções da biblioteca `itertools` são extremamente úteis para gerar combinações, permutações e produtos de maneira eficiente, especialmente quando lidando com grandes conjuntos de dados. Elas facilitam tarefas como a geração de todas as possíveis combinações para resolver problemas de otimização, a criação de testes abrangentes ou a exploração de cenários variados.

### groupby -itertools
A função `groupby` da biblioteca `itertools` em Python é usada para agrupar elementos consecutivos em uma sequência com base em uma função de chave. Ela retorna um iterador que gera pares contendo a chave e um iterador de elementos que têm a mesma chave. Isso é particularmente útil quando você deseja agrupar elementos semelhantes em uma sequência com base em algum critério.

Aqui está a assinatura da função `groupby`:

```python
itertools.groupby(iterable, key=None)
```

- `iterable`: A sequência de entrada que você deseja agrupar.
- `key`: Uma função opcional que define a chave de agrupamento para cada elemento. Se não for fornecida, os elementos serão agrupados com base na igualdade direta.

A função `groupby` agrupa elementos consecutivos na sequência com base na chave especificada. Ela retorna um iterador onde cada elemento é um par contendo a chave e um iterador dos elementos correspondentes a essa chave.

Exemplo de uso:

```python
from itertools import groupby

data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5)]

# Agrupa os elementos com base na chave (primeiro elemento da tupla)
grouped_data = groupby(data, key=lambda x: x[0])

for key, group in grouped_data:
    print(key, list(group))
```

Saída:
```
a [('a', 1), ('a', 2)]
b [('b', 3), ('b', 4)]
c [('c', 5)]
```

Neste exemplo, a função `groupby` agrupa os elementos da lista `data` com base no primeiro elemento de cada tupla. Isso resulta em três grupos: 'a', 'b' e 'c'. Cada grupo é um iterador que contém os elementos correspondentes a essa chave.

Lembre-se de que a sequência de entrada deve estar ordenada pela chave de agrupamento para que o `groupby` funcione corretamente, já que ele agrupa elementos consecutivos com chaves iguais.

##Conceitos relacionados a iteração e sequências em Python.

### 1. Map
`map()` é uma função integrada em Python que permite aplicar uma determinada função a cada elemento de um ou mais iteráveis, como listas, tuplas, etc. Ela retorna um objeto do tipo `map` que pode ser convertido em uma lista ou outro tipo de iterável. A sintaxe básica é a seguinte:

```python
map(função, iterável)
```

Por exemplo, se você quiser dobrar todos os números em uma lista, pode usar o `map` da seguinte forma:

```python
def dobrar(numero):
    return numero * 2

numeros = [1, 2, 3, 4]
dobrados = map(dobrar, numeros)
dobrados_lista = list(dobrados)  # Convertendo para lista
print(dobrados_lista)  # Saída: [2, 4, 6, 8]
```

### 2. Partial
`functools.partial` é uma função que permite fixar um ou mais argumentos de uma função, produzindo uma nova função com esses argumentos já predefinidos. Isso é útil quando você quer criar uma versão especializada de uma função com alguns parâmetros fixos.

```python
from functools import partial

def potencia(base, expoente):
    return base ** expoente

quadrado = partial(potencia, expoente=2)
cubo = partial(potencia, expoente=3)

print(quadrado(4))  # Saída: 16
print(cubo(3))       # Saída: 27
```

### 3. GeneratorType
`GeneratorType` não é algo que você normalmente interage diretamente em código Python. Ele se refere ao tipo de objeto retornado por geradores (generators). Os geradores são uma forma eficiente de criar iteráveis, permitindo a geração de valores sob demanda, economizando memória.

Um gerador é criado usando uma função comum, mas em vez de usar `return`, você usa a palavra-chave `yield`. Cada vez que o gerador é iterado, ele executa até encontrar uma instrução `yield`, retorna o valor especificado e pausa a execução da função até a próxima iteração.

```python
def contagem_regressiva(n):
    while n > 0:
        yield n
        n -= 1

contador = contagem_regressiva(5)
for numero in contador:
    print(numero)  # Produzirá os números de 5 a 1
```

### 4. Esgotamento de Iterators
Um esgotamento de iterador ocorre quando você itera por todos os elementos de um iterável e chega ao seu fim. Depois que um iterador é esgotado, ele não pode ser percorrido novamente. Isso é especialmente relevante quando se trabalha com geradores.

```python
def gerador_simples():
    yield 1
    yield 2
    yield 3

gen = gerador_simples()
for valor in gen:
    print(valor)

# Se você tentar iterar novamente, nada será impresso, pois o gerador foi esgotado.
for valor in gen:
    print(valor)  # Nenhum valor será impresso, pois o gerador já foi esgotado
```

Lembre-se de que geradores são eficientes quando se trata de memória, mas uma vez que eles são esgotados, você precisa criar uma nova instância do gerador para iterar novamente.
