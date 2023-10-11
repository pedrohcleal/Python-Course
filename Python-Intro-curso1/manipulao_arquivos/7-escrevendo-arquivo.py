arquivo =  open('1-pessoas.csv')

with open('1-pessoas.csv',) as arquivo:
    with open('1-pessoas.txt','w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('nome: {} Idade: {}'.format(*pessoa), file = saida)


if arquivo.closed:
    print('arquivo fechado')
if saida.close():
    print('arquivo de saida foi fechado')
#le o arquivo csv e escreve o arquivo txt