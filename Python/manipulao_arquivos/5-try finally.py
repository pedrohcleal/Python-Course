arquivo =  open('1-pessoas.csv')

try:
    arquivo = open('1-pessoas.csv')
    for registro in arquivo:
        print('nome: {} Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()
    print("finnally")

if arquivo.closed():
    print('arquivo fechado')

#strip apaga os espaços da borda
#.close serve para fechar o arquivo

#sem o *registro, a condição for não será feita e nem a linha 6

#com a condição tray ele tenta e se n der certo ele vai para o finnaly e o arquivo é fechado

