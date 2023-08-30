# Part 7

## Problemas dos parametros mutáveis em funções

Em Python, os parâmetros mutáveis em funções podem levar a comportamentos inesperados e erros difíceis de depurar. Os problemas decorrem da natureza mutável desses parâmetros, como listas ou dicionários, que podem ser alterados dentro da função sem que a chamada original perceba essas mudanças. Aqui estão alguns dos principais problemas associados aos parâmetros mutáveis em funções:

1. **Efeitos colaterais não intencionais**: Se a função modificar um parâmetro mutável, essa modificação afetará a variável original fora da função. Isso pode levar a resultados inesperados e dificultar a rastreabilidade das mudanças.

2. **Dificuldade de rastreamento**: Quando uma função altera um parâmetro mutável, pode ser difícil rastrear onde exatamente essa alteração ocorreu, especialmente em programas grandes. Isso pode complicar a depuração e manutenção do código.

3. **Compartilhamento de estado**: Se vários trechos de código compartilham uma referência a um objeto mutável, as alterações feitas em um local podem afetar imprevistamente outros trechos do código que também utilizam esse objeto.

4. **Inconsistência de estado**: Uma função pode alterar o estado de um objeto mutável de tal maneira que não esteja mais em um estado válido. Isso pode levar a erros difíceis de entender, pois o estado inválido pode não ser imediatamente visível.

5. **Compartilhamento de dados não intencional**: Quando objetos mutáveis são passados como parâmetros, pode ocorrer o compartilhamento de dados entre diferentes partes do código, o que pode levar a modificações indesejadas.

6. **Quebra do princípio da imutabilidade**: A imutabilidade é uma característica importante em programação funcional e ajuda a evitar efeitos colaterais. Parâmetros mutáveis podem quebrar essa abordagem, tornando mais difícil escrever código previsível e de fácil manutenção.

Para mitigar esses problemas, considere seguir as boas práticas ao lidar com parâmetros mutáveis:

- **Evite alterar parâmetros mutáveis diretamente**: Se possível, crie cópias dos objetos mutáveis para trabalhar com eles dentro da função, em vez de modificar o original.

- **Documente as modificações**: Se uma função modifica um parâmetro mutável, deixe isso claro na documentação da função para alertar os usuários sobre possíveis efeitos colaterais.

- **Use objetos imutáveis sempre que possível**: Quando você não precisa da mutabilidade, use objetos imutáveis, como tuplas e strings, para evitar problemas relacionados a parâmetros mutáveis.

- **Retorne novos objetos**: Se uma função precisa modificar um objeto mutável, em vez de alterá-lo in-place, retorne um novo objeto com as modificações aplicadas. Isso ajuda a evitar efeitos colaterais.

- **Use técnicas de programação funcional**: Técnicas da programação funcional, como evitar o uso de variáveis globais e minimizar o compartilhamento de estado, podem ajudar a reduzir os problemas associados aos parâmetros mutáveis.

Em resumo, enquanto o Python permite o uso de parâmetros mutáveis em funções, é importante estar ciente dos problemas potenciais e adotar abordagens para minimizar os riscos associados a esses parâmetros.

## Guard Clause em Py
Uma "Guard Clause" (também conhecida como "Early Return" ou "Bouncer Pattern") é um padrão de programação utilizado para melhorar a legibilidade e a manutenção do código, evitando aninhar uma lógica complexa dentro de uma estrutura de controle condicional (como um `if`) e, em vez disso, tratando as condições de erro ou casos especiais primeiro. Isso resulta em um código mais limpo, fácil de entender e com menos indentação.

No contexto de Python, uma Guard Clause é frequentemente implementada usando uma instrução `return` ou `raise` para sair da função ou método assim que uma condição for atendida. Isso ajuda a evitar o aninhamento excessivo de blocos de código e melhora a legibilidade do programa.

