# Padrões de Projeto

## Princípios SOLID

Os princípios SOLID são um conjunto de cinco princípios de design de software que foram introduzidos por Robert C. Martin para criar sistemas mais compreensíveis, flexíveis e fáceis de manter. Eles são:

1. **Princípio da Responsabilidade Única (Single Responsibility Principle - SRP):**
   - Este princípio afirma que uma classe deve ter apenas uma razão para mudar, ou seja, deve ter apenas uma responsabilidade. Em Python, isso significa que uma classe deve ter uma única tarefa ou funcionalidade bem definida.

   Exemplo:
   ```python
   class FileManager:
       def read_file(self, filename):
           # lógica para ler um arquivo

       def write_file(self, filename, content):
           # lógica para escrever em um arquivo
   ```

2. **Princípio Aberto/Fechado (Open/Closed Principle - OCP):**
   - Este princípio sugere que uma classe deve ser aberta para extensão, mas fechada para modificação. Isso significa que você pode adicionar novos recursos sem alterar o código existente. Em Python, você pode alcançar isso usando herança e polimorfismo.

   Exemplo:
   ```python
   class Shape:
       def area(self):
           pass

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius * self.radius

   class Square(Shape):
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side * self.side
   ```

3. **Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP):**
   - Este princípio afirma que objetos de uma classe base devem ser substituíveis por objetos de suas classes derivadas sem afetar a corretude do programa. Em Python, isso significa que as subclasses devem poder ser usadas onde quer que suas superclasses sejam usadas.

   Exemplo:
   ```python
   class Bird:
       def fly(self):
           pass

   class Sparrow(Bird):
       def fly(self):
           print("Sparrow is flying")

   class Penguin(Bird):
       def swim(self):
           print("Penguin is swimming")
   ```

4. **Princípio da Segregação de Interface (Interface Segregation Principle - ISP):**
   - Este princípio afirma que uma classe não deve ser forçada a implementar interfaces que ela não usa. Em Python, isso significa que você deve dividir interfaces grandes em interfaces menores e mais específicas.

   Exemplo:
   ```python
   class Worker:
       def work(self):
           pass

       def eat(self):
           pass

   class SuperWorker(Worker):
       def work(self):
           pass

       def eat(self):
           pass

       def code(self):
           pass
   ```

5. **Princípio da Inversão de Dependência (Dependency Inversion Principle - DIP):**
   - Este princípio afirma que módulos de alto nível não devem depender de módulos de baixo nível, ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes, detalhes devem depender de abstrações. Em Python, isso pode ser alcançado usando injeção de dependência.

   Exemplo:
   ```python
   class LightBulb:
       def turn_on(self):
           print("LightBulb is ON")

       def turn_off(self):
           print("LightBulb is OFF")

   class Switch:
       def __init__(self, device):
           self.device = device

       def operate(self):
           pass

   class RemoteControlledSwitch(Switch):
       def operate(self):
           self.device.turn_on() if self.is_on else self.device.turn_off()
   ```

Adotar esses princípios SOLID em seu design de software em Python pode levar a um código mais modular, flexível e de fácil manutenção. No entanto, é importante lembrar que esses princípios não são regras rígidas, mas diretrizes que podem ser adaptadas de acordo com a necessidade específica de cada projeto.

## Simple Factory

O Simple Factory (ou Factory Method) é um padrão de design que pertence à categoria de padrões de criação. Ele fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. O principal objetivo é abstrair a criação de objetos e permitir que o código cliente se concentre na manipulação desses objetos, em vez de se preocupar com a lógica de criação.

Aqui está um exemplo simples de como você pode implementar um Simple Factory em Python:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Animal type not supported")

# Uso do Simple Factory
factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.speak())  # Saída: Woof!

cat = factory.create_animal("cat")
print(cat.speak())  # Saída: Meow!
```

Neste exemplo, temos uma classe base `Animal` e duas subclasses `Dog` e `Cat`, cada uma implementando o método `speak`. Em seguida, temos a classe `AnimalFactory`, que possui o método `create_animal` responsável por criar instâncias de `Dog` ou `Cat` com base no tipo passado como argumento.

O código cliente utiliza a fábrica para criar instâncias de animais, sem precisar saber detalhes sobre como essas instâncias são criadas. Isso facilita a adição de novos tipos de animais no futuro sem modificar o código cliente.

Lembre-se de que o Simple Factory é uma forma básica de implementar a criação de objetos e pode ser expandido para padrões mais complexos, como o Factory Method e o Abstract Factory, dependendo dos requisitos do projeto.

## Factory Method

O Factory Method é um padrão de projeto de software que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. Ele é uma extensão do Simple Factory que introduz a ideia de uma classe/interface abstrata para a criação de objetos, delegando a responsabilidade da criação para as subclasses.

A estrutura do Factory Method geralmente envolve uma classe abstrata que declara um método de criação (o "Factory Method" propriamente dito) e subclasses concretas que implementam esse método para criar instâncias específicas.

Aqui está um exemplo de implementação do Factory Method em Python:

```python
from abc import ABC, abstractmethod

# Classe abstrata que define o Factory Method
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Subclasse concreta que implementa o Factory Method
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Subclasse concreta que implementa o Factory Method
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Interface para o Factory Method
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Implementação concreta do Factory Method
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

# Implementação concreta do Factory Method
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Uso do Factory Method
dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak())  # Saída: Woof!

