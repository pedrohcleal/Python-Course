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
