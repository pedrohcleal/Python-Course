PALAVRAS_PROIBIDAS = ('futebol','religião','politíca') #por convenção é variável ser letra maiuscula
textos [
    'joão gosta de futebol e política',
    'a praia foi divertida',
]
for frases in textos
    found = False #se nao tiver palavra o valor vai ser false para *frases*
    for palavra in frases.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('texto possui ao menos uma palavra proibida', palavra)
            found = True
            break
    if not found:
        print('texto autorizado', texto)