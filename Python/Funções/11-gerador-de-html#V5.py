#GERADOR DE HTML 1.0  #errado
def get_atrs(informados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'   #separa a string por _  ,transforma em dici e escolhe o primeiro elemento([-1])
                    for k, v in informados.items()




def tag_bloco(conteudo, *args, classe = 'sucess', inLine= False, **novos_atrs):   #args = propriedas que vc aplicar cacso seja calleble
    tag = 'span' if inLine else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    atributos = get_atrs(novos_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'

def tag_lista(*itens, **novos_atrs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)    #join --> concatenação com essa string vazia a cada novo valor
    return f'<ul {get_atrs(novos_atrs)} >{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print((tag_bloco('inline e classe',classe='info', True)))
    print(tag_bloco('inline',inLine=True)) #pulou o parametro ao definir Inline
    print(tag_bloco('falou',classe='erro'))
    print(tag_bloco('inline', inLine=False))
    print(tag_bloco(inLine=True, conteudo='inLine'))
    print(tag_bloco(tag_lista('item 1','item 2'), classe='info'))
    print((tag_bloco(tag_lista(, 'sabado', 'domingo', classe='info'))))

    print(tag_bloco(tag_lista, 'item1', 'item2', classe='info',bloco_acesskey= 'm', bloco_id = 'conteudo', ul_id='lista')