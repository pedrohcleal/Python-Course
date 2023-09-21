# Introdução a POO

A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia na ideia de estruturar o código em torno de objetos, que são instâncias de classes. No Python, a POO é uma parte fundamental da linguagem e oferece uma maneira eficaz de organizar, reutilizar e modularizar o código. Nesta introdução, vamos explorar os conceitos básicos da POO em Python.

Em POO, uma classe é um modelo ou plano para criar objetos. Um objeto é uma instância de uma classe e contém características (atributos) e comportamentos (métodos). A POO se concentra em encapsular o estado e o comportamento relacionados em um único pacote chamado objeto.

Vamos começar com um exemplo simples para ilustrar os conceitos:

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        self.velocidade -= quantidade
        if self.velocidade < 0:
            self.velocidade = 0

    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}, Velocidade: {self.velocidade} km/h")

# Criando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Ford", "Mustang")

# Usando os métodos para interagir com os objetos
carro1.acelerar(30)
carro2.acelerar(50)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
```

Neste exemplo, criamos uma classe `Carro` com atributos como `marca`, `modelo` e `velocidade`. Os métodos `acelerar`, `frear` e `exibir_informacoes` permitem interagir com os objetos criados a partir dessa classe.

A função `__init__` é um construtor especial que é chamado quando um objeto é criado a partir da classe. O parâmetro `self` refere-se ao próprio objeto e é usado para acessar seus atributos e métodos.

Através da POO, o código se torna mais organizado, modular e reutilizável. As classes permitem abstrair os detalhes complexos do programa, tornando-o mais compreensível e manutenível.

Em resumo, a POO em Python envolve a criação de classes que definem atributos e métodos, e a criação de objetos a partir dessas classes para interagir com o código. Isso promove a estruturação lógica e a eficiência na programação.

## Atributos de classe

Em Python, os atributos de classe são variáveis que pertencem a uma classe em vez de a uma instância específica dessa classe. Eles são compartilhados por todas as instâncias da classe e são definidos dentro da classe, mas fora de qualquer método. Os atributos de classe são usados para armazenar informações que são relevantes para a classe como um todo, em vez de para instâncias individuais da classe. Aqui estão alguns pontos-chave sobre os atributos de classe em Python:

1. Definição de Atributos de Classe:
   Os atributos de classe são definidos dentro da classe, fora de qualquer método. Eles são declarados diretamente na classe usando a notação `nome_atributo = valor`.

2. Compartilhamento de Dados:
   Todos os objetos (instâncias) de uma classe têm acesso ao mesmo valor do atributo de classe. Isso significa que as alterações feitas em um atributo de classe em uma instância serão refletidas em todas as outras instâncias da mesma classe.

3. Acesso a Atributos de Classe:
   Para acessar um atributo de classe, você pode usar a sintaxe `NomeDaClasse.nome_do_atributo` ou `nome_instancia.nome_do_atributo`, embora seja mais comum acessá-lo usando o nome da classe.

4. Modificação de Atributos de Classe:
   Os atributos de classe podem ser modificados usando o nome da classe, mas isso afetará todas as instâncias da classe. Por exemplo:
   
   ```python
   class MinhaClasse:
       atributo_de_classe = 0

   obj1 = MinhaClasse()
   obj2 = MinhaClasse()

   MinhaClasse.atributo_de_classe = 42  # Altera o valor para todas as instâncias
   print(obj1.atributo_de_classe)  # Saída: 42
   print(obj2.atributo_de_classe)  # Saída: 42
   ```

5. Uso Comum:
   Os atributos de classe são frequentemente usados para armazenar configurações, constantes compartilhadas ou informações globais relevantes para a classe em si.

Aqui está um exemplo simples de uma classe com um atributo de classe:

```python
class Pessoa:
    populacao = 0  # Atributo de classe para rastrear o número total de pessoas

    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    def __del__(self):
        Pessoa.populacao -= 1

pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob")

