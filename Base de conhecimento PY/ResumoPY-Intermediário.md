# Resumo python intermediário

## Funções

As funções em Python são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código em partes menores e mais gerenciáveis, permitindo que você quebre um programa complexo em unidades funcionais independentes. Funções tornam o código mais legível, facilitam a manutenção e promovem a reutilização de código em diferentes partes do programa.

Vamos explorar detalhadamente as características e elementos das funções em Python:

### Definindo uma Função:

Para definir uma função em Python, você usa a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter zero ou mais parâmetros (também chamados de argumentos). Uma função pode ter um corpo, que é um bloco de código indentado que contém as instruções a serem executadas quando a função é chamada.

```python
def nome_da_funcao(parametro1, parametro2, ...):
    # corpo da função
    # instruções a serem executadas
    # pode haver um retorno de valor (opcional)
```

### Parâmetros e Argumentos:

Parâmetros são as variáveis usadas na definição de uma função, enquanto argumentos são os valores passados para a função quando ela é chamada. Os parâmetros permitem que a função aceite dados externos e os utilize em seu corpo para realizar tarefas específicas.

Exemplo de função com parâmetros:

```python
def somar(a, b):
    resultado = a + b
    return resultado
```

Ao chamar essa função, você fornece os argumentos correspondentes aos parâmetros:

```python
resultado = somar(3, 5)
print(resultado)  # Output: 8
```

### Retorno de Valor:

Uma função pode retornar um valor usando a palavra-chave `return`. Isso é útil quando você deseja obter um resultado específico após a execução da função.

Exemplo de função com retorno de valor:

```python
def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado
```

Ao chamar essa função e armazenar seu retorno em uma variável, você obtém o resultado do cálculo:

```python
resultado = calcular_quadrado(4)
print(resultado)  # Output: 16
```

### Funções sem Retorno:

Uma função pode não ter um valor de retorno explícito. Nesse caso, ela retorna `None` por padrão.

Exemplo de função sem retorno:

```python
def saudar(nome):
    print(f"Olá, {nome}!")

resultado = saudar("Alice")
print(resultado)  # Output: Olá, Alice!
                  #         None
```

### Funções com Argumentos Padrão:

Você pode definir argumentos padrão para uma função, tornando-os opcionais ao chamar a função. Se nenhum valor for fornecido para esses argumentos, os valores padrão serão usados.

Exemplo de função com argumento padrão:

```python
def saudar(nome="visitante"):
    print(f"Olá, {nome}!")

saudar()          # Output: Olá, visitante!
saudar("João")     # Output: Olá, João!
```

### Documentação de Funções (Docstrings):

É uma boa prática incluir docstrings em suas funções para descrever o que elas fazem. As docstrings são strings de texto que explicam a finalidade da função e fornecem detalhes sobre seus parâmetros e valor de retorno.

Exemplo de função com docstring:

```python
def calcular_media(valores):
    """
    Calcula a média dos valores em uma lista.

    Parâmetros:
        valores (list): Uma lista de números.

    Retorno:
        float: A média dos valores na lista.
    """
    total = sum(valores)
    media = total / len(valores)
    return media
```

### Lambda (Funções Anônimas):

Python também suporta funções lambda, que são funções anônimas de uma única expressão. Elas são úteis quando você precisa de uma função simples sem a necessidade de definir um nome.

Exemplo de função lambda:

```python
dobro = lambda x: x * 2
print(dobro(5))  # Output: 10
```
A função `key` é um argumento opcional que pode ser fornecido à função `sorted()` em Python (e também à função `sort()` aplicada a listas). Essa função `key` é usada para extrair um valor de cada elemento da lista ou sequência antes que ocorra a comparação e ordenação dos elementos. Em outras palavras, a função `key` define uma base de comparação personalizada para a ordenação dos elementos.

### Função Key

A função `key` espera receber uma função como argumento, geralmente uma função lambda, que será aplicada a cada elemento da lista para extrair o valor relevante usado na comparação. O resultado da aplicação dessa função determina como os elementos serão ordenados.