cat_factory = CatFactory()
cat = cat_factory.create_animal()
print(cat.speak())  # Saída: Meow!
```

Neste exemplo, `Animal` é uma classe abstrata que define a interface para os objetos que serão criados. `Dog` e `Cat` são subclasses concretas que implementam essa interface.

A classe abstrata `AnimalFactory` declara o Factory Method `create_animal`, e suas subclasses concretas (`DogFactory` e `CatFactory`) implementam esse método para criar instâncias específicas de animais.

O Factory Method permite que o código cliente utilize o Factory Method através da interface `AnimalFactory`, sem se preocupar com a classe específica de `Animal` que está sendo criada. Isso torna o código mais flexível e extensível, facilitando a adição de novas subclasses sem modificar o código cliente.

## Abstract Factory

O Abstract Factory é um padrão de projeto de software que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Ele é um nível acima do Factory Method, onde não apenas um objeto é criado, mas uma família inteira de objetos.

A ideia central do Abstract Factory é fornecer uma interface para criar diferentes tipos de objetos relacionados sem expor as classes concretas desses objetos. Isso ajuda a garantir que os objetos criados sejam compatíveis entre si e pertençam à mesma família.

Vamos explorar um exemplo de implementação do Abstract Factory em Python:

```python
from abc import ABC, abstractmethod

# Interface para a fábrica abstrata
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def create_sound(self):
        pass

# Implementações concretas da fábrica abstrata
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

    def create_sound(self):
        return Bark()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

    def create_sound(self):
        return Meow()

