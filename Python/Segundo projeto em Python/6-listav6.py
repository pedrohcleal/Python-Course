#0,1,1,2,3,4,8,13,21

def fibonacci(quantidade):
    resultado = [0,1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:])) ##append add a lista
    return  resultado



if __name__ == '__main__':
    #listar os 20 primeiros números da sequencia
    for fib in fibonacci(10):
        print(fib)