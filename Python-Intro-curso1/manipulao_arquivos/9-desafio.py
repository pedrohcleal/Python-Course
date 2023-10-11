import csv

from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print('baixando csv')
        dados = entrada.read().decode('latin')
        print('download oompleto')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}:{cidade[3]}')

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')