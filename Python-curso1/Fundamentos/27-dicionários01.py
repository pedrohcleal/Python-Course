#DICIONARIOSS RS
pessoa = {'nome':'prof Ana','idade':38,'cursos':['ingles','portugues']}

print(type(pessoa))

print(len(pessoa))  #mostra a quantidade de chaves no dic.

print(pessoa['nome']) #acessa

print(pessoa['cursos'][1])

print(pessoa.keys())      #chaves dos valores
print(pessoa.values())     #valores do dir
print(pessoa.items())       #todos os itens das chaves
print(pessoa.get('idade'))   #retorna o item da idade
print(pessoa.get('tags', [])) #caso n exista retorna default

