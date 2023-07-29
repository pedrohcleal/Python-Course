# Resumo python intermediário

## Funções

Em Python, uma função é um bloco de código nomeado que realiza uma tarefa específica e pode ser reutilizado várias vezes ao longo do programa. Ela ajuda a organizar o código, tornando-o mais legível e modular. Para definir uma função em Python, você usa a palavra-chave `def`, seguida pelo nome da função, parênteses que podem conter argumentos (ou parâmetros) e, opcionalmente, uma sequência de instruções que constituem o corpo da função.

Aqui está a sintaxe geral de como uma função é definida em Python:

```python
def nome_da_funcao(parametro1, parametro2, ...):
    # corpo da função
    # instruções a serem executadas
    # pode haver um retorno de valor (opcional)
```

Vamos criar um exemplo simples de uma função para calcular o quadrado de um número:

```python
def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado
```

Neste exemplo, a função `calcular_quadrado` recebe um argumento chamado `numero`. Em seguida, o código dentro da função calcula o quadrado desse número utilizando o operador de exponenciação `**` e armazena o resultado na variável `quadrado`. Finalmente, a função retorna o valor do quadrado usando a palavra-chave `return`.

Para chamar (ou invocar) essa função, você pode simplesmente usar seu nome e passar um argumento para ela:

```python
resultado = calcular_quadrado(5)
print(resultado)  # Output: 25
```

Além disso, funções podem ter vários parâmetros e podem não retornar nada (ou seja, podem ter um retorno vazio). Veja um exemplo de uma função que soma dois números e não retorna nenhum valor:

```python
def somar(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}")

somar(3, 7)  # Output: A soma de 3 e 7 é 10
```

As funções são fundamentais na programação, pois permitem a reutilização do código e a separação de tarefas complexas em partes menores e mais gerenciáveis. Elas também ajudam a tornar o código mais legível e facilitam a manutenção do programa. Python possui diversas funções embutidas (built-in) e permite que você defina suas próprias funções para personalizar e estender a funcionalidade da linguagem de acordo com suas necessidades.

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
