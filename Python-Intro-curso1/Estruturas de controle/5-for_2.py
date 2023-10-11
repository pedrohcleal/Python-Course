##percorrer coisas

palavra = 'cubo'

for letra in palavra:
    print(letra, end=",") #o final de cada print vai ser vírgula e na mesma linha
print('fim')

aprovados = ['rafael','pedro','renato','maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao +1}', nome)

dias_semana = ('domingo', 'Segunda', 'Terça', 'Quarta','quinta','sexta')

for dia in dias_semana:
    print(f'hoje é {dia}')

for numero in {1,2,3,4,5,6}:
    print(numero)