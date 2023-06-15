#GERADOR DE HTML 1.0

def tag_bloco(conteudo, *args, classe = 'sucess', inLine= False):   #args = propriedas que vc aplicar cacso seja calleble
    tag = 'span' if inLine else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)    #join --> concatenação com essa string vazia a cada novo valor
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print((tag_bloco('inline e classe',classe='info', True)))
    print(tag_bloco('inline',inLine=True)) #pulou o parametro ao definir Inline
    print(tag_bloco('falou',classe='erro'))
    print(tag_bloco('inline', inLine=False))
    print(tag_bloco(inLine=True, conteudo='inLine'))
    print(tag_bloco(tag_lista('item 1','item 2'), classe='info'))
    print((tag_bloco(tag_lista(, 'sabado', 'domingo', classe='info'))))

