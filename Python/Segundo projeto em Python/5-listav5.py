#0,1,1,2,3,4,8,13,21

def fibonacci(limite):
    resultado = [0,1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1]) ##append add a lista
    return resultado
    print("finish")
        

if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)