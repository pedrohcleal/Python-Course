lista = []

print(dir(lista))
print(type(lista))

lista.append(1) #adiciona itens a lista
lista.append(5)

print(lista)

nova_lista = [1,5,'ana','bia']

print(nova_lista)

nova_lista.remove(5)  #remove o item 5 e não o indice 5

print(nova_lista)

nova_lista.reverse() #inverter a lista

print(nova_lista)

print(len(nova_lista)) #quantidade de itens na lista

