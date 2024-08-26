#operadores in e not in
#Strings são iteráveis
# 0 1 2 3 4 5 6
# o t á v i o
# 6 5 4 3 2 1 0

nome = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

print(nome[2])
print(nome[-4])
print('a' in nome)
print('z' in nome)
print("ot" not in nome )

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')