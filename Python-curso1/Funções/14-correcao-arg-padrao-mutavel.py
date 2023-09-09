def fibonacci(sequencia=None):
    #uso de mutaveis com o valor dafault(armadilha)
    sequencia = sequencia or [0,1] ##se retornar none então é 0,1
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0,1,1]