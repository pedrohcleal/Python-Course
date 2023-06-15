from math import  pi

def circulo(raio): #definir uma função   ##receber raio
    return pi * float(raio) ** 2        ##retorna area e registra esse valor

if __name__ == '__main__': #se o nome do bloco atual for main execute...
    raio = float(input('informe o raio: '))
    area = circulo(raio)
    print('area do circulo', area)

