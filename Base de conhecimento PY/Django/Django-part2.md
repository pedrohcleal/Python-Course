# Django part 2

## Status HTTP

No Django, os códigos de status de respostas HTTP são usados ​​para indicar o status de uma resposta HTTP. Eles são um componente importante da comunicação entre o cliente e o servidor, pois fornecem informações sobre o sucesso ou o fracasso de uma solicitação.

O Django fornece um número de classes para representar os códigos de status HTTP. Essas classes são derivadas da classe `HttpResponse`, que é a classe base para todas as respostas HTTP no Django.

**Códigos de status informativos (100-199)**

Os códigos de status informativos são usados ​​para indicar que a solicitação foi recebida e entendida pelo servidor. Eles não indicam necessariamente que a solicitação foi processada com sucesso.

Os códigos de status informativos mais comuns são:

* `100 Continue`: O servidor recebeu a primeira parte da solicitação e está esperando o restante.
* `101 Switching Protocols`: O servidor está mudando para um protocolo diferente.
* `102 Processing`: A solicitação está sendo processada.

**Códigos de status bem-sucedidos (200-299)**

Os códigos de status bem-sucedidos são usados ​​para indicar que a solicitação foi processada com sucesso.

Os códigos de status bem-sucedidos mais comuns são:

* `200 OK`: A solicitação foi processada com sucesso e a resposta contém o conteúdo solicitado.
* `201 Created`: Um novo recurso foi criado com sucesso.
* `202 Accepted`: A solicitação foi aceita e será processada posteriormente.

**Códigos de status de redirecionamento (300-399)**

Os códigos de status de redirecionamento são usados ​​para indicar que o cliente deve redirecionar sua solicitação para outro recurso.

Os códigos de status de redirecionamento mais comuns são:

* `301 Moved Permanently`: O recurso foi movido permanentemente para outro URI.
* `302 Found`: O recurso foi movido temporariamente para outro URI.
* `303 See Other`: O cliente deve enviar uma nova solicitação GET para o URI especificado.

**Códigos de status de erro do cliente (400-499)**

Os códigos de status de erro do cliente são usados ​​para indicar que a solicitação foi malformada ou contém um erro.

Os códigos de status de erro do cliente mais comuns são:

* `400 Bad Request`: A solicitação é malformada ou não pode ser entendida.
* `401 Unauthorized`: O cliente não está autorizado a acessar o recurso.
* `403 Forbidden`: O cliente está autorizado a acessar o recurso, mas não tem permissão para fazê-lo.

**Códigos de status de erro do servidor (500-599)**

Os códigos de status de erro do servidor são usados ​​para indicar que o servidor encontrou um erro ao processar a solicitação.

Os códigos de status de erro do servidor mais comuns são:

* `500 Internal Server Error`: O servidor encontrou um erro interno.
* `501 Not Implemented`: O servidor não implementa o recurso solicitado.
* `502 Bad Gateway`: O servidor intermediário não pôde processar a solicitação.

No Django, os códigos de status de respostas HTTP podem ser especificados usando o método `status_code` da classe `HttpResponse`. Por exemplo, o seguinte código retorna uma resposta com o código de status `200 OK`:

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse(status_code=200)
```

Os códigos de status de respostas HTTP também podem ser especificados usando o método `HttpResponseRedirect`. Por exemplo, o seguinte código redireciona o cliente para a URL `/other-page/`:

```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/other-page/')
```

É importante usar os códigos de status de respostas HTTP corretamente para fornecer informações úteis aos clientes e servidores.

## URLs

No Django, as URLs são usadas para mapear URLs para vistas. Elas são definidas no arquivo `urls.py` do seu projeto Django.

O arquivo `urls.py` contém uma lista de padrões de URLs. Cada padrão de URL consiste em uma expressão regular e uma função de visualização. Quando um cliente solicita uma URL, o Django compara a URL com os padrões de URLs. Se uma correspondência for encontrada, a função de visualização correspondente é chamada.

**Expressões regulares**

As expressões regulares são usadas para definir o formato das URLs que devem corresponder a um padrão. Elas são uma forma poderosa de definir padrões complexos.

Para obter mais informações sobre expressões regulares, consulte a documentação do Python.

**Funções de visualização**

As funções de visualização são usadas para gerar a resposta para uma solicitação de URL. Elas são funções Python que recebem um objeto `HttpRequest` como entrada e retornam um objeto `HttpResponse` como saída.

Para obter mais informações sobre funções de visualização, consulte a documentação do Django.

**Exemplos de URLs**

Aqui estão alguns exemplos de URLs que podem ser definidas no Django:

```python
# URL para a página inicial
path('', views.home, name='home')

# URL para a página de contato
path('contato/', views.contato, name='contato')

# URL para a página de listagem de produtos
path('produtos/', views.produtos_list, name='produtos')

# URL para a página de detalhes de um produto
path('produtos/<int:produto_id>/', views.produto_details, name='produto_details')
```

No primeiro exemplo, a URL `/` é mapeada para a função de visualização `home`. Esta função de visualização é responsável por gerar a página inicial do site.

No segundo exemplo, a URL `/contato/` é mapeada para a função de visualização `contato`. Esta função de visualização é responsável por gerar a página de contato do site.

No terceiro exemplo, a URL `/produtos/` é mapeada para a função de visualização `produtos_list`. Esta função de visualização é responsável por gerar uma lista de produtos.

No quarto exemplo, a URL `/produtos/<int:produto_id>/` é mapeada para a função de visualização `produto_details`. Esta função de visualização é responsável por gerar os detalhes de um produto específico.

**Separando as URLs em arquivos diferentes**

Se o seu projeto Django for grande, você pode querer separar as URLs em arquivos diferentes. Isso pode tornar o código mais organizado e fácil de manter.

Para fazer isso, você pode criar um arquivo `urls.py` para cada aplicação do seu projeto. Em seguida, você pode importar os arquivos `urls.py` das aplicações em seu arquivo `urls.py` principal.

**Exemplo**

Aqui está um exemplo de como separar as URLs em arquivos diferentes:

```python
# urls.py principal

from django.urls import include, path

from core import urls as core_urls
from produtos import urls as produtos_urls

urlpatterns = [
    path('', include(core_urls)),
    path('produtos/', include(produtos_urls)),
]

# core/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# produtos/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.produtos_list, name='produtos'),
    path('<int:produto_id>/', views.produto_details, name='produto_details'),
]
```

Neste exemplo, o arquivo `urls.py` principal importa os arquivos `urls.py` das aplicações `core` e `produtos`. O arquivo `core/urls.py` contém as URLs para a página inicial do site. O arquivo `produtos/urls.py` contém as URLs para a listagem e os detalhes de produtos.

