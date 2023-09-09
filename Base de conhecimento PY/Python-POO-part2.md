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

## A super e a sobreposição de membros

Em programação orientada a objetos (POO) em Python, a super e a sobreposição de membros são conceitos importantes para entender como as classes podem herdar e substituir comportamentos de outras classes. Vamos explorar esses conceitos em detalhes:

1. **Herança:**
   A herança é um princípio fundamental na POO, que permite que uma classe (chamada classe derivada ou subclasse) herde os atributos e métodos de outra classe (chamada classe base ou superclasse). A classe derivada pode estender ou modificar o comportamento da classe base, mas ela herda os membros da classe base.

2. **Método `super()`:**
   O método `super()` é usado para chamar métodos da classe base a partir da classe derivada. Isso é útil quando você deseja estender o comportamento de um método da classe base na classe derivada, mas também deseja executar o código do método da classe base. O método `super()` é comumente usado dentro do método da classe derivada para chamar o método correspondente da classe base.

   Exemplo:

   ```python
   class ClasseBase:
       def __init__(self, valor):
           self.valor = valor

       def imprimir(self):
           print(self.valor)

   class ClasseDerivada(ClasseBase):
       def __init__(self, valor, novo_valor):
           super().__init__(valor)  # Chama o construtor da ClasseBase
           self.novo_valor = novo_valor

       def imprimir(self):
           super().imprimir()  # Chama o método imprimir da ClasseBase
           print(self.novo_valor)

   obj = ClasseDerivada(10, 20)
   obj.imprimir()
   ```

   Neste exemplo, `super().__init__(valor)` chama o construtor da classe base `ClasseBase`, e `super().imprimir()` chama o método `imprimir()` da classe base, permitindo que o comportamento da classe base seja estendido na classe derivada.

3. **Sobreposição (Override):**
   A sobreposição é o conceito de substituir um método da classe base na classe derivada. Isso permite que a classe derivada forneça sua própria implementação para um método que foi herdado da classe base. No exemplo acima, a classe derivada `ClasseDerivada` sobrepôs o método `imprimir()` da classe base.

   A sobreposição é uma maneira poderosa de personalizar o comportamento de uma classe derivada sem modificar a classe base.

Em resumo, a `super()` é usada para acessar os membros da classe base em uma classe derivada, enquanto a sobreposição permite substituir os métodos herdados da classe base por implementações personalizadas na classe derivada. Esses conceitos são fundamentais para criar hierarquias de classes flexíveis e reutilizáveis em Python e em outras linguagens orientadas a objetos.

## Herança múltipla

A herança múltipla é um conceito da programação orientada a objetos (POO) que permite que uma classe herde atributos e métodos de várias classes pai. No Python, essa característica é suportada, o que significa que uma classe pode herdar de várias classes pai, combinando assim características de várias fontes diferentes. No entanto, a herança múltipla deve ser usada com cuidado, pois pode levar a complexidade e ambiguidade no código.

Aqui está um exemplo simples de como a herança múltipla funciona em Python:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Mamifero(Animal):
    def fazer_som(self):
        return "Som de mamífero"

class Ave(Animal):
    def fazer_som(self):
        return "Som de ave"

class MamiferoVoador(Mamifero, Ave):
    def __init__(self, nome):
        super().__init__(nome)

# Criando uma instância da classe MamiferoVoador
morcego = MamiferoVoador("Branco")

