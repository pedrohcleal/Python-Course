class potencia:
    #calcula potencia de numeros
    def __init__(self, expoente):
        self.expoente = expoente

    #def __call__(self, *args, **kwargs):
    def __call__(self, base):
        return base ** self.expoente

if __name__ == '__main__':
    quadrado = potencia(2)
    cubo = potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f"3² => {quadrado(3)}")
        print(f"5³ => {cubo(5)}")
        
        print(potencia(4)(2))