# Interface para a classe abstrata de animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Subclasses concretas de animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Interface para a classe abstrata de som
class Sound(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subclasses concretas de som
class Bark(Sound):
    def make_sound(self):
        return "Bark!"

class Meow(Sound):
    def make_sound(self):
        return "Meow!"

# Uso do Abstract Factory
def get_animal_and_sound(factory):
    animal = factory.create_animal()
    sound = factory.create_sound()
    return animal, sound

# Criando animais usando fábricas
dog_factory = DogFactory()
cat_factory = CatFactory()

dog, dog_sound = get_animal_and_sound(dog_factory)
cat, cat_sound = get_animal_and_sound(cat_factory)

print(f"The {type(dog).__name__} says: {dog.speak()} and makes the sound: {dog_sound.make_sound()}")
print(f"The {type(cat).__name__} says: {cat.speak()} and makes the sound: {cat_sound.make_sound()}")
```

Neste exemplo, temos as seguintes classes e interfaces:

1. `AnimalFactory`: Interface abstrata para as fábricas que criam animais e sons.
2. `DogFactory` e `CatFactory`: Implementações concretas de `AnimalFactory` que criam instâncias específicas de `Dog` e `Cat`, bem como suas respectivas instâncias de `Sound`.
3. `Animal`: Interface abstrata para as classes de animais.
4. `Dog` e `Cat`: Implementações concretas de `Animal`.
5. `Sound`: Interface abstrata para as classes de som.
6. `Bark` e `Meow`: Implementações concretas de `Sound`.

O método `get_animal_and_sound` recebe uma fábrica como parâmetro e retorna um par de objetos: um animal e um som. Isso demonstra como o Abstract Factory permite a criação de objetos relacionados, garantindo que pertençam à mesma família.

## Singleton

O Singleton é um padrão de design que garante a existência de apenas uma instância de uma classe e fornece um ponto global para acessar essa instância. Isso é útil quando exatamente uma instância de uma classe é necessária para coordenar ações em todo o sistema.

Em Python, o Singleton pode ser implementado de várias maneiras. Uma abordagem comum é usar um atributo de classe para armazenar a instância única e um método de classe para obter ou criar essa instância única.

Aqui está um exemplo de implementação de Singleton em Python:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Uso do Singleton
singleton_instance_1 = Singleton()
singleton_instance_2 = Singleton()

print(singleton_instance_1 is singleton_instance_2)  # Saída: True
```

Neste exemplo, a classe `Singleton` usa um atributo de classe `_instance` para armazenar a única instância. O método `__new__` é usado para criar uma nova instância apenas se `_instance` ainda não estiver definido.

Ao criar duas instâncias (`singleton_instance_1` e `singleton_instance_2`) e verificar se são as mesmas instâncias com `is`, você verá que são idênticas. Isso demonstra que apenas uma instância da classe `Singleton` foi criada, conforme o padrão Singleton.

No entanto, tenha em mente que, embora o Singleton seja útil em algumas situações, seu uso excessivo pode levar a dependências globais e acoplamento forte, o que pode tornar o código mais difícil de testar e manter. Portanto, é aconselhável considerar cuidadosamente a necessidade de um Singleton em seu projeto antes de implementá-lo.

## Monostate / Borg

O termo "Monostate" e "Borg" se referem a dois padrões de design distintos. Ambos estão relacionados ao conceito de compartilhamento de estado, mas têm abordagens diferentes. Vamos discutir brevemente cada um deles:

1. **Monostate:**
   - O Monostate é um padrão que visa garantir que todas as instâncias de uma classe compartilhem o mesmo estado, independentemente de serem consideradas objetos separados. Para alcançar isso, geralmente se usa uma combinação de variáveis de classe e instância. Embora externamente pareça que você está lidando com várias instâncias, internamente elas compartilham o mesmo estado.
   
   Exemplo de implementação do padrão Monostate:
   ```python
   class Monostate:
       _shared_state = {}

       def __new__(cls, *args, **kwargs):
           obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
           obj.__dict__ = cls._shared_state
           return obj

   # Uso do Monostate
   mono_instance1 = Monostate()
   mono_instance1.x = 10

   mono_instance2 = Monostate()
   print(mono_instance2.x)  # Saída: 10
   ```

2. **Borg:**
   - O padrão Borg visa permitir que as instâncias de uma classe compartilhem parte de seu estado, mas ainda mantenham alguma individualidade. Ao contrário do Monostate, o Borg cria instâncias separadas, mas compartilha partes específicas do estado usando uma referência compartilhada.
   
   Exemplo de implementação do padrão Borg:
   ```python
   class Borg:
       _shared_state = {}

       def __new__(cls, *args, **kwargs):
           obj = super(Borg, cls).__new__(cls, *args, **kwargs)
           obj.__dict__ = cls._shared_state
           return obj

   # Uso do Borg
   borg_instance1 = Borg()
   borg_instance1.x = 10

   borg_instance2 = Borg()
   print(borg_instance2.x)  # Saída: 10
   ```

Ambos os padrões têm suas aplicações específicas, mas geralmente são considerados padrões avançados e podem complicar a compreensão do código. É importante considerar os trade-offs envolvidos e garantir que esses padrões sejam apropriados para o seu caso de uso antes de implementá-los. Além disso, em muitas situações, é preferível usar abordagens mais simples e explícitas para compartilhamento de estado, como passagem de parâmetros ou injeção de dependência.

## Prototype

O padrão de projeto Prototype é um padrão de criação que permite a criação de novos objetos duplicando um objeto existente, chamado de protótipo. Isso é útil quando a criação de uma instância de uma classe é mais custosa ou complexa do que duplicar um objeto existente.

O padrão Prototype pode ser implementado de diferentes maneiras, mas geralmente envolve a definição de um método `clone` ou similar na classe do protótipo. Esse método cria uma cópia do objeto atual, mas permite que as subclasses ou implementações específicas ajustem os detalhes conforme necessário.

Aqui está um exemplo simples de implementação do padrão Prototype em Python:

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

# Uso do Prototype
prototype_instance = ConcretePrototype(value=10)
clone1 = prototype_instance.clone()
clone2 = prototype_instance.clone()

print(clone1.value)  # Saída: 10
print(clone2.value)  # Saída: 10

# Modificando o clone sem afetar o protótipo original
clone1.value = 20
print(clone1.value)  # Saída: 20
print(prototype_instance.value)  # Saída: 10
```

Neste exemplo, temos uma classe `Prototype` que define o método `clone`, e uma classe `ConcretePrototype` que herda dessa classe base. Quando `clone` é chamado, ele usa a função `deepcopy` do módulo `copy` para criar uma cópia profunda do objeto, garantindo que os objetos aninhados também sejam clonados.

Ao criar instâncias do protótipo e cloná-las, podemos ver que as cópias compartilham a mesma estrutura, mas são objetos independentes. Modificar o valor de um clone não afeta o valor do protótipo original.

O padrão Prototype é especialmente útil quando a criação de objetos é custosa em termos de desempenho ou quando você deseja isolar a lógica de criação de objetos em um local central. Ele permite criar novos objetos variando apenas o protótipo, o que pode ser particularmente útil em situações onde a criação de uma instância é complexa ou envolve muitos passos.

## Strategy

O padrão de projeto Strategy é um padrão comportamental que define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. O padrão permite que o cliente escolha o algoritmo a ser utilizado dinamicamente, sem alterar a estrutura do código.

A ideia fundamental do padrão Strategy é encapsular diferentes algoritmos em classes separadas, permitindo que os objetos cliente escolham entre eles com base nas necessidades específicas ou nas mudanças nos requisitos.

Aqui está um exemplo básico de implementação do padrão Strategy em Python:

```python
from abc import ABC, abstractmethod

# Interface para os algoritmos
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Implementações concretas dos algoritmos
class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Executando estratégia A"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Executando estratégia B"

# Contexto que usa a estratégia
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()

# Uso do padrão Strategy
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context = Context(strategy_a)
print(context.execute_strategy())  # Saída: Executando estratégia A

context.set_strategy(strategy_b)
print(context.execute_strategy())  # Saída: Executando estratégia B
```

Neste exemplo, temos:

1. `Strategy`: Uma interface que define o método `execute`, que será implementado por diferentes estratégias.
2. `ConcreteStrategyA` e `ConcreteStrategyB`: Implementações concretas das estratégias que definem seus próprios algoritmos específicos.
3. `Context`: O objeto cliente que mantém uma referência a uma estratégia e a utiliza conforme necessário.

O cliente (`Context`) pode alterar dinamicamente a estratégia que está sendo utilizada, permitindo que diferentes algoritmos sejam escolhidos em tempo de execução.

O padrão Strategy é valioso quando há a necessidade de suportar diferentes algoritmos ou comportamentos em uma aplicação, especialmente quando esses algoritmos podem ser intercambiáveis ou precisam ser alterados dinamicamente. Isso promove um design flexível e de fácil manutenção.

## Observer

O padrão Observer é um padrão de design comportamental que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente. Isso é útil quando você tem um objeto (chamado "sujeito" ou "observável") cujo estado pode afetar outros objetos (chamados "observadores") e você deseja garantir que todos os observadores sejam notificados quando o estado do sujeito muda.

Aqui está um exemplo básico de implementação do padrão Observer em Python:

```python
from abc import ABC, abstractmethod

# Interface para os observadores
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Sujeito observável
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Observador concreto
class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Recebi uma mensagem: {message}")

# Uso do padrão Observer
subject = Subject()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Mensagem importante!")
```

Neste exemplo:

1. `Observer`: Uma interface que define o método `update`, que será implementado pelos observadores.
2. `Subject`: O sujeito observável que mantém uma lista de observadores e notifica todos eles quando seu estado muda.
3. `ConcreteObserver`: Uma implementação concreta de observador que recebe e processa as notificações.

Ao adicionar observadores ao sujeito, qualquer mudança no sujeito aciona a notificação para todos os observadores registrados. Isso promove uma arquitetura flexível e desacoplada, pois o sujeito não precisa saber quais observadores estão interessados em suas mudanças de estado.

O padrão Observer é frequentemente utilizado em situações em que diferentes partes do sistema precisam reagir a mudanças em um objeto centralizado, como em implementações de interfaces gráficas, gerenciamento de eventos e sistemas distribuídos.

## Command

O padrão de projeto Command é um padrão comportamental que transforma uma solicitação em um objeto independente que contém toda a informação sobre a solicitação. Isso permite que você parametrize métodos com operações, adie a execução de uma operação ou a coloque em uma fila, e suporte operações que podem ser desfeitas.

Vamos explorar um exemplo básico de implementação do padrão Command em Python:

```python
from abc import ABC, abstractmethod

# Comando abstrato
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receptor - a classe que realiza a operação real
class Light:
    def turn_on(self):
        print("A luz está ligada.")

    def turn_off(self):
        print("A luz está desligada.")

# Comandos concretos
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invocador - responsável por executar os comandos
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Uso do padrão Command
light = Light()

turn_on = TurnOnCommand(light)
turn_off = TurnOffCommand(light)

remote = RemoteControl()

remote.set_command(turn_on)
remote.press_button()  # Saída: A luz está ligada.

remote.set_command(turn_off)
remote.press_button()  # Saída: A luz está desligada.
```

Neste exemplo:

- `Command`: A interface abstrata que define o método `execute`.
- `Light`: O "receptor", que é a classe que realiza a operação real.
- `TurnOnCommand` e `TurnOffCommand`: Implementações concretas do comando, cada uma associada a uma operação específica.
- `RemoteControl`: O "invocador", que é responsável por executar os comandos.

O padrão Command permite a parametrização de objetos com operações, desacopla o emissor e o receptor da solicitação, facilita a implementação de operações desfazer e refazer, e suporta a criação de macros.

Esse padrão é frequentemente utilizado em interfaces gráficas, sistemas de gerenciamento de transações, sistemas de logging e em situações onde se deseja desacoplar o código que emite um pedido do código que o processa.

## Template Method

O padrão de projeto Template Method é um padrão comportamental que define o esqueleto de um algoritmo em uma operação, mas deixa alguns passos a serem preenchidos pelas subclasses. Essas subclasses podem então alterar partes do algoritmo sem alterar sua estrutura geral.

Vamos explorar um exemplo básico de implementação do padrão Template Method em Python:

```python
from abc import ABC, abstractmethod

# Classe abstrata que define o Template Method
class AbstractClass(ABC):
    def template_method(self):
        self.common_operation1()
        self.required_operation1()
        self.common_operation2()
        self.hook()  # Método opcional (hook)
        self.required_operation2()

    # Métodos comuns
    def common_operation1(self):
        print("Operação comum 1")

    def common_operation2(self):
        print("Operação comum 2")

    # Métodos abstratos que as subclasses devem implementar
    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    # Método opcional (hook) que pode ser sobrescrito pelas subclasses
    def hook(self):
        pass

# Subclasse que implementa as operações específicas
class ConcreteClass(AbstractClass):
    def required_operation1(self):
        print("Implementação específica de Operação 1")

    def required_operation2(self):
        print("Implementação específica de Operação 2")

    def hook(self):
        print("Implementação específica do Hook")

# Uso do padrão Template Method
template_instance = ConcreteClass()
template_instance.template_method()
```

Neste exemplo:

- `AbstractClass`: A classe abstrata que define o Template Method e contém alguns métodos comuns, métodos abstratos que devem ser implementados pelas subclasses, e um método opcional (hook) que pode ser sobrescrito, mas não é obrigatório.
- `ConcreteClass`: Uma implementação concreta que herda de `AbstractClass` e fornece as implementações específicas para os métodos abstratos.

O método `template_method` representa o esqueleto do algoritmo, chamando os métodos comuns, os métodos abstratos obrigatórios e o hook opcional. As subclasses podem então implementar ou ignorar o hook conforme necessário.

O padrão Template Method é frequentemente utilizado em frameworks e bibliotecas, onde a estrutura geral de um algoritmo é fixa, mas algumas partes específicas podem variar. Ele ajuda a evitar duplicação de código ao permitir que as subclasses forneçam implementações específicas apenas para as partes necessárias do algoritmo.

## State

O padrão de projeto State é um padrão comportamental que permite a um objeto alterar seu comportamento quando seu estado interno muda. O padrão State encapsula os estados em classes separadas e delega a responsabilidade de gerenciar o estado atual para um objeto representativo do estado.

Vamos explorar um exemplo básico de implementação do padrão State em Python:

```python
from abc import ABC, abstractmethod

# Interface para os estados
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Contexto - mantém uma referência para um objeto de estado
class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

# Implementações concretas de estados
class ConcreteStateA(State):
    def handle(self):
        print("Executando a operação no Estado A")
        
class ConcreteStateB(State):
    def handle(self):
        print("Executando a operação no Estado B")

# Uso do padrão State
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context = Context(state_a)
context.request()  # Saída: Executando a operação no Estado A

context.set_state(state_b)
context.request()  # Saída: Executando a operação no Estado B
```

Neste exemplo:

- `State`: A interface que define o método `handle`, que representa a operação associada a um determinado estado.
- `Context`: O contexto que mantém uma referência para um objeto de estado e delega as chamadas ao método `handle` para o estado atual.
- `ConcreteStateA` e `ConcreteStateB`: Implementações concretas de estados que definem comportamentos específicos para os estados.

O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda. Isso é especialmente útil quando um objeto precisa alternar entre diferentes comportamentos de maneira dinâmica e quando o número de estados e transições entre eles pode crescer complexo.

O padrão State é particularmente útil em situações onde a lógica condicional baseada no estado se torna extensa e difícil de manter. Ao encapsular cada estado em uma classe separada, o padrão torna o código mais modular e fácil de entender, além de facilitar a adição de novos estados no futuro.

## Chain of Responsibility

O padrão de projeto Chain of Responsibility é um padrão comportamental que permite que você passe solicitações ao longo de uma cadeia de manipuladores. Ao longo dessa cadeia, cada manipulador decide se processa a solicitação ou a passa para o próximo manipulador na cadeia. Isso elimina a necessidade de acoplar explicitamente um remetente a um receptor e permite que vários objetos possam manipular a solicitação.

Vamos explorar um exemplo básico de implementação do padrão Chain of Responsibility em Python:

```python
from abc import ABC, abstractmethod

# Handler (Manipulador) abstrato
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# Handlers concretos
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A manipulou a solicitação.")
        elif self.successor is not None:
            self.successor.handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B manipulou a solicitação.")
        elif self.successor is not None:
            self.successor.handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            print("Handler C manipulou a solicitação.")
        elif self.successor is not None:
            self.successor.handle_request(request)

# Uso do padrão Chain of Responsibility
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_c = ConcreteHandlerC()

handler_a.successor = handler_b
handler_b.successor = handler_c

handler_a.handle_request("A")  # Saída: Handler A manipulou a solicitação.
handler_a.handle_request("B")  # Saída: Handler B manipulou a solicitação.
handler_a.handle_request("C")  # Saída: Handler C manipulou a solicitação.
handler_a.handle_request("D")  # Não há manipulador para a solicitação.
```

Neste exemplo:

- `Handler`: A classe abstrata que define um manipulador. Contém uma referência opcional para o próximo manipulador na cadeia e um método abstrato `handle_request` para processar a solicitação.
- `ConcreteHandlerA`, `ConcreteHandlerB`, `ConcreteHandlerC`: Implementações concretas de manipuladores, cada uma responsável por manipular uma determinada solicitação ou passá-la adiante para o próximo manipulador na cadeia.

O padrão Chain of Responsibility é útil quando há múltiplos objetos que podem lidar com uma solicitação e a ordem ou a composição desses objetos pode variar dinamicamente. Ele promove a flexibilidade e a extensibilidade do código, pois permite que novos manipuladores sejam adicionados ou removidos sem alterar o código cliente.

## Iterator

O padrão de projeto Iterator é um padrão comportamental que fornece uma maneira eficiente e uniforme de acessar elementos de uma coleção, sem expor sua representação subjacente. O padrão Iterator é frequentemente usado para percorrer coleções de objetos, permitindo que os clientes acessem os elementos sem conhecer os detalhes internos da implementação da coleção.

Vamos explorar um exemplo básico de implementação do padrão Iterator em Python:

```python
from abc import ABC, abstractmethod

# Interface para o Iterator
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Classe concreta que implementa o Iterator
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration("Não há mais elementos na coleção")

# Interface para a coleção
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Classe concreta que implementa a coleção
class ConcreteCollection(IterableCollection):
    def __init__(self):
        self._data = []

    def add_item(self, item):
        self._data.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._data)

