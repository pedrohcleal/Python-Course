def zeros(n):
    contador = 0
    soma = 1
    soma = [i for i in range(1,n+1)]

    for x in str(soma)[::-1]:
        if x == '0':
            contador += 1
        else: break
    return contador

print(zeros(6))