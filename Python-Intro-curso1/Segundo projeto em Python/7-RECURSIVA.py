def imprimir(maximo,atual)  :
    if atual >= maximo :
        return True
    print(atual)
    imprimir(maximo, atual + 1)

imprimir(99,1)


## FUNÇÃO RECURSIVA, POIS CHAMA A ELA MESMA, PRESTAR ATENÇÃO NA CONDIÇÕES DE PARADA


