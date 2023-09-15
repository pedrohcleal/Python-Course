# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self,nome):
        self.nome = nome
         
        self.fabricate = Fabricante()

    def motor(self,nome):
        self.motor = Motor() 

    def visualizar(self, nome, motor):
        print(self.motor,self.nome,self.fabricate)

class Motor:
    def __init__(self,nome):
        self.nome = nome
    
    def adicionar_motor(self, nome):
        self.nome += nome


class Fabricante:
    def __init__(self,nome):
        self.nome = nome
    def adicionar_fabricante(self,nome):
        self.nome += nome 


fusca = Carro
fusca.motor.adicionar_motor('V2')
fusca.fabricate.adicionar_fabricante('Ford')



