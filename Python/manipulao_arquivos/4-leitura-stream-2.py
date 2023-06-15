arquivo =  open('1-pessoas.csv')

for registro in arquivo:
    print('nome: {} Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()

#strip apaga os espaços da borda
#.close serve para 