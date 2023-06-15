produto = {'nome': 'Caneta chic', 'preco': 14.99, 'importada': True, 'estoque': 793}


for chave in produto.keys():
    print(chave)


for valor in produto.values():
    print(valor)


for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave,valor) ##estao visiveis fora do laço