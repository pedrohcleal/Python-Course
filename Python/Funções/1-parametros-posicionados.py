#GERADOR DE HTML 1.0

def tag_bloco(texto, classe = 'sucess'):   #precisa do texto, classe é opcional pq tem como padrção sucess
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    #teste (assertions), se o retorno for diferente do abaixo, dá erro(assertionerror)
    assert tag_bloco('incluido com sucesso!') == \
        '<div class="sucess">incluido com sucesso!</div>'
    assert tag_bloco('impossivel excluir', 'erro') == \
        '<div class="erro">impossivel excluir</div>'
    print(tag_bloco('impossivel excluir','erro'))