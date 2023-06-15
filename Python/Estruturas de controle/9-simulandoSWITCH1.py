def get_dia_semana(dia):
    dias = {
        1: 'domingo',
        2:'terça',
        3:'quarta',
        4: 'quinta',
        5: 'sexta',
        6: 'sab',
        7: 'segunda',
    }
    return dias.get(dia, 'inválido') ##

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')

##SWITCH SIMULADO