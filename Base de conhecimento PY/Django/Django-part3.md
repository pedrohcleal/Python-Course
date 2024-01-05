# Django part3

## Herança de templates

A herança de templates no Django permite que você defina um template base que contém a estrutura comum da sua aplicação e, em seguida, estenda ou herde esse template em outros templates específicos para adicionar ou substituir blocos de conteúdo. Isso é útil para evitar a duplicação de código e manter uma estrutura consistente em todo o seu site.

A herança de templates é implementada usando a tag `{% extends %}` para indicar que um template deve herdar de outro. Além disso, você pode usar a tag `{% block %}` para definir blocos de conteúdo no template pai que podem ser substituídos nos templates filhos.

Aqui está um exemplo básico para ilustrar a herança de templates no Django:

### Template Base (base.html):

```html
<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Título Padrão{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <h1>{% block header %}Meu Site{% endblock %}</h1>
    </header>

    <nav>
        <!-- Menu de navegação comum -->
    </nav>

    <div id="content">
        {% block content %}{% endblock %}
    </div>

    <footer>
        <p>&copy; 2023 Meu Site</p>
    </footer>
</body>
</html>
```

### Template Filho (page.html):

```html
<!-- page.html -->

{% extends 'base.html' %}

{% block title %}Página Específica - {{ block.super }}{% endblock %}

{% block header %}Página Específica{% endblock %}

{% block content %}
    <h2>Conteúdo da Página Específica</h2>
    <p>Este é o conteúdo único para esta página.</p>
{% endblock %}
```

Neste exemplo:

- `base.html` é o template base que contém a estrutura comum do site.
- `page.html` estende `base.html` usando `{% extends 'base.html' %}`.
- Os blocos `{% block %}` em `base.html` indicam áreas onde conteúdo específico pode ser inserido ou substituído pelos templates filhos.
- O conteúdo do bloco `title` em `page.html` substitui o conteúdo do bloco `title` em `base.html`, e assim por diante.

Quando você renderiza `page.html`, ele incluirá a estrutura de `base.html` e substituirá ou adicionar o conteúdo específico definido no próprio template `page.html`. Isso proporciona uma maneira eficaz de organizar e reutilizar código em seus projetos Django.

## partials e include para separar trechos de templates

No contexto de templates no Django, "partials" refere-se a trechos de código HTML ou blocos de conteúdo que são separados e reutilizados em vários templates. A diretiva `include` é uma ferramenta fundamental para implementar partials, permitindo que você inclua o conteúdo de um arquivo em um local específico de outro template. Isso é útil para evitar a duplicação de código e manter uma estrutura de código modular e fácil de manter.

### Implementando Partials com `include`:

1. **Criação de Partial (ex. `_header.html`):**
   - Crie um arquivo HTML que contenha o trecho de código que você deseja reutilizar. Nomeie-o com um prefixo de sublinhado para indicar que é um partial.

     ```html
     <!-- _header.html -->

     <header>
         <h1>Meu Site</h1>
         <nav>
             <!-- Menu de navegação -->
         </nav>
     </header>
     ```

2. **Uso de `include` em Outro Template:**
   - Em outros templates onde você deseja incluir esse trecho, use a tag `{% include %}`.

     ```html
     <!-- outro_template.html -->

     {% include '_header.html' %}

     <div id="content">
         <h2>Conteúdo da Página</h2>
         <p>Este é o conteúdo específico da página.</p>
     </div>

     <footer>
         <p>&copy; 2023 Meu Site</p>
     </footer>
     ```

3. **Renderização Final:**
   - Quando o template `outro_template.html` é renderizado, o conteúdo do arquivo `_header.html` é incluído no local onde a tag `{% include '_header.html' %}` foi colocada.

### Vantagens:

- **Reutilização de Código:** Ao usar partials e `include`, você pode reutilizar facilmente trechos de código em vários templates, evitando a duplicação e tornando o código mais limpo e modular.

