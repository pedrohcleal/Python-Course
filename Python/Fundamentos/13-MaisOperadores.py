#operador de membro

lista = [1,2,3,'ana','carla']
print(2 in lista)
print('ana' not in lista)

#operador de identidade

x = 3
y = x
z = 3
print(x is y) #True
print(y is z) #false
print(x is not z) #true

lista_a = [1,2,3]
lista_b = lista_a   #aponta pra mesma mémoria da lista a
lista_c = [1,2,3]   #é outra mémoria alocada

print(lista_a is lista_b) #true
print(lista_b is lista_c) #false
print(lista_a is not lista_c) #true