Vamos dar um exemplo simples:

```python
nomes = ['Ana', 'João', 'Pedro', 'Maria']

# Ordena a lista de nomes alfabeticamente
nomes_ordenados = sorted(nomes)
print(nomes_ordenados)
```

Neste exemplo, os nomes são ordenados alfabeticamente por padrão.

Agora, vamos usar a função `key` para realizar uma ordenação personalizada:

```python
nomes = ['Ana', 'João', 'Pedro', 'Maria']

# Ordena a lista de nomes pelo comprimento de cada nome
nomes_ordenados_por_comprimento = sorted(nomes, key=lambda x: len(x))
print(nomes_ordenados_por_comprimento)
```

Neste segundo exemplo, usamos a função `key` para extrair o comprimento de cada nome (usando a função `len()`) e, em seguida, a lista é ordenada com base nesses valores. Portanto, a saída será: `['Ana', 'João', 'Maria', 'Pedro']`, que é a ordem crescente de acordo com o comprimento dos nomes.

No seu código original, a função `key` é usada nas chamadas a `sorted()` para extrair os valores das chaves `'nome'` e `'sobrenome'` de cada dicionário da lista, e é com base nesses valores que os dicionários são ordenados alfabeticamente.
As funções em Python são um dos conceitos mais poderosos da linguagem, permitindo que você crie blocos de código reutilizáveis e organizados para resolver tarefas específicas. Com funções bem projetadas, você pode criar programas mais modulares, fáceis de manter e extensíveis.
## Escopo Global & Local

Em Python, escopo refere-se à visibilidade e acessibilidade de variáveis em diferentes partes do código. Existem dois tipos principais de escopo em Python: escopo global e escopo local.

### Escopo Global:

Variáveis declaradas fora de qualquer função ou bloco de código têm escopo global. Isso significa que elas podem ser acessadas de qualquer lugar no programa, incluindo dentro de funções. Para criar uma variável global, basta declará-la fora de todas as funções, no nível mais alto do programa.

Exemplo de variável global:

```python
# Variável global
nome = "João"

def saudacao():
    # A variável 'nome' pode ser acessada dentro da função, pois é global
    print(f"Olá, {nome}!")

saudacao()  # Output: Olá, João!
```

As variáveis globais são úteis quando você deseja que uma variável seja compartilhada e acessível em diferentes partes do programa. No entanto, é importante ter cuidado ao modificar variáveis globais dentro de funções, pois isso pode levar a resultados inesperados e dificultar o entendimento do código.

### Escopo Local:

Variáveis declaradas dentro de uma função têm escopo local e são acessíveis apenas dentro dessa função. Elas não podem ser acessadas fora da função em que foram definidas. Isso significa que uma variável local só é válida e acessível dentro do bloco de código da função em que foi definida.

Exemplo de variável local:

```python
def saudacao():
    # Variável local
    nome = "Maria"
    print(f"Olá, {nome}!")

saudacao()  # Output: Olá, Maria!

# Tentar acessar a variável 'nome' fora da função causará um erro:
# print(nome)  # NameError: name 'nome' is not defined
```

As variáveis locais são usadas para armazenar valores temporários dentro de uma função, permitindo que você realize operações com esses valores sem interferir com outras partes do programa.

### Acessando Variáveis Globais Dentro de Funções:

Se você precisar acessar uma variável global dentro de uma função, é possível fazê-lo usando a palavra-chave `global` antes do nome da variável. Isso permite que você modifique a variável global dentro da função.

Exemplo:

```python
contador = 0

def incrementar_contador():
    global contador
    contador += 1

incrementar_contador()
print(contador)  # Output: 1
```

No entanto, é recomendável usar variáveis globais com cautela, pois elas podem tornar o código menos legível e mais difícil de depurar. Em muitos casos, é preferível passar variáveis como argumentos para funções ou retornar valores relevantes em vez de usar variáveis globais.

