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
