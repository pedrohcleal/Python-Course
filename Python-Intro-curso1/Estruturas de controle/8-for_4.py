#for i in range(1, 10):
#    if i==6:
#        break
#    print(i) ##else n será encontrado caso tenha break
#else:
#    print('fim!')

#sortear numeros entre 1 e 6
#for pra percorrer de 1 a 6
    #se for par e for igual ao numero sorteado
    #imprimir "acertou" e break
# se não acertar chamar o else.. imprimir frase "não acertou"

from random import randint

for i in range(1,7):
    numero_secreto = randint(0, 9) #radint atribui um numero aleatorio de 0 a 9
    if i % 2 == 0 and i == numero_secreto:
        print('acertou miseravi, o número é {} e a sequencia do i é {}'.format(numero_secreto,i))
        break  #o else não será executado
    else:
        print('não acertou o nº {}'.format(numero_secreto))


