arquivo = open('1-pessoas.csv')

dados = arquivo.read()

arquivo.close()

for registro in dados.splitlines():
    print('nome:{}, idade:{}'.format(*registro.split(','))) ##quebrar o registro em linhas

##o asterisco serve pra dizer q é um argumento variável



