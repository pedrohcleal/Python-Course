# **kwargs == argumentos nomeados keyword args

def resultad_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

if __name__ == '__main__':
    resultad_f1(primeiro='hamilton',
                segundo = 'vestapen',
                terceiro= 'vettel')

