def fibonacci(sequencia=[0,1]):
    #uso de mutaveis com o valor dafault(armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))