"""Pedro Henrique Carlos Leal - 819224064
Marcos Paulo Ribeiro Gonçalves 819214887
Leonardo Aprigio Ferreira - 82017722
Gustavo Henrique da Silva Azzolino - 8222240275
Mauricio Souza Mendonça - 81922250
Enzo Gomes Garcia Lampi - 819224721
Guilherme de Oliveira Bento - 822144977
Nathaly Costa - 82115630"""

import pandas as pd 

def tedenciaCentral(date):
    listaDados = []
    for index, row in date.iterrows():
        listaDados.append(row[1])
        #print(f"Conteúdo da linha {index}, row[0]:", row[0], " row[1]: ", row[1])
    listaDados.sort()
    return f"""a média dos dados é: {sum(listaDados) / len(listaDados)},
mediana dos dados é {mediana(listaDados)}, 
a moda dos dados é {moda(listaDados)} """

def mediana(lista):
    if len(lista) % 2 == 0:
        IndexMid = int(len(lista)/2)-1 #indíce do meio na lista
        soma = sum(lista[IndexMid:IndexMid+2]) /2
        return soma
    else:
        return lista[round(len(lista)/2)]

def moda(lista):
    contagem = {}
    for item in lista:
        contagem[item] = lista.count(item)
    # contagem = ([(0, 47), (1, 29), (2, 13), (3, 8), (4, 13)])
    moda = []
    maior_contagem = max(contagem.values())
    for item, freq in contagem.items(): #item = nª, freq = freq do nª // Verifica as Modas
        if freq == maior_contagem:
            moda.append(item)

    return moda

if __name__ == "__main__" :
    df = pd.read_excel('exportadores.xlsx', sheet_name='Sheet1')
    print(tedenciaCentral(df))
