# Resumo Python part 4

## Método isinstace()

Em Python, o método `isinstance()` é usado para verificar se um objeto pertence a uma determinada classe ou a uma tupla de classes. Ele retorna `True` se o objeto for uma instância de qualquer uma das classes fornecidas e `False` caso contrário.

A sintaxe geral do método `isinstance()` é a seguinte:

```python
isinstance(objeto, classe_ou_tupla_de_classes)
```

- `objeto`: O objeto que você deseja verificar.
- `classe_ou_tupla_de_classes`: Pode ser uma classe única ou uma tupla de classes. Se o objeto for uma instância de qualquer uma das classes fornecidas, o método retornará `True`.

Aqui estão alguns exemplos de uso do método `isinstance()`:

```python
# Verificando se um número é do tipo int
num = 10
resultado = isinstance(num, int)
print(resultado)  # Saída: True

# Verificando se uma string é do tipo str ou int
texto = "Olá, mundo!"
resultado = isinstance(texto, (str, int))
print(resultado)  # Saída: True

# Verificando se um objeto é uma instância de uma classe específica
class Pessoa:
    pass

pessoa = Pessoa()
resultado = isinstance(pessoa, Pessoa)
print(resultado)  # Saída: True

# Verificando se um objeto é uma instância de uma das classes em uma tupla
class Animal:
    pass

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

animal = Cachorro()
resultado = isinstance(animal, (Cachorro, Gato))
print(resultado)  # Saída: True
```

O método `isinstance()` é útil quando você deseja verificar o tipo de um objeto de forma dinâmica e tomar decisões com base nessa verificação. Isso é particularmente útil em situações em que você está lidando com herança de classes e polimorfismo.

## Truthy & False

Em Python, os termos "Truthy" e "Falsy" referem-se a valores booleanos implícitos que são usados ​​em contextos de avaliação de expressões condicionais. Valores "Truthy" são aqueles que são considerados verdadeiros em avaliações booleanas, enquanto valores "Falsy" são aqueles que são considerados falsos.

Os seguintes valores são considerados "Falsy" em Python:

1. `False`: O valor booleano `False` é sempre considerado falso.

2. `None`: O objeto `None` é usado para representar a ausência de um valor. Ele é considerado falso em contextos booleanos.

3. `0`: O inteiro zero é considerado falso.

4. `0.0`: O número de ponto flutuante zero também é considerado falso.

5. `""` (String vazia): Uma string vazia é considerada falsa.

6. `[]` (Lista vazia): Uma lista vazia é considerada falsa.

7. `{}` (Dicionário vazio): Um dicionário vazio é considerado falso.

8. `()` (Tupla vazia): Uma tupla vazia é considerada falsa.

9. `set()` (Conjunto vazio): Um conjunto vazio é considerado falso.

Além desses valores "Falsy", todos os outros valores em Python são considerados "Truthy". Isso inclui números diferentes de zero, strings não vazias, listas, dicionários, tuplas, conjuntos e outros objetos.

A ideia de valores "Truthy" e "Falsy" é frequentemente usada em avaliações condicionais, como em estruturas de controle `if`, `while`, `for`, entre outras. Por exemplo:

```python
value = 0

if value:
    print("Value is truthy")
else:
    print("Value is falsy")
```

Nesse exemplo, a saída será "Value is falsy" porque o valor de `value` é zero, que é um valor "Falsy".

É importante entender esses conceitos ao lidar com expressões condicionais e avaliações booleanas em Python, pois eles podem afetar o fluxo de controle do seu programa.

## dir, hasattr e getattr

Funções `dir`, `hasattr` e `getattr` em Python.

1. **`dir()`**:

A função `dir()` é uma função embutida em Python que retorna uma lista de nomes de atributos e métodos de um objeto. Ela pode ser usada para explorar o conteúdo de um objeto e descobrir quais métodos e atributos estão disponíveis para ele. Se você chamar `dir()` sem argumentos, ela retornará uma lista dos nomes no escopo atual.

Exemplo:
```python
my_list = [1, 2, 3]
print(dir(my_list))
```

2. **`hasattr()`**:

A função `hasattr()` é usada para verificar se um objeto possui um atributo específico. Ela recebe dois argumentos: o objeto e o nome do atributo como uma string. Ela retorna `True` se o objeto tiver o atributo e `False` caso contrário.

Exemplo:
```python
class MyClass:
    def __init__(self):
        self.my_attribute = 42

obj = MyClass()

print(hasattr(obj, 'my_attribute'))  # True
print(hasattr(obj, 'nonexistent_attribute'))  # False
```

3. **`getattr()`**:

A função `getattr()` é usada para obter o valor de um atributo de um objeto. Ela recebe três argumentos: o objeto, o nome do atributo como uma string e, opcionalmente, um valor padrão para retornar se o atributo não estiver presente no objeto. Se o atributo não existir e nenhum valor padrão for fornecido, `getattr()` lançará uma exceção AttributeError.

Exemplo:
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")

print(getattr(person, 'name'))  # Retorna o valor do atributo 'name' ('Alice')
print(getattr(person, 'age', 25))  # Retorna 25, pois 'age' não existe no objeto
```

Essas funções são úteis para inspecionar e interagir com objetos em tempo de execução, permitindo uma maior flexibilidade e dinamismo na programação Python.
