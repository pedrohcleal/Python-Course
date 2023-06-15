arquivo =  open('1-pessoas.csv')

with open('1-pessoas.csv') as arquivo:
    for registro in arquivo:
        print('nome: {} Idade: {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print('arquivo fechado')

#"with" excelente opção para garantir q o arquivo foi fechado, e recursos do sistema operacional
#strip apaga os espaços da borda