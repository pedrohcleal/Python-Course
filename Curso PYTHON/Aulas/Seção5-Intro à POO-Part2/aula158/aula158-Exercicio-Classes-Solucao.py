
class Conta(Banco):
    def __init__(self) -> None:
        pass

    def sacar(self, valor):
        pass

class Pessoa(Banco):
    def __init__(self):
        pass

class Banco:
    def __init__(self) -> None:
        pass

class Cliente(Pessoa):
    def __init__(self):
        super().__init__()
        self._nome = ''
        self._idade = ''


class ContaPoupanca(Conta):
    def __init__(self) -> None:
        super().__init__()
        self.extralimit = 450
        self.agencia = 0
        self.numeroCP = 0
        self.saldo = 0 
    
    def depositar(self, valor):
        self.saldo += valor
        return print("saldo adicionado de = ", valor) 


class ContaCorrente(Conta):
    def __init__(self) -> None:
        super().__init__()
        self.extralimit = 450
        self.agencia = 0
        self.numeroCP = 0
        self.saldo = 0 

    def depositar(self, valor):
        self.saldo += valor
        return print("saldo adicionado de = ", valor) 

