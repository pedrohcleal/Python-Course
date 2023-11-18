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
