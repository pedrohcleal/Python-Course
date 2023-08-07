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
