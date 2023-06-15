#colocar uma entrada que aceite apenas sim ou não para jogar dados.

import random

cond = bool(input("Deseja jogar?"))

while cond == "sim":
    print(random.randrange(1, 6))

while cond != 'não':
    cond = (input("Digite sim ou não: "))

if cond == "sim":
    print(random.randrange(1,6))

if cond == "não":
    print('volte sempre')

