pessoa = {'nome':'Prof Alberto','idade':48, 'cursos':['React','Python']}

pessoa['idade'] = 44 #mudou o item da chave
print(pessoa)

pessoa['cursos'].append('Angular') #adicionou mais um item a chave
print(pessoa)

print(pessoa.pop('idade')) #retorna o item da chave e dps anula a própria chave
print(pessoa)

pessoa.update({'idade':40,'sexo':'M'}) #adiciona mais chaves e items no dicionario'pessoa'
print(pessoa)

print(pessoa.clear()) #limpa todos o itens

