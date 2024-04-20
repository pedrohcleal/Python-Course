"""Pedro Henrique Carlos Leal - 819224064
Marcos Paulo Ribeiro Gonçalves 819214887
Leonardo Aprigio Ferreira - 82017722
Gustavo Henrique da Silva Azzolino - 8222240275
Mauricio Souza Mendonça - 81922250
Enzo Gomes Garcia Lampi - 819224721
Guilherme de Oliveira Bento - 822144977
Nathaly Costa - 82115630"""

import pandas as pd 

def verificarMediana(data):
    lista = []
    for index, row in data.iterrows():
        lista.append(row[1])
        print(f"Conteúdo da linha {index}, row[0]:", row[0], " row[1]: ", row[1])
    
    lista.sort()
    lenList = len(lista)
    
    if lenList % 2 == 0:
        IndexMid = int(lenList/2)-1 #indíce do meio na lista
        mediana = sum(lista[IndexMid:IndexMid + 2])/2
        return f"Mediana = {mediana}"
    else:
        return f"Mediana = {lista[round(lenList/2)]}"
    
def verificarModa(data):
    DictData = {}
    for index, row in data.iterrows():
        DictData[row[0]] = row[1] 
        #dict_items([(0, 47), (1, 29), (2, 13), (3, 8), (4, 13)])
    moda = []
    maior_contagem = max(DictData.values()) 
    for index, value in DictData.items(): #item = nª, freq = freq do nª // Verificar as modas
        if value == maior_contagem:
            moda.append(index)
    print(DictData.items())
    return f"a moda da tabela é: {moda}"

if __name__ == "__main__":
    df = pd.read_excel('alunos.xlsx', sheet_name='Sheet1')
    print(verificarModa(df))
    #print(verificarMediana(df))
