#GERADOR DE HTML 1.0

def tag_bloco(texto, classe = 'sucess', inLine= False):   #precisa do texto, classe é opcional pq tem como padrção sucess
    tag = 'span' if inLine else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print((tag_bloco('inline e classe','info', True)))
    print(tag_bloco('inline',inLine=True)) #pulou o parametro ao definir Inline
    print(tag_bloco('falou',classe='erro'))
    print(tag_bloco('inline', inLine=False))