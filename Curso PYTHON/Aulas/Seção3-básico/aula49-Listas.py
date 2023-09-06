"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#sequencia de acesso a list:
#---------[0, 1, 2]

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
print(lista_b)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a1 = ['Luiz', 'Maria', 1, True, 1.2]
lista_b1 = lista_a.copy()

lista_a1[0] = 'Qualquer coisa'
print(lista_a1)
print(lista_b1)

"""
for in com listas
"""
lista2 = ['Maria', 'Helena', 'Luiz']

for nome in lista2:
    print(nome, type(nome))