Aqui está um exemplo simples de uma função que calcula a divisão de dois números usando uma Guard Clause:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")  # Guard Clause
    return a / b
```

Nesse exemplo, a Guard Clause verifica se o denominador (`b`) é igual a zero. Se for, a função levanta um erro com uma mensagem apropriada. Caso contrário, a divisão é realizada e o resultado é retornado. Essa abordagem evita a necessidade de indentar todo o código da função dentro do bloco `if`, o que tornaria o código mais difícil de ler à medida que a lógica se torna mais complexa.

Aqui está outro exemplo mais detalhado, ilustrando como uma Guard Clause pode melhorar a legibilidade do código:

```python
def calculate_grade(score):
    if score < 0:
        return "Invalid score"  # Guard Clause
    if score < 50:
        return "F"
    elif score < 70:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"
```

Neste exemplo, a primeira Guard Clause lida com o caso em que o valor do `score` é inválido. Se o valor for negativo, a função retorna imediatamente com uma mensagem de erro. Isso evita a necessidade de aninhar o restante da lógica dentro de um bloco `if`.

Em resumo, as Guard Clauses em Python são uma técnica que visa tornar o código mais legível e menos aninhado, tratando condições de erro ou casos especiais no início de uma função ou método antes de prosseguir com a lógica principal. Isso contribui para um código mais claro, mais organizado e mais fácil de manter.

## Controlando a quantidade de argumentos posicionais e nomeados em funções

Em Python, a capacidade de controlar a quantidade e o tipo de argumentos passados para uma função é fundamental para escrever código flexível e legível. Você pode usar diferentes técnicas para controlar os argumentos em funções, incluindo a definição de parâmetros posicionais somente ("/"), argumentos somente por palavra-chave e padrões padrão. Vou explicar como usar essas técnicas.

### Parâmetros Posicionais Somente ("/"):

O caractere "/" é usado para indicar que todos os parâmetros antes dele na lista de parâmetros de uma função devem ser passados por posição, sem a possibilidade de usar palavras-chave. Isso ajuda a criar uma separação clara entre os argumentos posicionais e os argumentos que devem ser passados por palavra-chave. Veja um exemplo:

```python
def positional_only_example(a, b, /):
    return a + b

result = positional_only_example(3, 5)  # Válido, pois passamos a e b por posição
# result = positional_only_example(a=3, b=5)  # Inválido, pois não podemos usar palavras-chave
```

### Argumentos Somente por Palavra-chave:

Você também pode definir argumentos que só podem ser passados por palavra-chave, o que significa que eles não podem ser passados por posição. Isso é útil quando você tem argumentos opcionais que podem não estar na ordem certa. Você define essa restrição usando o caractere "*" antes deles. Veja um exemplo:

```python
def keyword_only_example(*, x, y):
    return x * y

# result = keyword_only_example(2, 3)  # Inválido, pois os argumentos são apenas por palavra-chave
result = keyword_only_example(x=2, y=3)  # Válido, passando os argumentos corretamente
```

### Parâmetros Padrão:

Parâmetros padrão permitem que você defina valores predefinidos para os argumentos de uma função. Isso é útil quando você deseja que um argumento seja opcional. No entanto, você precisa garantir que os parâmetros com valores padrão estejam após todos os parâmetros posicionais (antes do "/") ou após o caractere "*" (para argumentos somente por palavra-chave). Exemplo:

```python
def default_arguments_example(a, b, c=0):
    return a + b + c

result1 = default_arguments_example(1, 2)  # c assume o valor padrão 0
result2 = default_arguments_example(1, 2, 3)  # c assume o valor 3 passado explicitamente
```

Combinar essas técnicas permite que você controle cuidadosamente como os argumentos são passados para suas funções, criando um código mais legível e claro, além de prevenir erros comuns de passagem de argumentos. Certifique-se de compreender bem as regras de sintaxe para cada caso antes de aplicá-las em seu código.
