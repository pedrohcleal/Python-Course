# Django part4

## Problemas no hardcoded

"Hardcoded" é um termo utilizado na programação para descrever a prática de incluir valores ou referências diretamente no código-fonte, em vez de utilizar variáveis ou configurações que podem ser facilmente modificadas. Essencialmente, hardcoded significa que um valor específico está "fixo" no código, tornando-se parte integrante do programa.

Exemplos de hardcoded podem incluir:

1. **Valores Literais:**
   ```python
   # Exemplo em Python
   def calcular_area_raio(raio):
       return 3.14 * raio * raio
   ```

   No código acima, o valor `3.14` é hardcoded. Se a precisão da constante pi mudar, seria necessário alterar manualmente em todos os lugares em que ela foi utilizada.

2. **Caminhos de Arquivo:**
   ```python
   # Exemplo em Python
   arquivo = open('caminho/do/arquivo.txt', 'r')
   ```

   Neste exemplo, o caminho do arquivo está hardcoded. Se o arquivo for movido para um local diferente, o código precisará ser alterado.

3. **Credenciais:**
   ```python
   # Exemplo em Python (não recomendado)
   conexao_banco_dados('usuario', 'senha', 'host', 'nome_do_banco')
   ```

   Colocar credenciais diretamente no código é uma prática insegura e também considerada hardcoded. O ideal é armazenar informações sensíveis em variáveis de ambiente ou outros mecanismos de configuração.

O principal problema com o hardcoded é que ele torna o código menos flexível e mais difícil de manter. Se algo precisa ser alterado, é necessário modificar diretamente o código-fonte, o que pode ser propenso a erros e dificulta a manutenção. Em vez disso, é geralmente preferível usar variáveis ou configurações externas para armazenar valores que podem mudar com o tempo ou em diferentes ambientes.

Usar valores hardcoded pode ser apropriado em algumas situações simples, mas em muitos casos, é preferível adotar práticas mais flexíveis e configuráveis para garantir um código mais sustentável e fácil de gerenciar.

## Hardcoded no Django

Vamos considerar um exemplo simples no contexto do Django, onde um valor está hardcoded em uma view. Em seguida, veremos como podemos solucionar isso usando configurações do Django.

### Exemplo Hardcoded no Django:

Suponha que temos uma view que exibe uma mensagem de boas-vindas com um nome específico codificado diretamente no código:

```python
# views.py
from django.shortcuts import render

def welcome_view(request):
    name = "Alice"
    return render(request, 'welcome.html', {'name': name})
```

```html
<!-- welcome.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Bem-vindo</title>
</head>
<body>
    <h1>Bem-vindo, Alice!</h1>
</body>
</html>
```

Neste exemplo, o nome "Alice" está hardcoded na view, o que significa que, se quisermos alterar a mensagem de boas-vindas para um nome diferente, precisamos modificar diretamente o código.

### Solução Usando Configurações do Django:

Uma abordagem mais flexível seria usar configurações do Django para armazenar valores que podem ser facilmente modificados sem a necessidade de alterar diretamente o código-fonte. Vamos modificar o exemplo para usar uma configuração:

```python
# settings.py
WELCOME_NAME = "Alice"
```

```python
# views.py
from django.conf import settings
from django.shortcuts import render

def welcome_view(request):
    name = settings.WELCOME_NAME
    return render(request, 'welcome.html', {'name': name})
```

```html
<!-- welcome.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Bem-vindo</title>
</head>
<body>
    <h1>Bem-vindo, {{ name }}!</h1>
</body>
</html>
```

Agora, podemos alterar o nome de boas-vindas simplesmente modificando a configuração `WELCOME_NAME` no arquivo `settings.py`, sem precisar mexer no código da view.

Essa abordagem torna o código mais flexível, facilita a manutenção e separa as configurações do código-fonte principal. No entanto, é importante ter cuidado ao armazenar informações sensíveis em configurações, e em muitos casos, é preferível usar variáveis de ambiente ou outros métodos seguros para armazenar configurações sensíveis.

## URLs dinâmicas

Em Django, URLs dinâmicas referem-se à capacidade de capturar partes variáveis de uma URL e passá-las como parâmetros para funções de visualização. Isso é frequentemente realizado usando "curingas" (wildcards) na definição de URLs. As URLs dinâmicas são úteis quando você precisa lidar com diferentes informações ou recursos em seu aplicativo, onde parte da URL é variável.

A principal ferramenta para criar URLs dinâmicas no Django é o uso de padrões de URL e grupos de captura. Aqui está um exemplo básico para ilustrar como você pode criar URLs dinâmicas:

### Exemplo de URLs Dinâmicas no Django:

Suponha que você tenha um aplicativo chamado `blog` e deseje criar URLs dinâmicas para visualizar postagens individuais.

1. **Definição de URL no `urls.py` do Aplicativo:**

   ```python
   # blog/urls.py
   from django.urls import path
   from . import views

   urlpatterns = [
       path('posts/', views.lista_de_posts, name='lista_de_posts'),
       path('posts/<int:post_id>/', views.detalhes_do_post, name='detalhes_do_post'),
   ]
   ```

   Neste exemplo:
   - `posts/` corresponde a uma lista de todos os posts.
   - `posts/<int:post_id>/` captura um número inteiro (`<int:post_id>`) da URL, que será passado como um parâmetro chamado `post_id` para a função `detalhes_do_post` na sua view.

2. **Função de Visualização Correspondente:**

   ```python
   # blog/views.py
   from django.shortcuts import render, get_object_or_404
   from .models import Post

   def lista_de_posts(request):
       # Lógica para exibir lista de posts
       posts = Post.objects.all()
       return render(request, 'blog/lista_de_posts.html', {'posts': posts})

   def detalhes_do_post(request, post_id):
       # Lógica para exibir detalhes de um post específico
       post = get_object_or_404(Post, id=post_id)
       return render(request, 'blog/detalhes_do_post.html', {'post': post})
   ```

   Na função `detalhes_do_post`, `post_id` é um parâmetro que foi capturado da URL e passado para a função de visualização. Isso permite que você acesse o post específico correspondente ao `post_id`.

3. **Uso nos Templates:**

   Agora, nos templates, você pode criar links dinâmicos usando a tag `url` do Django:

   ```html
   <!-- blog/lista_de_posts.html -->
   <ul>
       {% for post in posts %}
           <li><a href="{% url 'detalhes_do_post' post_id=post.id %}">{{ post.titulo }}</a></li>
       {% endfor %}
   </ul>
   ```

   Aqui, `post.id` é usado para criar dinamicamente URLs para cada post, levando em consideração o padrão definido em `urls.py`.

Essa é uma maneira básica de criar URLs dinâmicas no Django. Lembre-se de que você pode personalizar os padrões de URL conforme necessário, dependendo dos requisitos do seu aplicativo. As URLs dinâmicas proporcionam flexibilidade e são uma parte fundamental do desenvolvimento web em Django.
