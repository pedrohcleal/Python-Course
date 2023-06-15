#0,1,1,2,3,4,8,13,21

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end =',')
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo
    print("finish")


if __name__ == '__main__':
    fibonacci(10000)