# Uso do padrão Iterator
collection = ConcreteCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())
```

Neste exemplo:

- `Iterator`: A interface que define métodos para percorrer uma coleção, incluindo `has_next` para verificar se há mais elementos e `next` para obter o próximo elemento.
- `ConcreteIterator`: Uma implementação concreta de `Iterator` que mantém uma referência à coleção e rastreia a posição atual ao percorrê-la.
- `IterableCollection`: A interface para a coleção que define um método `create_iterator` para criar um iterator.
- `ConcreteCollection`: Uma implementação concreta de `IterableCollection` que mantém uma lista de itens e cria um `ConcreteIterator` para percorrê-los.

O padrão Iterator é útil quando você tem uma coleção de objetos e deseja fornecer um meio padronizado de acessar esses objetos sem expor os detalhes internos da implementação da coleção. Ele facilita a iteração sobre diferentes tipos de coleções de maneira uniforme.

## Mediator

O padrão de projeto Mediator é um padrão comportamental que define um objeto que centraliza a comunicação entre vários objetos, permitindo que eles se comuniquem de maneira desacoplada. Em vez de os objetos se comunicarem diretamente entre si, eles se comunicam apenas por meio do mediador.

Vamos explorar um exemplo básico de implementação do padrão Mediator em Python:

```python
from abc import ABC, abstractmethod

