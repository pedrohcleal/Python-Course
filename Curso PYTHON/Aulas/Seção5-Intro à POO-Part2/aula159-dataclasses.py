# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass
from dataclasses import dataclass, field
#from dataclasses import fields -> retornar funções da dataclasses disponiveis

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)