import time

import pandas as pd

def test_iloc(data):
    for pos in range(len(df)):
        linha_dado0 = df.iloc[pos][1]
        linha_dado1 = df.iloc[pos][1]
        print(f"Conteúdo da linha {pos}, \nrow[0]: {linha_dado0} row[1]: {linha_dado1}")

def test_iter(data):
    for index, row in data.iterrows():
        print(f"Conteúdo da linha {index}, \nrow[0]: {row[0]} row[1]: {row[1]}")


if __name__ == "__main__":
    df = pd.read_excel('example.xlsx', sheet_name='Sheet1')
    test_iloc(df)
    #test_iter(df)