# Interface do Mediator
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Colega (Colleague) abstrato
class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, event):
        pass

    @abstractmethod
    def receive(self, event):
        pass

# Implementações concretas de Colleague
class ConcreteColleagueA(Colleague):
    def send(self, event):
        print("Colleague A enviando:", event)
        self._mediator.notify(self, event)

    def receive(self, event):
        print("Colleague A recebendo:", event)

class ConcreteColleagueB(Colleague):
    def send(self, event):
        print("Colleague B enviando:", event)
        self._mediator.notify(self, event)

    def receive(self, event):
        print("Colleague B recebendo:", event)

# Implementação concreta de Mediator
class ConcreteMediator(Mediator):
    def __init__(self, colleague_a, colleague_b):
        self._colleague_a = colleague_a
        self._colleague_b = colleague_b

    def notify(self, sender, event):
        if sender == self._colleague_a:
            self._colleague_b.receive(event)
        elif sender == self._colleague_b:
            self._colleague_a.receive(event)

# Uso do padrão Mediator
colleague_a = ConcreteColleagueA(None)  # O mediador será definido posteriormente
colleague_b = ConcreteColleagueB(None)  # O mediador será definido posteriormente

mediator = ConcreteMediator(colleague_a, colleague_b)

colleague_a._mediator = mediator
colleague_b._mediator = mediator

colleague_a.send("Mensagem para Colleague B")
colleague_b.send("Mensagem para Colleague A")
```

Neste exemplo:

- `Mediator`: A interface que define o método `notify` para permitir que os colegas comuniquem eventos uns com os outros.
- `Colleague`: A classe abstrata que representa os colegas. Cada colega mantém uma referência ao mediador.
- `ConcreteColleagueA` e `ConcreteColleagueB`: Implementações concretas de colegas que herdam de `Colleague`.
- `ConcreteMediator`: Implementação concreta de mediador que implementa a lógica de comunicação entre os colegas.

O padrão Mediator é útil quando um conjunto de objetos precisa se comunicar de maneira flexível, sem depender fortemente uns dos outros. Ele promove o desacoplamento entre os objetos, tornando mais fácil adicionar novos objetos ao sistema ou modificar as interações existentes sem alterar cada classe individualmente. Este padrão é especialmente útil em sistemas onde a complexidade das interações entre objetos cresce e torna-se difícil de gerenciar diretamente.

## Visitor e Interpreter

Os padrões de projeto Visitor e Interpreter são dois padrões comportamentais distintos que têm finalidades diferentes. Vamos explorar cada um separadamente:

### Visitor:

O padrão de projeto Visitor é usado quando você deseja adicionar novas operações a uma estrutura de objetos existente sem alterar esses objetos. Ele permite definir uma nova operação (um "visitor") sem modificar as classes dos elementos sobre os quais a operação atua.

Exemplo básico de implementação do padrão Visitor em Python:

```python
from abc import ABC, abstractmethod

