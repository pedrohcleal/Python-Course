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
