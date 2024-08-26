primeiro_valor = input('digite um valor:')

segundo_valor = input('digite outro valor:')

if primeiro_valor == segundo_valor:
    print('ambos os valores são iguais')

elif primeiro_valor > segundo_valor:
    print('o  valor: {} é maior que{}'.format(primeiro_valor,segundo_valor))

elif segundo_valor > primeiro_valor:
    print('o valor: {} é maior que{}'.format(segundo_valor,primeiro_valor))