Em resumo, o escopo global refere-se ao acesso a variáveis em todo o programa, enquanto o escopo local refere-se ao acesso apenas dentro de uma função. O uso adequado de escopos ajuda a manter o código organizado e facilita a manutenção do programa.

## Módulos

Em Python, módulos são arquivos que contêm definições de variáveis, funções e classes que podem ser usadas em outros programas Python. Eles permitem organizar e reutilizar o código de forma eficiente, tornando o desenvolvimento mais fácil e legível. Python possui uma ampla biblioteca padrão com módulos para várias finalidades, como manipulação de strings, acesso ao sistema operacional, gerenciamento de arquivos, entre outros.

Os módulos fornecem um mecanismo para dividir um programa em partes menores e mais gerenciáveis, tornando o código mais modular e facilitando a manutenção. Eles também permitem a criação de bibliotecas personalizadas para que você possa compartilhar seu código com outros desenvolvedores ou reutilizá-lo em vários projetos.

Vamos explorar mais sobre os módulos em Python:

### Importando um Módulo:

Para usar um módulo em um programa Python, você precisa importá-lo. Existem várias maneiras de fazer isso:

1. Importando o módulo inteiro:

```python
import modulo  # onde 'modulo' é o nome do arquivo .py (sem a extensão)
```

Após importar o módulo dessa forma, você pode acessar suas definições usando a sintaxe `modulo.nome_da_definicao`.

2. Importando um módulo com um alias (apelido):

```python
import modulo as md  # 'md' é o alias para o módulo
```

Com um alias, você pode usar o alias para acessar as definições do módulo.

3. Importando apenas definições específicas do módulo:

```python
from modulo import funcao, variavel  # onde 'funcao' e 'variavel' são as definições específicas do módulo que você quer importar
```

Este método permite que você acesse diretamente as definições sem usar o nome do módulo.

### Exemplo de Módulo:

Considere o seguinte exemplo de um módulo chamado `matematica.py`:

```python
# matematica.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
```

Agora, podemos importar e usar esse módulo em outro arquivo Python:

```python
# main.py
import matematica

resultado_soma = matematica.somar(5, 3)
print(resultado_soma)  # Output: 8

resultado_subtracao = matematica.subtrair(10, 4)
print(resultado_subtracao)  # Output: 6
```

### Módulos da Biblioteca Padrão:

Python possui uma rica biblioteca padrão com diversos módulos que abrangem funcionalidades como operações matemáticas, manipulação de strings, acesso ao sistema operacional, trabalho com datas, entre muitos outros. Alguns exemplos de módulos da biblioteca padrão incluem:

- `math`: Fornece funções matemáticas.
- `os`: Permite acessar funcionalidades específicas do sistema operacional.
- `datetime`: Oferece suporte para trabalhar com datas e horários.
- `random`: Permite gerar números aleatórios.
- `json`: Facilita a leitura e gravação de dados no formato JSON.

Esses módulos são amplamente utilizados e podem ser importados em qualquer programa Python sem a necessidade de instalação adicional.

Além da biblioteca padrão, Python também possui uma vasta quantidade de módulos de terceiros disponíveis, que podem ser instalados através do gerenciador de pacotes `pip`. Esses módulos adicionais fornecem recursos adicionais que podem ser incorporados aos seus projetos, expandindo significativamente as capacidades da linguagem Python.

Em resumo, os módulos em Python são uma forma poderosa de organizar, reutilizar e compartilhar código. Eles facilitam a modularização de programas e permitem que você tire proveito da biblioteca padrão e de módulos de terceiros para resolver uma ampla variedade de problemas de programação.

## Empacotamento e Desempacotamento em Funções

O empacotamento (packing) e desempacotamento (unpacking) em funções em Python permitem lidar com um número variável de argumentos de uma maneira mais flexível. Isso significa que você pode criar funções que aceitam um número desconhecido de argumentos ou passar múltiplos argumentos para uma função de forma mais conveniente.

### Empacotamento em Funções:

O empacotamento em funções é feito usando o operador `*` antes de um parâmetro na definição da função. Isso permite que a função aceite um número variável de argumentos, que são empacotados em uma tupla dentro da função.

Exemplo de empacotamento em função:

```python
def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

imprimir_argumentos(1, 2, 3, "Olá", True)
# Output:
# 1
# 2
# 3
# Olá
# True
```

Nesse exemplo, a função `imprimir_argumentos` pode aceitar qualquer número de argumentos, que são empacotados na tupla `args`. Dentro da função, podemos iterar sobre `args` e imprimir cada valor.

### Desempacotamento em Funções:

O desempacotamento em funções é usado quando você tem uma lista, tupla ou outro iterável de valores e deseja passá-los como argumentos para uma função. Isso é feito usando o operador `*` novamente, mas desta vez na chamada da função.

Exemplo de desempacotamento em função:

```python
def soma(a, b, c):
    resultado = a + b + c
    return resultado

valores = [1, 2, 3]
resultado_soma = soma(*valores)
print(resultado_soma)  # Output: 6
```

Neste exemplo, a lista `valores` é desempacotada e seus elementos são passados como argumentos para a função `soma`, que os recebe nas variáveis `a`, `b` e `c`. O resultado é a soma dos valores contidos na lista.

### Empacotamento e Desempacotamento Simultaneamente:

Você também pode empacotar e desempacotar simultaneamente em funções. Por exemplo, você pode criar uma função que recebe alguns argumentos fixos e uma lista de valores adicionais:

```python
def somar_numeros(a, b, *args):
    total = a + b
    for numero in args:
        total += numero
    return total

resultado = somar_numeros(1, 2, 3, 4, 5)
print(resultado)  # Output: 15
```

Neste exemplo, os argumentos `a` e `b` são passados normalmente para a função, e o operador `*args` empacota o restante dos argumentos em uma tupla chamada `args`. A função então soma todos os valores, incluindo os valores empacotados em `args`.

O empacotamento e desempacotamento em funções são técnicas poderosas em Python que oferecem flexibilidade no tratamento de argumentos e permitem que você crie funções mais versáteis e reutilizáveis. Eles são especialmente úteis quando você precisa lidar com um número desconhecido de valores ou quando deseja passar uma lista de valores como argumentos para uma função.

## Uso de args & kwargs em Funções

Em Python, `*args` é uma sintaxe especial usada em funções para permitir que elas aceitem um número variável de argumentos posicionais (não nomeados). O nome `args` é apenas uma convenção, e você pode escolher qualquer outro nome para o parâmetro, mas o asterisco (`*`) é obrigatório. Quando você utiliza `*args` como um parâmetro em uma função, ela pode receber zero ou mais argumentos posicionais, que são agrupados em uma tupla dentro da função.

Aqui está um exemplo simples para ilustrar o uso de `*args` em uma função:

```python
def somar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

# Chamada da função com diferentes quantidades de argumentos
print(somar(1, 2, 3))  # Saída: 6
print(somar(10, 20, 30, 40))  # Saída: 100
print(somar())  # Saída: 0 (sem argumentos, resultando em uma tupla vazia)
```

Observe que, ao usar `*args`, você pode passar qualquer número de argumentos para a função `somar`, e eles serão somados corretamente.

É importante notar que, apesar de `*args` ser útil para lidar com um número variável de argumentos posicionais, ele não permite que você passe argumentos nomeados. Para lidar com argumentos nomeados variáveis, você deve usar `**kwargs`, que é outra sintaxe especial, onde `kwargs` é apenas uma convenção (mas o duplo asterisco é obrigatório).

Aqui está um exemplo que combina `*args` e `**kwargs` em uma função:

```python
def imprimir_argumentos(*args, **kwargs):
    print("Argumentos posicionais (args):", args)
    print("Argumentos nomeados (kwargs):", kwargs)

# Chamada da função com diferentes tipos de argumentos
imprimir_argumentos(1, 2, 3, nome="Alice", idade=30)
# Saída:
# Argumentos posicionais (args): (1, 2, 3)
# Argumentos nomeados (kwargs): {'nome': 'Alice', 'idade': 30}

imprimir_argumentos("hello", True, cor="azul", tamanho="grande")
# Saída:
# Argumentos posicionais (args): ('hello', True)
# Argumentos nomeados (kwargs): {'cor': 'azul', 'tamanho': 'grande'}
```

Assim, `*args` é uma poderosa funcionalidade do Python para criar funções que possam lidar com quantidades variáveis de argumentos posicionais, tornando o código mais flexível e versátil.

## Funções de primeira classe - Higher Order Functions

Em Python, as funções são tratadas como cidadãos de primeira classe (first-class citizens), o que significa que elas podem ser tratadas da mesma forma que qualquer outro objeto no idioma. Especificamente, as funções de primeira classe têm as seguintes características:

1. Atribuição a variáveis: Você pode atribuir uma função a uma variável, assim como faria com um número ou uma string.

2. Passagem como argumento: É possível passar uma função como argumento para outra função. Isso é muito útil para criar funções mais genéricas ou para aplicar funções em coleções de dados.

3. Retorno de funções: As funções podem retornar outras funções como resultado, permitindo a criação de funções aninhadas ou funções de ordem superior (higher-order functions).

4. Armazenamento em estruturas de dados: Você pode armazenar funções em listas, dicionários ou outras estruturas de dados.

Vamos explorar cada uma dessas características com exemplos:

1. Atribuição a variáveis:

```python
def saudacao(nome):
    return f"Olá, {nome}!"

# Atribuição da função a uma variável
cumprimento = saudacao

# Chamada da função através da variável
print(cumprimento("João"))  # Saída: Olá, João!
```

2. Passagem como argumento:

```python
def dobrar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def aplicar_funcao(func, numero):
    return func(numero)

print(aplicar_funcao(dobrar, 5))  # Saída: 10
print(aplicar_funcao(triplicar, 5))  # Saída: 15
```

3. Retorno de funções:

```python
def criar_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

multiplicador_por_5 = criar_multiplicador(5)
print(multiplicador_por_5(3))  # Saída: 15
print(multiplicador_por_5(7))  # Saída: 35
```

4. Armazenamento em estruturas de dados:

```python
def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

funcoes_matematicas = [quadrado, cubo]

print(funcoes_matematicas[0](3))  # Saída: 9 (quadrado de 3)
print(funcoes_matematicas[1](3))  # Saída: 27 (cubo de 3)
```

Essas características tornam as funções de primeira classe uma parte fundamental da programação funcional em Python, permitindo a criação de código mais conciso, flexível e modular.

## Closure

Um closure em Python é uma função que é definida dentro de outra função e captura (ou "fecha") as variáveis locais dessa função exterior, mesmo que essa função exterior já tenha terminado sua execução. Em outras palavras, um closure é uma função que "lembra" o ambiente em que foi criada, permitindo que ela acesse e manipule as variáveis da função externa, mesmo quando essa função externa não está mais em execução.

Aqui está um exemplo simples de closure em Python:

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # Isso imprimirá 15
```

No exemplo acima, a função `inner_function` é um closure, pois ela é definida dentro da função `outer_function` e acessa a variável local `x` da função externa. Mesmo após a execução da função `outer_function`, o closure `inner_function` ainda "lembra" o valor de `x` que foi passado para a função externa. Quando chamamos `closure(5)`, a função interna utiliza o valor de `x` (que é 10) e retorna a soma de `x` e `y`, resultando em 15.

Os closures são frequentemente usados para criar funções auxiliares que compartilham algum estado com a função que as cria. Eles são úteis para encapsular comportamentos e dados relacionados em um escopo limitado, evitando a necessidade de criar variáveis globais.

É importante notar que closures podem ser poderosos, mas também podem levar a bugs sutis se não forem compreendidos e gerenciados corretamente, especialmente em situações onde as variáveis capturadas mudam de valor após a criação do closure.
