from math import  pi
import sys #já manda o input via linha de comando
def circulo(raio): #definir uma função   ##receber raio
    return pi * float(raio) ** 2        ##retorna area e registra esse valor

if __name__ == '__main__': #se o nome do bloco atual for main execute...
    if len(sys.argv) < 2: #len = calcular tamanho de lista
        print("""\
        É necessário informar o raio do círculo.
        Sintaxe correta: {} <raio>""".format(sys.argv[0][67:]))
        #sys.argv[0] é uma string
        #[67:] revela do 67º elemento até o fim da string
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('area do circulo', area)