print(Pessoa.populacao)  # Saída: 2 (o número total de pessoas é mantido no atributo de classe)
```

Neste exemplo, o atributo de classe `populacao` é usado para rastrear o número total de instâncias da classe `Pessoa`, e ele é incrementado no construtor e decrementado no destrutor das instâncias.

## A diferença entre os atributos de classe e os atributos de instância

Os atributos de classe e os atributos de instância são dois tipos diferentes de variáveis que podem ser definidas em uma classe em programação orientada a objetos. Eles têm comportamentos e finalidades distintas:

1. Atributos de Classe:
   - São compartilhados por todas as instâncias (objetos) da classe.
   - São definidos fora dos métodos da classe, geralmente no nível da classe.
   - São acessados usando o nome da classe, seguido por um ponto e o nome do atributo.
   - Mantêm o mesmo valor para todas as instâncias da classe, a menos que seja alterado explicitamente.
   - Úteis quando se deseja armazenar informações que se aplicam a toda a classe, como constantes ou configurações globais.

Exemplo em Python:
```python
class Pessoa:
    # Atributo de classe
    especie = "Homo sapiens"

    def __init__(self, nome, idade):
        # Atributos de instância
        self.nome = nome
        self.idade = idade

# Atributo de classe acessado usando o nome da classe
print(Pessoa.especie)  # Saída: "Homo sapiens"
```

2. Atributos de Instância:
   - São específicos de cada objeto (instância) da classe.
   - São definidos no construtor (__init__) da classe e podem variar de objeto para objeto.
   - São acessados usando a instância do objeto, seguida por um ponto e o nome do atributo.
   - Cada objeto pode ter valores diferentes para seus atributos de instância.
   - Úteis quando se deseja armazenar informações exclusivas para cada objeto.

Exemplo em Python:
```python
class Carro:
    def __init__(self, marca, modelo):
        # Atributos de instância
        self.marca = marca
        self.modelo = modelo

