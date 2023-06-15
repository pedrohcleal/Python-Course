""""
Operados lógicos
and (e) or (ou) not(não)
and -> Todas as condições precisam ser verdadeiras e 
se qualquer valor for considerado falso, a
expressão inteira será avaliada naquele valor
-> São considerados falsy(que vc já viu)
> 0 - 0.0 - '' - Fakse
-> Também existeo  o tipo None que é usado para
representar um "não valor"

"""
 
entrada = input('[E]entrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = "123456"

if entrada == 'E','e' and senha_digitada == senha_permitida:
    (print('entrar'))

else:
    (print('sair'))