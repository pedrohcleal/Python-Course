PALAVRAS_PROIBIDAS = {'futebol','religião','politíca'} #{}determina o set
textos = [
    'joão gosta de futebol e política',
    'a praia foi divertida',
    ]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("texto possui palavras proibidas:", intersecao)
    else:
        print('texto autorizado',texto)