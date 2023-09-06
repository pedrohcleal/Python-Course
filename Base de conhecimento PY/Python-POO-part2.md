# POO Part2

## @property - um getter pythônico

Em Python, o `@property` é um decorador que é usado para transformar um método em um atributo de leitura somente (read-only). Isso permite que você defina métodos personalizados para acessar e calcular valores de atributos de uma classe, ao mesmo tempo em que mantém a sintaxe de acesso a atributos simples, como se fossem variáveis comuns. O uso de `@property` é uma técnica importante na programação orientada a objetos (POO) para implementar encapsulamento e controle de acesso aos atributos de uma classe.

Aqui está como você pode usar o `@property` em Python:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo privado com um sublinhado prefixado por convenção
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade não pode ser negativa.")

    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto Pessoa
pessoa = Pessoa("Alice", 30)

# Usando o @property para acessar os atributos como se fossem variáveis
print(pessoa.nome)  # Saída: Alice
print(pessoa.idade)  # Saída: 30

# Usando o setter definido pelo @property para modificar a idade
pessoa.idade = 32
print(pessoa.idade)  # Saída: 32

# Tentando definir uma idade negativa
pessoa.idade = -5  # Isso levanta um ValueError
```

Neste exemplo, `@property` é usado para criar métodos `nome` e `idade` que permitem acessar os atributos `_nome` e `_idade` de maneira controlada. O uso de um sublinhado prefixado em `_nome` e `_idade` é uma convenção em Python para indicar que esses atributos devem ser tratados como privados e não devem ser acessados diretamente de fora da classe.

O método `@idade.setter` é usado para permitir a modificação controlada do atributo `idade`. Isso permite que você defina regras ou verificações ao atribuir um novo valor à idade, como garantir que a idade não seja negativa.

O uso de `@property` ajuda a manter o encapsulamento e fornece um controle mais preciso sobre o acesso e a modificação dos atributos de uma classe, tornando o código mais robusto e mais fácil de manter.
