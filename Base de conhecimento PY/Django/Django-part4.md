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
