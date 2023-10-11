from math import  pi

def circulo(raio): #definir uma função
    print('area do cirtuclo: ', pi * float(raio) ** 2)

if __name__ == '__main__': #se o nome do bloco atual for main execute...
    raio = float(input('informe o raio: '))
    circulo(raio)

