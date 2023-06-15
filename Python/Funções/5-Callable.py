def executar(funcao):   #uma função pra executar uma função
    if callable(funcao):   #callable = é uma função ? true or false
        funcao()

def bom_dia():
    print('bomdia')

if __name__ == '__main__':
    executar(bom_dia)