# Elemento abstrato
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Elemento concreto
class ConcreteElement(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element(self)

# Visitor abstrato
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element(self, element):
        pass

# Implementação concreta do Visitor
class ConcreteVisitor(Visitor):
    def visit_concrete_element(self, element):
        print("Visitando ConcreteElement")

# Uso do padrão Visitor
element = ConcreteElement()
visitor = ConcreteVisitor()

element.accept(visitor)
```

Neste exemplo, `ConcreteElement` é um elemento que aceita um `Visitor`. O `ConcreteVisitor` implementa a operação específica para esse elemento.

### Interpreter:

O padrão de projeto Interpreter é usado para definir uma gramática para uma linguagem e fornecer um interpretador que interpreta sentenças nessa linguagem. Ele é útil quando há uma necessidade de avaliar expressões ou interpretar uma linguagem específica.

Exemplo básico de implementação do padrão Interpreter em Python:

```python
from abc import ABC, abstractmethod

# Contexto
class Context:
    def __init__(self):
        self.variables = {}

    def get_variable(self, variable):
        return self.variables.get(variable, 0)

    def set_variable(self, variable, value):
        self.variables[variable] = value

# Expressão abstrata
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# Implementação concreta de Expressão
class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable

    def interpret(self, context):
        return context.get_variable(self.variable)

# Operação concreta
class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Uso do padrão Interpreter
context = Context()
context.set_variable("x", 10)
context.set_variable("y", 5)

expression = AddExpression(NumberExpression(VariableExpression("x")), NumberExpression(VariableExpression("y")))

result = expression.interpret(context)
print(result)  # Saída: 15
```

Neste exemplo, o `AddExpression` é uma expressão que avalia a soma de duas subexpressões (`NumberExpression` e `VariableExpression`). O `Context` fornece o contexto no qual as variáveis podem ser avaliadas.

Em resumo, enquanto o padrão Visitor é utilizado para adicionar novas operações a uma estrutura de objetos, o padrão Interpreter é utilizado para interpretar e avaliar expressões ou sentenças em uma linguagem específica. Ambos são padrões comportamentais, mas resolvem problemas diferentes.

## Memento

O padrão de projeto Memento é um padrão comportamental que fornece a capacidade de capturar e externalizar um estado interno de um objeto, permitindo que o objeto seja restaurado para esse estado em um momento posterior. O Memento permite que você salve e recupere o estado de um objeto sem revelar os detalhes de sua implementação interna.

Vamos explorar um exemplo básico de implementação do padrão Memento em Python:

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Originator
class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print(f"Originator: Definindo estado para {state}")
        self._state = state

    def create_memento(self):
        print("Originator: Criando memento")
        return Memento(self._state)

    def restore_memento(self, memento):
        print("Originator: Restaurando estado do memento")
        self._state = memento.get_state()

    def show_state(self):
        print(f"Originator: Estado atual é {self._state}")

# Caretaker
class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Caretaker: Adicionando memento à lista")
        self._mementos.append(memento)

    def get_memento(self, index):
        print("Caretaker: Obtendo memento da lista")
        return self._mementos[index]

# Uso do padrão Memento
originator = Originator()
caretaker = Caretaker()

originator.set_state("Estado 1")
originator.show_state()

caretaker.add_memento(originator.create_memento())

originator.set_state("Estado 2")
originator.show_state()

caretaker.add_memento(originator.create_memento())

originator.set_state("Estado 3")
originator.show_state()

restored_memento = caretaker.get_memento(0)
originator.restore_memento(restored_memento)
originator.show_state()
```

Neste exemplo:

- `Memento`: Armazena o estado interno do `Originator`. Pode ser acessado e modificado apenas pelo `Originator`.
- `Originator`: Mantém o estado interno e cria e restaura mementos. O estado interno é protegido por meio de encapsulamento.
- `Caretaker`: Responsável por armazenar e gerenciar mementos.

O padrão Memento é útil quando você precisa implementar a funcionalidade de desfazer/refazer, fornecer snapshots de estados para persistência ou permitir a reversão do estado de um objeto a um estado anterior. Ele ajuda a manter a coesão e a encapsular o estado interno, evitando que objetos externos acessem diretamente o estado interno do `Originator`.

## Adapter

O padrão de projeto Adapter é um padrão estrutural que permite a colaboração entre classes com interfaces incompatíveis, tornando possível que elas trabalhem juntas. O Adapter atua como uma ponte entre duas interfaces incompatíveis, convertendo a interface de uma classe em outra interface esperada pelo cliente.

Vamos explorar um exemplo básico de implementação do padrão Adapter em Python:

```python
# Interface alvo (Target)
class Target:
    def request(self):
        pass

# Classe Adaptee (a ser adaptada)
class Adaptee:
    def specific_request(self):
        return "Requisição específica do Adaptee"

# Adapter (Adaptador) que faz Adaptee trabalhar como Target
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adaptado: {self._adaptee.specific_request()}"

# Uso do padrão Adapter
adaptee = Adaptee()
adapter = Adapter(adaptee)

result = adapter.request()
print(result)  # Saída: Adaptado: Requisição específica do Adaptee
```

Neste exemplo:

- `Target`: A interface que o cliente espera.
- `Adaptee`: A classe que precisa ser adaptada para trabalhar com `Target`.
- `Adapter`: A classe que atua como um adaptador, convertendo a interface de `Adaptee` em `Target`.

O padrão Adapter é útil quando você tem uma classe existente (Adaptee) com uma interface que não é compatível com a interface desejada pelo cliente (Target). O Adapter faz a adaptação, permitindo que o cliente interaja com a classe Adaptee como se fosse uma instância do Target.

Há dois tipos comuns de adaptação: adaptação de objeto (como mostrado acima) e adaptação de classe, onde o Adapter herda da classe Adaptee. Ambas as abordagens têm seus casos de uso, dependendo das circunstâncias específicas do sistema.

## Façade

O padrão de projeto Façade é um padrão estrutural que fornece uma interface simplificada para um conjunto de interfaces em um subsistema mais amplo. O Façade define uma interface de nível mais alto que facilita o uso e a interação com o subsistema, ocultando a complexidade subjacente.

Vamos explorar um exemplo básico de implementação do padrão Façade em Python:

```python
# Subsistema complexo
class SubsystemA:
    def operation_a1(self):
        pass

    def operation_a2(self):
        pass

# Subsistema complexo
class SubsystemB:
    def operation_b1(self):
        pass

    def operation_b2(self):
        pass

# Façade
class Facade:
    def __init__(self, subsystem_a, subsystem_b):
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b

    def operation(self):
        # Utilizando métodos dos subsistemas para fornecer uma interface mais simples
        self._subsystem_a.operation_a1()
        self._subsystem_a.operation_a2()
        self._subsystem_b.operation_b1()
        self._subsystem_b.operation_b2()

# Cliente utilizando a Façade
def client_code(facade):
    facade.operation()

subsystem_a = SubsystemA()
subsystem_b = SubsystemB()

facade = Facade(subsystem_a, subsystem_b)
client_code(facade)
```

Neste exemplo:

- `SubsystemA` e `SubsystemB`: São subsistemas complexos com funcionalidades específicas.
- `Facade`: É a classe que fornece uma interface simplificada para interagir com os subsistemas. Ele coordena as ações dos subsistemas para atender a uma tarefa mais complexa.
- `client_code`: É o código do cliente que utiliza a Façade para interagir com os subsistemas de forma mais simples.

O padrão Façade é útil quando um sistema é composto por vários subsistemas complexos e o cliente precisa de uma interface mais simples para interagir com esses subsistemas. A Façade proporciona um ponto de entrada único para o cliente, ocultando a complexidade interna dos subsistemas.

Esse padrão é particularmente útil para melhorar a modularidade e manutenção do código, pois reduz a dependência do cliente em relação aos detalhes internos dos subsistemas. Ele promove um design mais desacoplado e facilita a extensão ou modificação do sistema sem afetar o código do cliente.

## Proxy

O padrão de projeto Proxy é um padrão estrutural que fornece um substituto ou representante para outro objeto a fim de controlar o acesso a ele. O Proxy atua como uma interface intermediária para controlar o acesso ao objeto real, adicionando funcionalidades adicionais, como verificação de permissões, controle de acesso, registro de solicitações, entre outros.

Vamos explorar um exemplo básico de implementação do padrão Proxy em Python:

```python
from abc import ABC, abstractmethod

# Interface do Subject
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Objeto Real
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Processando a requisição.")

# Proxy
class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # Alguma lógica adicional antes de encaminhar a requisição para o objeto real
        print("Proxy: Verificando permissões antes de encaminhar a requisição.")
        self._real_subject.request()

# Uso do padrão Proxy
real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()
```

Neste exemplo:

- `Subject`: A interface que ambos, o `RealSubject` e o `Proxy`, implementam. Isso garante que o Proxy pode ser usado onde o RealSubject é esperado.
- `RealSubject`: O objeto real que realiza a operação real.
- `Proxy`: O proxy que controla o acesso ao `RealSubject`. Ele contém uma referência ao `RealSubject` e implementa a mesma interface.

O padrão Proxy é útil quando você precisa adicionar uma camada de controle de acesso ou funcionalidades adicionais sem modificar diretamente o objeto real. Pode ser usado para realizar tarefas como verificação de permissões, caching, registro de solicitações, controle de acesso, entre outros.

Existem diferentes tipos de proxies, incluindo o Proxy Virtual (adiamento da criação de objetos caros até que sejam realmente necessários), o Proxy de Proteção (controle de acesso) e o Proxy Remoto (representante de um objeto localizado em outro espaço de endereçamento). O padrão Proxy fornece uma maneira flexível de gerenciar o acesso a objetos, adaptando-se a diferentes requisitos de controle e proteção.

## Bridge

O padrão de projeto Bridge é um padrão estrutural que separa uma abstração de sua implementação, permitindo que ambas evoluam independentemente. Isso é alcançado por meio da criação de duas hierarquias de classes independentes, uma para a abstração e outra para a implementação, e uma ponte que conecta as duas hierarquias.

Vamos explorar um exemplo básico de implementação do padrão Bridge em Python:

```python
from abc import ABC, abstractmethod

# Implementação
class Implementor(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

# Implementação concreta A
class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor A")

# Implementação concreta B
class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor B")

# Abstração
class Abstraction(ABC):
    def __init__(self, implementor):
        self._implementor = implementor

    @abstractmethod
    def operation(self):
        pass

# Abstração refinada
class RefinedAbstraction(Abstraction):
    def operation(self):
        print("Refined Abstraction")
        self._implementor.operation_implementation()

# Uso do padrão Bridge
implementor_a = ConcreteImplementorA()
implementor_b = ConcreteImplementorB()

abstraction_a = RefinedAbstraction(implementor_a)
abstraction_a.operation()
# Saída: Refined Abstraction
#        Concrete Implementor A

abstraction_b = RefinedAbstraction(implementor_b)
abstraction_b.operation()
# Saída: Refined Abstraction
#        Concrete Implementor B
```

Neste exemplo:

- `Implementor`: Define a interface para a implementação.
- `ConcreteImplementorA` e `ConcreteImplementorB`: Implementações concretas da interface `Implementor`.
- `Abstraction`: Define a interface para a abstração e mantém uma referência a um objeto `Implementor`.
- `RefinedAbstraction`: Implementa detalhes específicos da abstração.

O padrão Bridge é útil quando você deseja evitar um vínculo permanente entre uma abstração e sua implementação, permitindo que ambas possam evoluir independentemente. Ele é particularmente útil quando você tem várias variantes de uma abstração e várias implementações, e deseja evitar uma explosão combinatória de classes.

O padrão Bridge promove a flexibilidade, manutenção e extensibilidade do código, permitindo que mudanças em uma hierarquia não afetem diretamente a outra.

## Flyweight

O padrão de projeto Flyweight é um padrão estrutural que visa otimizar o uso de objetos, reduzindo a redundância quando muitos objetos semelhantes precisam ser manipulados. Ele faz isso compartilhando o estado comum entre vários objetos, em vez de replicá-lo em cada instância. O Flyweight é particularmente útil em situações em que a quantidade de objetos a serem manipulados é grande e a economia de memória é uma preocupação.

Vamos explorar um exemplo básico de implementação do padrão Flyweight em Python:

```python
class Flyweight:
    def operation(self, extrinsic_state):
        pass

# Implementação concreta de Flyweight
class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"Concrete Flyweight: {extrinsic_state}")

# Unidade de fábrica de Flyweights
class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight()
        return self._flyweights[key]

# Cliente
class Client:
    def __init__(self, factory):
        self._factory = factory
        self._flyweights = {}

    def operation(self, key, extrinsic_state):
        flyweight = self._factory.get_flyweight(key)
        flyweight.operation(extrinsic_state)
        self._flyweights[key] = flyweight

# Uso do padrão Flyweight
factory = FlyweightFactory()
client = Client(factory)

client.operation("A", 1)
# Saída: Concrete Flyweight: 1

client.operation("B", 2)
# Saída: Concrete Flyweight: 2

client.operation("A", 3)  # Reutilizando o Flyweight existente
# Saída: Concrete Flyweight: 3
```

Neste exemplo:

- `Flyweight`: Define uma interface para os objetos flyweight.
- `ConcreteFlyweight`: Implementação concreta de `Flyweight` que compartilha o estado comum.
- `FlyweightFactory`: Fábrica de flyweights que gerencia e fornece instâncias de flyweights.
- `Client`: Cliente que usa os flyweights da fábrica.

O padrão Flyweight é útil quando a aplicação usa um grande número de objetos semelhantes, e a redução do uso de memória é crítica. Ele permite compartilhar o estado comum entre várias instâncias, reduzindo assim a redundância de dados e economizando recursos.

Note que o padrão Flyweight muitas vezes envolve uma separação entre o estado intrínseco (compartilhado) e o estado extrínseco (único para cada instância). O estado intrínseco é armazenado no objeto flyweight, enquanto o estado extrínseco é passado como um parâmetro durante a operação.

## Composite

O padrão de projeto Composite é um padrão estrutural que permite que você compense objetos em estruturas de árvore para representar hierarquias parte-todo. O padrão Composite permite que clientes tratem objetos individuais e composições de objetos de maneira uniforme, simplificando assim a manipulação de hierarquias complexas.

Vamos explorar um exemplo básico de implementação do padrão Composite em Python:

```python
from abc import ABC, abstractmethod

# Componente
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Folha (Leaf)
class Leaf(Component):
    def operation(self):
        print("Leaf operation")

# Composto (Composite)
class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        print("Composite operation")
        for child in self._children:
            child.operation()

# Uso do padrão Composite
leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite.operation()
# Saída:
# Composite operation
# Leaf operation
# Leaf operation
```

Neste exemplo:

- `Component`: A interface que define as operações comuns a folhas e composites.
- `Leaf`: Uma folha, que é uma parte indivisível da hierarquia.
- `Composite`: Um composto, que contém outros componentes, seja folhas ou outros composites.

O padrão Composite é útil quando você precisa tratar objetos individuais e composições de objetos de maneira uniforme. Isso permite que clientes interajam com objetos folha e compositos de maneira consistente, sem se preocupar com a complexidade da hierarquia. É particularmente útil em situações onde você precisa representar estruturas hierárquicas parte-todo e deseja tratar todas as partes de forma homogênea.

O padrão Composite é amplamente utilizado em interfaces gráficas de usuário, manipulação de documentos, árvores de elementos DOM em HTML, entre outras situações onde a representação hierárquica é útil.

## Decorator

O padrão de projeto Decorator é um padrão estrutural que permite adicionar comportamentos adicionais a objetos individuais, de forma dinâmica e transparente, sem alterar a estrutura da classe subjacente. O Decorator é uma alternativa flexível à herança para estender funcionalidades.

Vamos explorar um exemplo básico de implementação do padrão Decorator em Python:

```python
from abc import ABC, abstractmethod

# Componente (interface ou classe abstrata)
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Implementação concreta do Componente
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Decorator abstrato
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Decorator concreto
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

# Decorator concreto
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Uso do padrão Decorator
simple_coffee = SimpleCoffee()
print("Custo do Simple Coffee:", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print("Custo do Milk Coffee:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Custo do Sugar Milk Coffee:", sugar_milk_coffee.cost())
```

Neste exemplo:

- `Coffee`: A interface (ou classe abstrata) que define o componente base.
- `SimpleCoffee`: Uma implementação concreta do componente.
- `CoffeeDecorator`: Um decorador abstrato que herda de `Coffee` e contém uma referência ao `Coffee` original.
- `MilkDecorator` e `SugarDecorator`: Implementações concretas de decoradores que estendem o comportamento do componente base.

O padrão Decorator é útil quando você precisa adicionar responsabilidades adicionais a objetos individualmente, de forma flexível e sem criar subclasses para cada combinação possível de funcionalidades. Isso permite que você componha diferentes funcionalidades de maneira dinâmica.

O Decorator é frequentemente usado em situações em que a herança não é uma opção viável ou prática para estender comportamentos, especialmente quando existem muitas combinações possíveis de funcionalidades.

# FIM!

