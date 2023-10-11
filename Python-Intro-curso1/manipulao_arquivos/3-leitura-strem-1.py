arquivo =  open('1-pessoas.csv')

for registro in arquivo:
    print('nome: {} Idade: {}'.format(*registro.split(',')))

arquivo.close()