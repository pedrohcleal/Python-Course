dicionario = {i: i*2 for i in range(10) if i % 2 == 0}

#apenas numero pares, de acordo com condicional

print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')