# Criando duas instâncias (objetos) da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Atributos de instância são específicos para cada objeto
print(carro1.marca)  # Saída: "Toyota"
print(carro2.marca)  # Saída: "Honda"
```

Em resumo, a principal diferença entre atributos de classe e atributos de instância é que os atributos de classe são compartilhados por todas as instâncias da classe e mantêm o mesmo valor para todas elas, enquanto os atributos de instância são específicos para cada objeto e podem ter valores diferentes para cada instância. A escolha entre eles depende da necessidade de armazenar informações que são globais para a classe ou específicas para cada objeto.

## Métodos em classe:
Em Python, métodos em classe são funções que são definidas dentro de uma classe e operam em instâncias dessa classe. Eles são usados para definir o comportamento das instâncias da classe e são acessados através de uma instância da classe ou da própria classe. Existem três tipos principais de métodos em classe em Python:

1. **Métodos de Instância:**
   - Métodos de instância são os mais comuns em Python. Eles operam em instâncias específicas da classe e são chamados usando uma instância da classe.
   - A primeira variável em um método de instância é geralmente chamada de `self` por convenção, e ela se refere à instância atual da classe. Isso permite que você acesse os atributos e outros métodos da instância dentro do método.
   - Exemplo:

   ```python
   class MinhaClasse:
       def __init__(self, valor):
           self.valor = valor

       def imprimir_valor(self):
           print(self.valor)

   instancia = MinhaClasse(42)
   instancia.imprimir_valor()  # Chama o método de instância
   ```

2. **Métodos de Classe:**
   - Métodos de classe são métodos que operam na classe em si, em vez de em instâncias específicas. Eles são decorados com o decorador `@classmethod`.
   - Esses métodos recebem a própria classe como o primeiro argumento, geralmente chamado de `cls` por convenção, em vez da instância.
   - Eles são usados para operações relacionadas à classe e podem ser chamados diretamente na classe ou em uma instância da classe.
   - Exemplo:

   ```python
   class MinhaClasse:
       contador = 0

       def __init__(self):
           MinhaClasse.contador += 1

       @classmethod
       def obter_contador(cls):
           return cls.contador

   instancia1 = MinhaClasse()
   instancia2 = MinhaClasse()
   print(MinhaClasse.obter_contador())  # Chama o método de classe
   ```

3. **Métodos Estáticos:**
   - Métodos estáticos são métodos que não dependem de instâncias específicas ou da classe em si. Eles são decorados com o decorador `@staticmethod`.
   - Eles são usados quando você precisa de uma função relacionada à classe, mas não precisa acessar seus atributos ou métodos.
   - Eles podem ser chamados diretamente na classe, sem criar uma instância.
   - Exemplo:

   ```python
   class Calculadora:
       @staticmethod
       def somar(a, b):
           return a + b

   resultado = Calculadora.somar(5, 3)  # Chama o método estático
   ```

Em resumo, os métodos em classe em Python permitem que você defina o comportamento das instâncias de uma classe e manipule operações relacionadas à classe em si. Métodos de instância operam em instâncias específicas, métodos de classe operam na classe e métodos estáticos são independentes de instâncias e classes, sendo usados quando a lógica não está diretamente ligada aos atributos ou métodos da classe.

## Sobre @classmethod, factories e cLs
No contexto de programação orientada a objetos, as fábricas (factories) e o uso do parâmetro `cls` têm a ver com a criação de objetos e a manipulação de classes. Vou explicar cada um deles separadamente:

1. **Fábricas (Factories):**
   - As fábricas são funções ou métodos que são usados para criar e retornar instâncias de classes. Elas são usadas quando a criação de um objeto envolve alguma lógica complicada ou quando você deseja encapsular a criação de objetos em um local centralizado.
   - O objetivo das fábricas é esconder a complexidade da criação de objetos do restante do código e fornecer uma interface mais simples para criar objetos.
   - Exemplo:

   ```python
   class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade

   def criar_pessoa(nome, idade):
       if idade >= 18:
           return Pessoa(nome, idade)
       else:
           return None

   pessoa1 = criar_pessoa("Alice", 25)
   pessoa2 = criar_pessoa("Bob", 15)

   if pessoa1:
       print(f"{pessoa1.nome} tem {pessoa1.idade} anos.")
   else:
       print("Pessoa não é maior de idade.")

   if pessoa2:
       print(f"{pessoa2.nome} tem {pessoa2.idade} anos.")
   else:
       print("Pessoa não é maior de idade.")
   ```

2. **Parâmetro `cls` (Classe):**
   - O parâmetro `cls` é frequentemente usado em métodos de classe e métodos de fábrica para se referir à própria classe onde o método é definido.
   - É uma convenção comum nomear esse parâmetro como `cls`, mas você pode usar qualquer nome, desde que mantenha a mesma convenção no código.
   - Usar `cls` permite que você acesse ou crie instâncias da classe, mesmo quando você não sabe o nome da classe antecipadamente. Isso é útil em herança e em métodos de fábrica que criam instâncias da classe atual ou de subclasses.
   - Exemplo:

   ```python
   class Veiculo:
       veiculos = []

       def __init__(self, nome):
           self.nome = nome
           Veiculo.veiculos.append(self)

       @classmethod
       def criar_veiculo(cls, nome):
           return cls(nome)

   class Carro(Veiculo):
       pass

   carro1 = Veiculo.criar_veiculo("Carro A")
   carro2 = Carro.criar_veiculo("Carro B")

   print(Veiculo.veiculos)  # [Veiculo(nome='Carro A'), Carro(nome='Carro B')]
   ```

   Neste exemplo, o parâmetro `cls` é usado no método de classe `criar_veiculo` para criar instâncias da classe atual (`Veiculo` ou `Carro`) com base na classe que o chama.

Em resumo, fábricas são usadas para criar objetos de forma mais flexível e encapsulada, enquanto o parâmetro `cls` é usado em métodos de classe e fábricas para se referir à classe atual, tornando-os úteis em situações em que a herança está envolvida ou quando você precisa criar instâncias de classes dinamicamente.

## Uso de getters em classes

Em Python, você pode usar getters em classes de programação orientada a objetos (POO) para acessar atributos privados de uma classe de maneira controlada. Embora Python não tenha modificadores de acesso como em algumas outras linguagens de programação (como `private` ou `protected`), é uma convenção em Python que atributos que começam com um sublinhado (`_`) sejam considerados como "privados" e não devem ser acessados diretamente fora da classe. Para acessar esses atributos, você pode usar métodos getters.

Aqui está um exemplo simples de como criar e usar um getter em uma classe em Python:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo "privado" com um sublinhado
        self._idade = idade

    # Getter para o atributo "nome"
    def get_nome(self):
        return self._nome

    # Getter para o atributo "idade"
    def get_idade(self):
        return self._idade

# Criar uma instância da classe Pessoa
pessoa = Pessoa("João", 30)

# Usar os getters para acessar os atributos "nome" e "idade"
print("Nome:", pessoa.get_nome())
print("Idade:", pessoa.get_idade())
```

Neste exemplo, `_nome` e `_idade` são atributos considerados "privados", e seus valores são acessados apenas por meio de métodos getters `get_nome` e `get_idade`. Usar getters permite que você tenha mais controle sobre o acesso aos atributos da classe, o que pode ser útil para implementar lógica de validação ou manipulação dos dados antes de serem retornados.

É importante mencionar que, em Python, essa convenção de "atributos privados" é apenas uma convenção, e ainda é possível acessar esses atributos diretamente se necessário. No entanto, é geralmente considerado uma boa prática usar getters e setters para manter a encapsulação e fornecer um ponto de acesso controlado aos atributos da classe.