print(morcego.nome)  # Saída: Branco
print(morcego.fazer_som())  # Saída: Som de mamífero
```

Neste exemplo, temos quatro classes:

1. `Animal`: Uma classe base que define uma propriedade `nome` e um método `fazer_som`.
2. `Mamifero` e `Ave`: Duas classes que herdam de `Animal` e substituem o método `fazer_som` com comportamentos específicos para mamíferos e aves, respectivamente.
3. `MamiferoVoador`: Uma classe que herda de ambas `Mamifero` e `Ave` usando herança múltipla. Isso significa que `MamiferoVoador` herda as características de ambas as classes pai.

Quando criamos uma instância de `MamiferoVoador`, ela pode acessar os atributos e métodos de ambas as classes pai, desde que não haja conflitos de nomes. Se houver conflitos, a ordem das classes na lista de herança determinará qual método ou atributo será usado. No exemplo acima, `Mamifero` vem antes de `Ave`, então o método `fazer_som` de `Mamifero` é chamado.

No entanto, é importante notar que a herança múltipla pode tornar o código complexo e difícil de manter, especialmente quando há muitas classes envolvidas. Em alguns casos, é preferível usar outras técnicas de POO, como composição, para evitar problemas de herança múltipla. Além disso, a herança múltipla pode levar a ambiguidades se não for usada com cuidado, e é importante planejar a estrutura das classes com antecedência para evitar conflitos.

## A ordem de resolução de métodos
O MRO, que significa "Method Resolution Order" (Ordem de Resolução de Métodos), é um conceito crucial na programação orientada a objetos, especialmente quando se trata de herança múltipla. O MRO determina a ordem em que as classes base são pesquisadas quando um método é chamado em uma classe derivada. Ele ajuda a evitar ambiguidades e define qual implementação de método deve ser usada em caso de herança múltipla.

No Python, a MRO é calculada usando o algoritmo C3, que é uma adaptação do algoritmo CLOS (Common Lisp Object System). Esse algoritmo é responsável por estabelecer uma ordem linear em que as classes base são pesquisadas quando um método é chamado em uma classe derivada. Aqui estão os principais pontos sobre como o MRO funciona:

1. **Ordem de pesquisa das classes base**: O MRO determina a ordem em que as classes base de uma classe derivada são pesquisadas quando um método é chamado. A ordem é importante para garantir que a implementação correta do método seja usada, especialmente em casos de herança múltipla.

2. **Ordem C3**: O algoritmo C3 calcula a ordem de pesquisa ideal para evitar ambiguidades. Ele leva em consideração as relações de herança entre as classes e suas subclasses para determinar a ordem.

3. **Super():** O uso da função `super()` em uma classe derivada permite chamar o método da classe base seguinte na ordem de resolução de métodos. Isso é útil para garantir que todos os métodos das classes base sejam chamados corretamente, preservando a ordem do MRO.

4. **Herança múltipla**: O MRO é particularmente importante em linguagens como o Python, que suportam herança múltipla. Herdar de várias classes pode criar situações onde os métodos têm o mesmo nome em classes diferentes, e o MRO determina qual método deve ser usado.

5. **Caso de ambiguidade**: Se houver uma ambiguidade na ordem de resolução de métodos, o Python lançará um erro de tempo de execução para informar que a chamada de método é ambígua. Nesse caso, você precisará revisar a estrutura de herança e, se necessário, reorganizar as classes ou renomear métodos para resolver a ambiguidade.

6. **Visualização do MRO**: Você pode usar a função `mro()` ou a propriedade `.__mro__` de uma classe para visualizar a ordem de resolução de métodos. Isso pode ser útil para entender como o Python determina a ordem de pesquisa das classes base.

A ordem de resolução de métodos é um mecanismo poderoso para gerenciar herança em Python e outras linguagens de programação orientadas a objetos. Ele ajuda a evitar problemas de ambiguidade e garante que os métodos sejam chamados na ordem correta, tornando o código mais previsível e fácil de entender.

## **`mro()`** & **`__mro__` (Dunder MRO)**

1. **`mro()`**:

   O método `mro()` é uma função que pode ser chamada em uma classe e retorna a ordem de resolução de métodos (MRO) dessa classe como uma lista de classes. Ele permite que você veja a ordem exata em que as classes base serão pesquisadas quando você chamar um método em uma instância dessa classe. Aqui está um exemplo simples:

   ```python
   class A:
       pass

   class B(A):
       pass

   class C(A):
       pass

   class D(B, C):
       pass

   print(D.mro())
   ```

   A saída será uma lista que representa a ordem de resolução de métodos para a classe `D`. A ordem será `[D, B, C, A, object]`, indicando que primeiro será verificada a própria classe `D`, depois a classe base `B`, em seguida a classe base `C`, depois a classe base `A` e, finalmente, a classe base `object`.

2. **`__mro__` (Dunder MRO)**:

   A propriedade `__mro__`, também conhecida como dunder MRO, é uma propriedade especial que está disponível em todas as classes em Python. Ela fornece a mesma informação que o método `mro()`, mas como uma tupla. Você pode acessá-la diretamente usando a notação de ponto em uma classe. Aqui está um exemplo de como você pode usá-la:

   ```python
   class A:
       pass

   class B(A):
       pass

   class C(A):
       pass

   class D(B, C):
       pass

   print(D.__mro__)
   ```

   A saída será uma tupla que representa a ordem de resolução de métodos para a classe `D`. A ordem será a mesma que no exemplo anterior: `(D, B, C, A, object)`.

Ambas as formas, `mro()` e `__mro__`, fornecem informações sobre a ordem de resolução de métodos, mas você pode escolher a que melhor se adapta à sua preferência de uso no código. Geralmente, `mro()` é usado quando você deseja obter a MRO como uma lista, enquanto `__mro__` é usado quando você quer acessar a MRO como uma tupla diretamente a partir da classe.