- **Manutenção Simples:** Se você precisar fazer alterações no trecho de código que está sendo reutilizado, só precisará fazer essa alteração em um único local (no arquivo partial), e as mudanças serão refletidas em todos os lugares onde o partial é incluído.

### Considerações Adicionais:

- **Variáveis e Contexto:** Você também pode passar variáveis para partials usando o argumento `with` na tag `{% include %}`. Isso permite personalizar o conteúdo do partial com base no contexto do template pai.

   ```html
   {% include '_header.html' with user=usuario %}
   ```

- **Nomeando Convenções:** O uso de nomes que começam com um sublinhado (`_`) para partials é uma convenção comum, mas não é obrigatório. O importante é escolher um sistema que faça sentido para sua equipe e manter a consistência.

O uso de partials e `include` é uma prática recomendada no desenvolvimento web Django, facilitando a criação de templates mais limpos, organizados e fáceis de manter.

## Arquivos estáticos

Em Django, os arquivos estáticos são recursos como imagens, arquivos CSS, JavaScript e outros tipos de arquivos que não são gerados dinamicamente pelo servidor web, mas permanecem inalterados durante a execução da aplicação. Esses arquivos são servidos diretamente pelo servidor web, sem processamento pela aplicação Django.

Os arquivos estáticos são essenciais para adicionar estilos, scripts e outros recursos visuais e interativos às páginas web. Aqui está uma descrição dos principais componentes relacionados aos arquivos estáticos em um projeto Django:

### 1. **Diretório `static`:**
   - Em cada aplicativo Django, você pode criar um diretório chamado `static` para armazenar seus arquivos estáticos. Este diretório deve estar localizado no mesmo nível que o diretório `templates`.

     ```plaintext
     meu_app/
     ├── static/
     │   └── meu_app/
     │       ├── css/
     │       │   └── style.css
     │       └── js/
     │           └── script.js
     └── templates/
         └── meu_app/
             └── template.html
     ```

### 2. **Definição de Arquivos Estáticos no HTML:**
   - Para incluir arquivos estáticos em seus templates HTML, use a tag `{% load static %}` para carregar o conjunto de tags estáticas do Django. Em seguida, use a tag `{% static %}` para construir a URL do arquivo estático.

     ```html
     {% load static %}

     <!DOCTYPE html>
     <html>
     <head>
         <link rel="stylesheet" type="text/css" href="{% static 'meu_app/css/style.css' %}">
     </head>
     <body>
         <!-- Conteúdo da página -->
         <script src="{% static 'meu_app/js/script.js' %}"></script>
     </body>
     </html>
     ```

### 3. **Configurações em `settings.py`:**
   - O arquivo de configuração `settings.py` do seu projeto Django contém configurações relacionadas a arquivos estáticos. Verifique se a configuração `STATIC_URL` está configurada corretamente. O valor padrão é `'/static/'`.

     ```python
     # settings.py

     STATIC_URL = '/static/'
     ```

### 4. **Coleta de Arquivos Estáticos para Produção:**
   - Para aplicativos em produção, você deve coletar todos os arquivos estáticos em um diretório centralizado. Use o comando `collectstatic` para realizar essa tarefa.

     ```bash
     python manage.py collectstatic
     ```

   - Isso copiará todos os arquivos estáticos de todos os aplicativos para o diretório definido em `STATIC_ROOT` em seu arquivo `settings.py`.

### 5. **Uso de `whitenoise` ou Servidores de Arquivos Estáticos:**
   - Em ambientes de produção, você pode optar por usar o middleware `whitenoise` ou servidores web dedicados (como Nginx ou Apache) para servir arquivos estáticos de maneira mais eficiente.

### 6. **Arquivos Estáticos no Django Admin:**
   - O Django Admin também lida automaticamente com os arquivos estáticos necessários para sua interface. Certifique-se de que a URL `/static/admin/` está configurada corretamente para que os estilos e scripts do Django Admin sejam carregados corretamente.

