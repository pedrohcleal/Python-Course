from decimal import Decimal, getcontext

a = 10

getcontext().prec = 4 #máximo de 4 decimais(regra geral) (precisão)
print(Decimal(1) / Decimal(7)) #em float a conta dá um erro binário
print(Decimal.max(Decimal(1), Decimal(7))) #retorna o maior valor
dir(Decimal) #mostra as opções

getcontext().prec = 10
print(1.1 + 2.2) #  =3.300...3
print(Decimal(1.1) + Decimal(2.2)) #  =3.300





