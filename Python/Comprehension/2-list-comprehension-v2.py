# [ espressão for item in list if condincional ]

dobros_dos_pares = [i *2 for i in range(10) if i % 2 == 0]
print(dobros_dos_pares)

#versao 'normal'

dobros_dos_pares = []

for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i*2)

print(dobros_dos_pares)