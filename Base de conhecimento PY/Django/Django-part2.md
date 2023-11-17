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

No Django, o sistema de URLs desempenha um papel fundamental na correspondência entre as URLs solicitadas pelos usuários e as funções ou classes de visualização que manipulam essas URLs. O arquivo principal onde as URLs são definidas é geralmente chamado de `urls.py`. Aqui está uma descrição geral do funcionamento do sistema de URLs no Django:

### Estrutura Básica:

1. **`urls.py` do Projeto:**
   - O arquivo `urls.py` no nível do projeto (na pasta principal do projeto) é responsável por mapear as URLs para os URLs dos aplicativos.

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('meu_app/', include('meu_app.urls')),  # Adiciona as URLs do aplicativo
   ]
   ```

2. **`urls.py` do Aplicativo:**
   - Cada aplicativo Django também pode ter seu próprio arquivo `urls.py`, onde as URLs específicas do aplicativo são definidas.

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('pagina/', views.pagina, name='pagina_url'),
       # Outras definições de URLs específicas do aplicativo
   ]
   ```

### Mapeamento de URLs:

- **Path():**
  - O método `path()` da biblioteca `django.urls` é frequentemente usado para mapear URLs para funções de visualização.

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('minha_url/', views.minha_funcao, name='nome_da_url'),
  ]
  ```

  - Neste exemplo, quando um usuário acessa `http://exemplo.com/minha_url/`, a função `minha_funcao` no módulo `views` será chamada para processar a solicitação.

- **Include():**
  - O método `include()` é usado para incluir as URLs de outro arquivo `urls.py`. Isso é útil para organizar o código e dividir as URLs por aplicativos.

  ```python
  from django.urls import path, include
  from . import views

  urlpatterns = [
      path('outro_app/', include('outro_app.urls')),
      # ...
  ]
  ```

- **Parâmetros na URL:**
  - É possível incluir parâmetros nas URLs, que podem ser capturados pela função de visualização.

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('pagina/<int:numero>/', views.pagina_com_parametro, name='pagina_com_parametro'),
  ]
  ```

### Nomeação de URLs:

- **`name` Parameter:**
  - A opção `name` em uma definição de URL permite nomear a URL. Isso é útil para referenciar a URL em templates ou em código Python.

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('minha_url/', views.minha_funcao, name='nome_da_url'),
  ]
  ```

### Inclusão de URLs no Projeto:

- **Incluindo URLs do Aplicativo no Projeto:**
  - Ao incluir as URLs de um aplicativo no arquivo `urls.py` do projeto, você cria uma hierarquia que permite que o Django roteie solicitações para os aplicativos corretos.

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('meu_app/', include('meu_app.urls')),  # Inclui as URLs do aplicativo
  ]
  ```

O sistema de URLs do Django oferece flexibilidade para organizar e estruturar as URLs de um aplicativo web de maneira clara e eficiente. Ele também facilita a manutenção e expansão de projetos à medida que crescem em complexidade.

## Alinhamento de URL

No Django, a organização e o alinhamento de URLs geralmente são tratados no arquivo `urls.py` de cada aplicativo, bem como no arquivo `urls.py` do projeto. Aqui estão algumas práticas comuns para organizar e alinhar URLs de maneira clara e legível:

1. **Indentação e Alinhamento:**
   - Use uma indentação consistente para tornar o código fácil de ler. Normalmente, uma indentação de 4 espaços é preferida, mas pode variar dependendo das preferências da equipe.

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('url1/', views.view1, name='name1'),
       path('url2/', views.view2, name='name2'),
       path('url3/', views.view3, name='name3'),
   ]
   ```

2. **Quebras de Linha:**
   - Se a lista de URLs estiver ficando muito longa, considere usar quebras de linha para tornar o código mais legível.

   ```python
   urlpatterns = [
       path('url1/', views.view1, name='name1'),
       path('url2/', views.view2, name='name2'),
       path('url3/', views.view3, name='name3'),
       # ... muitas outras URLs ...
   ]
   ```

3. **Uso de `include`:**
   - Ao usar o `include` para incluir URLs de outros aplicativos, você pode manter as definições de URLs do aplicativo alinhadas.

   ```python
   from django.urls import path, include
   from . import views

   urlpatterns = [
       path('app1/', include('app1.urls')),
       path('app2/', include('app2.urls')),
       # ...
   ]
   ```

4. **Uso de Grupos de URLs (`path()` ou `re_path()`):**
   - À medida que sua aplicação cresce, você pode começar a usar grupos de URLs para organizar ainda mais seu código. Isso pode ajudar a manter as URLs relacionadas alinhadas.

   ```python
   from django.urls import path, re_path
   from . import views

   urlpatterns = [
       path('group1/', [
           path('url1/', views.view1, name='name1'),
           path('url2/', views.view2, name='name2'),
       ]),
       re_path(r'^group2/(?P<param>\d+)/$', views.group2_view, name='group2_name'),
       # ...
   ]
   ```

5. **Comentários:**
   - Adicione comentários conforme necessário para documentar a finalidade de grupos de URLs ou URLs individuais.

   ```python
   urlpatterns = [
       path('url1/', views.view1, name='name1'),  # Esta URL faz algo específico
       # ...
   ]
   ```

Lembre-se de que a clareza e a legibilidade são fundamentais. Escolha um estilo que faça sentido para você e sua equipe, mantenha a consistência e ajuste conforme necessário à medida que o projeto evolui. O objetivo é garantir que outros desenvolvedores (e você mesmo no futuro) possam entender facilmente a estrutura de URLs do seu aplicativo.
