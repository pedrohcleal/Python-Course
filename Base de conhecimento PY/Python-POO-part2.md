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

## Encapsulamento - public, protectec and private

Em Python, o encapsulamento é um conceito fundamental da Programação Orientada a Objetos (POO) que se refere à forma como os atributos e métodos de uma classe são acessados e modificados a partir de fora da classe. Python não implementa o encapsulamento da mesma forma que algumas outras linguagens de programação, como Java ou C++, mas oferece certos mecanismos para controlar o acesso aos membros de uma classe.

Os modificadores de acesso em Python não são tão rígidos quanto em algumas outras linguagens, como o Java, mas eles são baseados em convenções de nomenclatura e não em palavras-chave específicas. Os três principais níveis de acesso em Python são:

1. **Public**: Em Python, por padrão, todos os membros de uma classe são públicos, o que significa que eles podem ser acessados e modificados a partir de qualquer lugar no código. Os membros públicos são acessados diretamente pelo nome, sem nenhuma restrição.

```python
class MinhaClasse:
    def __init__(self):
        self.valor_publico = 10

obj = MinhaClasse()
print(obj.valor_publico)  # Acesso direto ao membro público
```

2. **Protected**: Em Python, para indicar que um membro deve ser tratado como protegido, você pode usar uma convenção de nomenclatura com um sublinhado simples no início do nome do membro. No entanto, isso é apenas uma convenção e não impede o acesso direto ao membro. O programador é encorajado a não acessar membros protegidos diretamente, mas nada impede que isso seja feito.

```python
class MinhaClasse:
    def __init__(self):
        self._valor_protegido = 20

obj = MinhaClasse()
print(obj._valor_protegido)  # Acesso direto ao membro protegido (convenção)
```

3. **Private**: Em Python, para indicar que um membro deve ser tratado como privado, você pode usar uma convenção de nomenclatura com dois sublinhados no início do nome do membro. Novamente, isso é apenas uma convenção, e o membro privado ainda pode ser acessado diretamente, mas com uma pequena modificação no nome, que inclui o nome da classe.

```python
class MinhaClasse:
    def __init__(self):
        self.__valor_privado = 30

obj = MinhaClasse()
# Acesso ao membro privado (com modificação no nome)
print(obj._MinhaClasse__valor_privado)
```

É importante notar que, em Python, a ênfase está na responsabilidade do programador em seguir as convenções de nomenclatura e respeitar os membros protegidos e privados, em vez de impor restrições rígidas de acesso. O objetivo é fornecer flexibilidade e confiança no programador, em vez de impor restrições estritas como em algumas outras linguagens de programação. Portanto, o encapsulamento em Python é mais uma questão de convenção e boas práticas do que de restrições de acesso.
