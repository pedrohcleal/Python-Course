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
