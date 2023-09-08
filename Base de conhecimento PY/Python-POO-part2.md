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

## Associaçãao, agregação e composição - POO

Na programação orientada a objetos (POO) em Python, a associação, agregação e composição são três formas de relacionar objetos entre si. Elas descrevem como os objetos se conectam e interagem em um sistema orientado a objetos. Vamos explorar cada uma delas:

1. **Associação**:

   A associação é o relacionamento mais simples entre objetos. Ela ocorre quando um objeto faz referência a outro objeto, geralmente por meio de um atributo que armazena uma referência a esse objeto. Essa associação não implica que um objeto seja parte integrante do outro, apenas que eles têm conhecimento mútuo. Por exemplo:

   ```python
   class Pessoa:
       def __init__(self, nome):
           self.nome = nome

   class Carro:
       def __init__(self, marca):
           self.marca = marca

   pessoa = Pessoa("Alice")
   carro = Carro("Toyota")

   pessoa.carro = carro  # Associação entre a pessoa e o carro
   ```

   Nesse exemplo, a pessoa e o carro estão associados, mas nenhum é parte essencial do outro.

2. **Agregação**:

   A agregação é um relacionamento mais forte do que a associação. Ela ocorre quando um objeto é composto por outros objetos, mas esses objetos ainda podem existir independentemente do objeto principal. Isso significa que a destruição do objeto principal não afeta necessariamente os objetos agregados. Por exemplo:

   ```python
   class SalaDeAula:
       def __init__(self, numero):
           self.numero = numero
           self.alunos = []

       def adicionar_aluno(self, aluno):
           self.alunos.append(aluno)

   class Aluno:
       def __init__(self, nome):
           self.nome = nome

   sala = SalaDeAula(101)
   aluno1 = Aluno("João")
   aluno2 = Aluno("Maria")

   sala.adicionar_aluno(aluno1)
   sala.adicionar_aluno(aluno2)

   # A sala de aula possui uma agregação de alunos
   ```

   Nesse caso, a sala de aula "agrega" alunos, mas eles ainda são objetos independentes que podem existir fora da sala de aula.

3. **Composição**:

   A composição é o relacionamento mais forte entre objetos e implica que um objeto é parte essencial de outro objeto. Em outras palavras, a destruição do objeto principal também implica a destruição dos objetos compostos. Um exemplo típico de composição é quando um objeto é criado como parte do construtor de outro objeto. Por exemplo:

   ```python
   class CorpoHumano:
       def __init__(self):
           self.cerebro = Cerebro()

   class Cerebro:
       def __init__(self):
           self.pensamentos = []

       def adicionar_pensamento(self, pensamento):
           self.pensamentos.append(pensamento)

   meu_corpo = CorpoHumano()
   meu_corpo.cerebro.adicionar_pensamento("Estou com fome")

   # O Cérebro é uma parte essencial do CorpoHumano (composição)
   ```

   Nesse exemplo, o objeto `Cerebro` é uma parte essencial do objeto `CorpoHumano`, e a destruição do corpo também implica a destruição do cérebro.

Em resumo, a associação é um relacionamento mais fraco, a agregação é um relacionamento intermediário e a composição é um relacionamento mais forte entre objetos em programação orientada a objetos em Python. A escolha entre esses tipos de relacionamentos depende dos requisitos do seu sistema e da forma como os objetos devem interagir.

## Heranças:

Em programação orientada a objetos (POO) em Python, as heranças desempenham um papel fundamental. A herança é um conceito que permite que uma classe herde atributos e métodos de outra classe. Isso promove a reutilização de código e facilita a criação de hierarquias de classes, onde classes filhas herdam características e comportamentos de classes pai (ou superclasses). Vamos explorar alguns aspectos importantes sobre heranças em Python:

1. Sintaxe de Herança:
   Para criar uma classe filha que herda de uma classe pai, você define a classe filha e coloca o nome da classe pai entre parênteses na definição da classe filha. Aqui está um exemplo básico:

   ```python
   class Pai:
       def __init__(self):
           self.nome = "Pai"
       
       def falar(self):
           print(f"{self.nome} diz: Olá!")

   class Filho(Pai):
       def __init__(self):
           super().__init__()
           self.nome = "Filho"
   
   filho = Filho()
   filho.falar()  # Saída: "Filho diz: Olá!"
   ```

   Observe o uso de `super().__init__()` na classe Filho para chamar o construtor da classe Pai.

2. Métodos e Atributos Herdados:
   Quando uma classe filha herda de uma classe pai, ela obtém todos os métodos e atributos da classe pai. A classe filha pode então adicionar novos métodos ou substituir (sobrescrever) os métodos herdados.

3. Sobrescrita de Métodos:
   A sobrescrita de métodos permite que uma classe filha substitua a implementação de um método herdado da classe pai. Isso é útil quando você deseja que a classe filha tenha um comportamento ligeiramente diferente. Veja um exemplo:

   ```python
   class Pai:
       def falar(self):
           print("Pai diz: Olá!")

   class Filho(Pai):
       def falar(self):
           print("Filho diz: Olá, Papai!")

   filho = Filho()
   filho.falar()  # Saída: "Filho diz: Olá, Papai!"
   ```

4. Múltipla Herança:
   Python permite a múltipla herança, onde uma classe pode herdar de várias classes pai. No entanto, isso pode levar a complexidades de resolução de métodos e deve ser usado com cuidado.

   ```python
   class Mae:
       def falar(self):
           print("Mãe diz: Olá!")

   class Pai:
       def falar(self):
           print("Pai diz: Olá!")

   class Filho(Mae, Pai):
       pass

   filho = Filho()
   filho.falar()  # Saída: "Mãe diz: Olá!"
   ```

   Nesse exemplo, a classe Filho herda de tanto Mae quanto Pai, mas a ordem em que as classes pai são listadas na definição da classe filha determina qual método falar será chamado.

As heranças são uma parte importante do paradigma de programação orientada a objetos e Python oferece flexibilidade e recursos poderosos para trabalhar com heranças de maneira eficaz. No entanto, é importante usá-las com cuidado para manter um código claro e fácil de entender.
