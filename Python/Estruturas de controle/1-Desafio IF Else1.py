def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota inválida'


if __name__ == '__main__':
    valor_informado = input('nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
