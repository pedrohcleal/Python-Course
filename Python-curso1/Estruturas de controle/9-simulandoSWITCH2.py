def get_tipo_dia(dia):
    dias = {
        1: 'fim de semana',
        2: 'dia de semana',
        3: 'dia de semana',
        4: 'dia de semana',
        5: 'dia de semana',
        6: 'dia de semana',
        7: 'fim de semana',
    }
    return dias.get(dia, 'inváido')

if __name__ == '__main__':
    for dia in range (0,9):
        print("{}:{}".format(dia,get_tipo_dia(dia)))