def fibonacci(quantidade, sequencia = (0,1)):
    #imporante: condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    #listar os 20 primeiros númeors dasequeência
    for fib in fibonacci(20):
        print(fib)