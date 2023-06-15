from math import  pi
import sys #já manda o input via linha de comando
def circulo(raio): #definir uma função   ##receber raio
    return pi * float(raio) ** 2        ##retorna area e registra esse valor

if __name__ == '__main__': #se o nome do bloco atual for main execute...
    print(sys.argv[1])   #argv vai ter todos os argumentos passados para o script via linha de comando
    raio = sys.argv[1]
    area = circulo(raio)
    print('area do circulo', area)


#sys.argv[0] é o nome do arquivo no systema
#sys.argv[1] é o primeiro argumento dps do nome do arqvo do sys
