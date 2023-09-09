#while True:
#    print('vai demorar muito, laço infinito')

from random import randint

numero_informado = -1
numero_secreto = randint(0,9)   ##// radint atribui um numero aleatorio de 0 a 9

while numero_informado != numero_secreto:
    numero_informado = int(input('informa o numero: '))

print('numero secreto {} foi encontrado!'.format(numero_secreto))