O uso adequado de arquivos estáticos é crucial para criar interfaces web atraentes e interativas. Ao seguir as convenções do Django para arquivos estáticos, você garante uma organização clara e eficiente desses recursos em seu projeto.

## Uso de context para enviar dados para  dentro dos templates do django

No Django, o contexto é uma maneira de enviar dados do lado do servidor para o template, permitindo que você renderize dinamicamente informações específicas em suas páginas web. O contexto é geralmente uma estrutura de dados, como um dicionário, que contém pares de chave-valor representando variáveis que podem ser acessadas no template.

### Passando Contexto para Templates:

1. **Usando `render` em Funções de Visualização:**
   - Ao usar a função `render` para renderizar um template em uma função de visualização, você pode passar um dicionário como contexto.

     ```python
     from django.shortcuts import render

     def minha_visualizacao(request):
         contexto = {'nome': 'João', 'idade': 25}
         return render(request, 'template.html', contexto)
     ```

2. **Usando `Context` em Classes de Visualização:**
   - Se você estiver usando classes de visualização baseadas em `View`, pode usar a classe `Context` para definir o contexto.

     ```python
     from django.views import View
     from django.http import HttpResponse
     from django.template import Context, loader

     class MinhaView(View):
         def get(self, request):
             contexto = {'nome': 'Maria', 'idade': 30}
             template = loader.get_template('template.html')
             return HttpResponse(template.render(contexto, request))
     ```

### Acessando Contexto em Templates:

1. **Uso de Variáveis no Template:**
   - No template, você pode acessar as variáveis definidas no contexto usando a sintaxe `{{ nome_da_variavel }}`.

     ```html
     <!-- template.html -->

     <p>Nome: {{ nome }}</p>
     <p>Idade: {{ idade }}</p>
     ```

2. **Estruturas de Controle:**
   - Você pode usar estruturas de controle como `{% if %}`, `{% for %}`, etc., para tomar decisões ou iterar sobre dados do contexto.

     ```html
     <!-- template.html -->

     {% if idade >= 18 %}
         <p>Este usuário é maior de idade.</p>
     {% else %}
         <p>Este usuário é menor de idade.</p>
     {% endif %}
     ```

3. **Acesso a Atributos de Objetos:**
   - Se o contexto contiver objetos, você pode acessar seus atributos usando a notação de ponto.

     ```python
     # views.py

     class Pessoa:
         def __init__(self, nome, idade):
             self.nome = nome
             self.idade = idade

     def minha_visualizacao(request):
         pessoa = Pessoa(nome='Ana', idade=22)
         contexto = {'usuario': pessoa}
         return render(request, 'template.html', contexto)
     ```

     ```html
     <!-- template.html -->

     <p>Nome: {{ usuario.nome }}</p>
     <p>Idade: {{ usuario.idade }}</p>
     ```

### Passando Contexto Adicional Globalmente:

- Às vezes, pode ser útil passar dados específicos para todos os templates em todas as visualizações. Para isso, você pode usar um context processor. Um context processor é uma função que adiciona variáveis ao contexto global.

   ```python
   # meu_app/context_processors.py

   def informacoes_globais(request):
       return {'informacao_global': 'Essa é uma informação global.'}
   ```

   Adicione isso ao `context_processors` em `settings.py`:

   ```python
   # settings.py

   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   # ...
                   'meu_app.context_processors.informacoes_globais',
               ],
           },
       },
   ]
   ```

   Agora, `informacao_global` estará disponível em todos os templates.

### Conclusão:

O uso de contexto no Django é fundamental para fornecer dados dinâmicos aos seus templates, permitindo que você crie páginas web personalizadas e interativas. Certifique-se de escolher um nome de variável claro e siga as práticas recomendadas para manter seus templates organizados e fáceis de entender.

