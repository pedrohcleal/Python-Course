def faixa_etaria(idade):
    if 0 < idade < 18:
        return 'menor de idadade'
    elif idade in range(18,65):
        return 'adulto'
    elif idade in range(65,100):
        return 'melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'

if __name__ == '__main__':
    for idade in (17,35,87,113,-2):
        print(f'{idade} : {faixa_etaria(idade)}')

