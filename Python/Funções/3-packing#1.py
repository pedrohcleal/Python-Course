def soma_2(a,b):
    return a+b

def soma_3(a,b,c):
    return a+b+c
def soma_n(*numeros):                 #numeros vai ser uma tupla
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n            #acrescenta ao valor de omsa
    return soma

if __name__ == '__main__':
    print(soma_2(2,3))
    print(soma_3(2,4,6))
    print(soma_n(1))
    print(soma_n(11,2,3,4,5,434,23,))

    tupla_nums = (1,2,3)
    print(soma_3(*tupla_numsnums)) ##nums vai ir para a func soma_3, = 1+2+3 = 6

    lista_nums= [1,2,3]
    print(soma_3(*lista_nums))