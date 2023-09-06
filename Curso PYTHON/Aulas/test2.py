import numpy as np
def zeros(n):
    
    contador = 0
    soma = np.math.factorial(n)

    for x in str(soma)[::-1]:
        if x == '0':
            contador += 1
        else: break
    return contador


print(zeros(6))