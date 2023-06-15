def todos_params(*args, **kwargs):   #voce quer pegar todos argumentos posicionais e nomeados  <==
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

if __name__ == '__main__':
    todos_params('a','b','c')  #posições
    todos_params(1,2,3, legal = True, valor = 12.99) #imprime as posições e dps os valores
    todos_params('ana', False, [1,2,3], tamanho = 'm', fragil = False)   #kwargs mostra os dics
    todos_params('maria', primeiro = 'joao')
