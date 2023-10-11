import csv

with open('1-pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('nome: {} idade {}'.format(*pessoa))