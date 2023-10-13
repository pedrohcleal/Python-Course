# Bibliotecas Py part 4

## SYS lib

A biblioteca `sys` em Python é um módulo padrão que fornece acesso a funcionalidades relacionadas ao sistema. Ela permite que você interaja com o ambiente em que seu programa Python está sendo executado, fornecendo informações e funcionalidades relacionadas ao sistema operacional, ao interpretador Python e ao ambiente de execução. Aqui estão algumas das principais funcionalidades da biblioteca `sys`:

1. **Acesso a argumentos de linha de comando:** O módulo `sys` permite que você acesse os argumentos passados ​​para um programa Python a partir da linha de comando. Você pode usar `sys.argv` para obter uma lista dos argumentos, onde `sys.argv[0]` é o nome do script Python em execução e os argumentos subsequentes são os argumentos fornecidos.

2. **Manipulação de caminhos de arquivo:** A biblioteca `sys` fornece funcionalidades para trabalhar com caminhos de arquivo. O `sys.path` é uma lista de diretórios onde o interpretador Python procura módulos para importar. Você pode adicionar diretórios a esta lista se desejar importar módulos de locais personalizados.

3. **Funções relacionadas à saída padrão e erro:** `sys.stdout` e `sys.stderr` são objetos que representam a saída padrão e a saída de erro, respectivamente. Você pode redirecionar essas saídas para outros locais, como arquivos, se necessário.

4. **Variáveis e configurações do interpretador:** O módulo `sys` oferece informações sobre o interpretador Python em execução. Você pode acessar informações como a versão do Python (`sys.version`), a versão do interpretador (`sys.hexversion`), e outros detalhes relacionados ao sistema.

5. **Finalização de programa:** A função `sys.exit()` é usada para encerrar o programa. Seu argumento opcional pode ser um código de status que indica o motivo do encerramento.

6. **Gestão de exceções:** A função `sys.exc_info()` retorna informações sobre a exceção atual sendo tratada, se houver. Isso pode ser útil para lidar com erros de forma programática.

7. **Interação com o interpretador Python:** O módulo `sys` também permite interagir com o interpretador Python em execução. Por exemplo, você pode usar `sys.stdin` e `sys.stdout` para interagir com a entrada e saída do interpretador, ou `sys.exec_prefix` para obter o diretório onde o interpretador Python está instalado.

A biblioteca `sys` é uma parte essencial da linguagem Python e é amplamente utilizada em várias aplicações, desde processamento de linha de comando até manipulação de caminhos de arquivo e gerenciamento de exceções. Ela fornece acesso a informações importantes sobre o ambiente de execução do seu programa e é útil em uma variedade de cenários.

### sys.argv

`sys.argv` é uma lista em Python que contém os argumentos passados para um programa Python a partir da linha de comando quando o programa é iniciado. Ela é uma parte fundamental do módulo `sys` e é comumente usada para interagir com argumentos de linha de comando.

A lista `sys.argv` é composta pelos seguintes elementos:

1. `sys.argv[0]`: O primeiro elemento da lista `sys.argv` é sempre o nome do script Python em execução. Esse valor é fornecido automaticamente pelo interpretador Python.

2. `sys.argv[1]`, `sys.argv[2]`, e assim por diante: Os elementos subsequentes na lista `sys.argv` são os argumentos que foram passados para o programa na linha de comando. Por exemplo, se você executar um script Python da seguinte maneira:

   ```bash
   python meu_script.py arg1 arg2 arg3
   ```

   Então, `sys.argv[1]` conterá a string "arg1", `sys.argv[2]` conterá "arg2" e `sys.argv[3]` conterá "arg3".

Você pode usar `sys.argv` para criar programas que sejam sensíveis aos argumentos de linha de comando. Isso é especialmente útil quando você deseja que seu programa realize ações diferentes com base nos argumentos fornecidos pelos usuários. Você pode usar bibliotecas como `argparse` para analisar e gerenciar os argumentos de forma mais sofisticada.

Aqui está um exemplo simples de como você pode usar `sys.argv` em um script Python:

```python
import sys

# Verificando se pelo menos um argumento foi passado
if len(sys.argv) > 1:
    # O primeiro argumento é o nome do script, então começamos a partir de sys.argv[1]
    for i in range(1, len(sys.argv)):
        print(f"Argumento {i}: {sys.argv[i]}")
else:
    print("Nenhum argumento foi passado.")
```

Este script verifica se foram passados argumentos na linha de comando e os imprime. Caso contrário, exibe uma mensagem informando que nenhum argumento foi passado.

## argparse

`argparse` é um módulo em Python que permite que você processe argumentos de linha de comando de uma maneira conveniente e eficiente. Ele é frequentemente usado para criar interfaces de linha de comando para programas Python, tornando mais fácil para os usuários interagir com o seu programa fornecendo argumentos ao executá-lo a partir da linha de comando.

Aqui estão os conceitos básicos sobre como usar o `argparse` em Python:

1. **Importação do módulo `argparse`**:
   Comece importando o módulo `argparse` no seu código.

   ```python
   import argparse
   ```

2. **Criação de um objeto `ArgumentParser`**:
   Em seguida, crie um objeto `ArgumentParser` que será usado para definir os argumentos que seu programa aceitará.

   ```python
   parser = argparse.ArgumentParser(description='Descrição do seu programa')
   ```

3. **Definição de argumentos**:
   Use o objeto `parser` para definir os argumentos que o seu programa aceitará. Você pode adicionar argumentos posicionais, argumentos opcionais (com ou sem valores padrão) e outros tipos de argumentos. Por exemplo:

   ```python
   parser.add_argument('arquivo', help='Nome do arquivo de entrada')
   parser.add_argument('--verbose', '-v', action='store_true', help='Ativar modo verboso')
   parser.add_argument('--output', '-o', default='output.txt', help='Nome do arquivo de saída')
   ```

4. **Parsagem dos argumentos**:
   Use `parser.parse_args()` para analisar os argumentos da linha de comando. Ele retornará um objeto que contém os valores dos argumentos definidos anteriormente.

   ```python
   args = parser.parse_args()
   ```

5. **Acesso aos valores dos argumentos**:
   Você pode acessar os valores dos argumentos a partir do objeto `args` gerado pela função `parse_args()`.

   ```python
   print(args.arquivo)
   if args.verbose:
       print('Modo verboso ativado.')
   print(f'Arquivo de saída: {args.output}')
   ```

6. **Execução do programa**:
   Agora, você pode usar os valores dos argumentos para executar as ações necessárias no seu programa.

Geralmente, o `argparse` fornece funcionalidades poderosas para manipulação de argumentos de linha de comando, incluindo validação de tipos de dados, ajuda automática e mensagens de erro. Ele é uma ferramenta essencial ao criar scripts Python que interagem com o usuário via linha de comando.

## Requests lib

O módulo `requests` em Python é uma biblioteca popular para fazer solicitações HTTP de forma simples e eficiente. Ele permite que os desenvolvedores enviem requisições HTTP para servidores web e recebam as respostas de forma fácil, proporcionando uma maneira conveniente de interagir com recursos na web, como fazer solicitações a APIs, baixar conteúdo da web, enviar dados para servidores, e muito mais.

Aqui estão algumas funcionalidades-chave do módulo `requests`:

1. **Envio de Requisições HTTP**: O `requests` permite enviar solicitações HTTP, como GET, POST, PUT, DELETE e muitos outros, usando funções simples e legíveis. Por exemplo:

```python
import requests

response = requests.get('https://www.example.com')
```

2. **Tratamento de Respostas HTTP**: O módulo permite acessar facilmente os dados retornados em uma resposta HTTP. Isso inclui o conteúdo da resposta, cabeçalhos, status code e outros detalhes da resposta:

```python
print(response.text)  # Conteúdo da resposta
print(response.status_code)  # Código de status (e.g., 200 para OK)
print(response.headers)  # Cabeçalhos da resposta
```

3. **Envio de Dados**: É possível enviar dados com solicitações POST e PUT, que são frequentemente usadas ao interagir com APIs. Por exemplo, enviando um JSON:

```python
import requests

data = {'key': 'value'}
response = requests.post('https://www.example.com/api', json=data)
```

4. **Autenticação**: O `requests` oferece suporte a diferentes métodos de autenticação, como autenticação básica (HTTP Basic Auth) e autenticação baseada em tokens.

5. **Sessões**: A biblioteca permite manter sessões para manter o estado entre várias solicitações, o que pode ser útil ao lidar com autenticação persistente ou gerenciamento de cookies.

6. **Manipulação de Cookies**: Você pode facilmente acessar e gerenciar cookies nas solicitações, o que é útil ao lidar com autenticação baseada em cookies.

7. **Tratamento de Redirecionamento**: O `requests` segue automaticamente redirecionamentos, tornando mais fácil lidar com recursos que redirecionam para outras URLs.

8. **Manipulação de Erros**: A biblioteca lida com erros de solicitação de forma apropriada, tornando mais fácil capturar exceções e tratar problemas de rede ou servidor.

O módulo `requests` é amplamente utilizado em muitos projetos Python e é uma escolha popular para tarefas de comunicação com a web devido à sua simplicidade, flexibilidade e documentação abrangente.

Para começar a usar o `requests`, você precisa instalá-lo (caso ainda não esteja instalado) e, em seguida, importá-lo no seu código. Você pode instalar o `requests` usando o `pip`:

```bash
pip install requests
```

Depois de instalado, você pode começar a usá-lo em seus projetos Python para interagir com recursos da web de forma eficiente e amigável.
### Envio de Requisições HTTP

O envio de requisições HTTP na biblioteca `requests` em Python é uma tarefa fundamental ao interagir com serviços web, consumir APIs ou realizar operações de comunicação com recursos na internet. A biblioteca `requests` simplifica esse processo, tornando-o fácil de entender e usar. Abaixo estão as etapas básicas para enviar requisições HTTP com o `requests`:

1. **Importe a biblioteca `requests`**:

   Para começar, você precisa importar o módulo `requests` no seu código Python. Você pode fazer isso da seguinte forma:

   ```python
   import requests
   ```

2. **Envie uma solicitação HTTP**:

   Agora, você pode usar as funções disponíveis no módulo `requests` para enviar solicitações HTTP. As solicitações HTTP mais comuns incluem GET, POST, PUT e DELETE. Veja como fazer cada uma delas:

   - **GET Request**:

     Para fazer uma solicitação GET e recuperar dados de um servidor web, use o método `requests.get()`:

     ```python
     response = requests.get('https://api.example.com/data')
     ```

   - **POST Request**:

     Para enviar dados para um servidor, use o método `requests.post()`. Você pode fornecer dados no corpo da solicitação, como um dicionário, uma lista ou uma string:

     ```python
     data = {'key': 'value'}
     response = requests.post('https://api.example.com/endpoint', data=data)
     ```

   - **PUT Request**:

     Para atualizar recursos no servidor, use o método `requests.put()` de forma semelhante ao POST, mas para solicitações PUT:

     ```python
     data = {'key': 'new_value'}
     response = requests.put('https://api.example.com/resource/123', data=data)
     ```

   - **DELETE Request**:

     Para excluir recursos no servidor, use o método `requests.delete()`:

     ```python
     response = requests.delete('https://api.example.com/resource/123')
     ```

3. **Acesse a resposta HTTP**:

   Após enviar a solicitação, você pode acessar a resposta HTTP para obter informações, como o conteúdo da resposta, o código de status, os cabeçalhos e muito mais. Por exemplo:

   - Para acessar o conteúdo da resposta:

     ```python
     response.text  # Contém o conteúdo da resposta (geralmente em formato de texto)
     ```

   - Para verificar o código de status:

     ```python
     response.status_code  # Contém o código de status da resposta (por exemplo, 200 para sucesso)
     ```

   - Para acessar os cabeçalhos da resposta:

     ```python
     response.headers  # Contém os cabeçalhos da resposta em um dicionário
     ```

A biblioteca `requests` é muito flexível e fornece recursos adicionais para lidar com autenticação, sessões, manipulação de cookies e redirecionamento. É amplamente utilizada para interagir com serviços web, consumir APIs e automatizar tarefas de comunicação com recursos na internet. Certifique-se de lidar com possíveis erros ou exceções que possam ocorrer durante a comunicação com o servidor, para garantir que seu código seja robusto e seguro.
### https.server

Parece que você está tentando iniciar o servidor HTTP embutido do Python (`http.server`) com algumas opções específicas. No comando que você forneceu, você está tentando:

1. Definir o diretório raiz do servidor como `.\aula190_site\`.
2. Definir a porta como `3333`.

No entanto, há um pequeno problema no comando que você forneceu: a porta deve ser especificada antes do diretório. Aqui está o comando corrigido:

```bash
python -m http.server 3333 -d .\aula190_site\
```

Neste comando:

- `python -m http.server` inicia o servidor HTTP embutido.
- `3333` define a porta na qual o servidor escutará.
- `-d .\aula190_site\` define o diretório raiz a partir do qual os arquivos serão servidos.

Certifique-se de que o diretório `aula190_site` exista no diretório atual e que os arquivos que deseja servir estejam dentro desse diretório. Após executar o comando corrigido, você deve poder acessar os arquivos do diretório `aula190_site` em um navegador digitando `http://localhost:3333` no endereço. Certifique-se de que o servidor seja iniciado sem erros e que os arquivos no diretório estejam configurados corretamente.

## BeatifulSoup lib

Beautiful Soup é uma biblioteca Python muito popular para análise de documentos HTML e XML. Ela é amplamente utilizada para extrair dados de páginas da web, raspar informações de sites e realizar tarefas de web scraping. Beautiful Soup cria uma árvore analisável a partir de um documento HTML ou XML, tornando a extração de dados e a navegação através da estrutura do documento mais fácil e conveniente.

Aqui estão alguns conceitos e recursos-chave do BeautifulSoup:

1. Análise de documentos: Beautiful Soup ajuda na análise de documentos HTML ou XML, permitindo que você acesse facilmente elementos, atributos e texto.

2. Navegação na árvore: A biblioteca fornece várias maneiras de navegar pela estrutura do documento, como buscar elementos por tag, classe, id, ou mesmo usando seletores CSS.

3. Extração de dados: Você pode extrair facilmente informações de um documento, como texto, atributos de elementos e dados de tabelas.

4. Modificação de documentos: Beautiful Soup permite fazer modificações no documento, como adicionar ou remover elementos, alterar atributos ou texto.

5. Parsing: Beautiful Soup suporta diferentes analisadores, como "html.parser," "lxml," e "html5lib," o que a torna flexível para lidar com documentos HTML diversos.

Aqui está um exemplo simples de como usar Beautiful Soup para analisar um documento HTML:

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>Exemplo de BeautifulSoup</title>
</head>
<body>
    <p class="paragrafo">Este é um exemplo de BeautifulSoup.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
</body>
</html>
"""

# Criar um objeto BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Acessar elementos
title = soup.title
paragraph = soup.find('p', class_='paragrafo')
items = soup.find_all('li')

# Imprimir o texto dos elementos
print(title.text)
print(paragraph.text)
for item in items:
    print(item.text)
```

Beautiful Soup é uma ferramenta poderosa para tarefas de web scraping, permitindo que você extraia dados de páginas da web de maneira eficiente. No entanto, lembre-se sempre de seguir as leis e políticas de acesso aos dados de sites da web ao usá-lo.

## Web Scraping com Python usando requests e bs4 BeautifulSoup

O web scraping com Python, usando as bibliotecas `requests` e `Beautiful Soup` (ou `bs4`), é uma técnica para extrair informações de páginas da web de forma automatizada. O `requests` é usado para fazer solicitações HTTP para obter o conteúdo da página web, e o `Beautiful Soup` ajuda a analisar e extrair os dados desejados do HTML ou XML da página.

Aqui está um exemplo passo a passo de como realizar web scraping usando essas duas bibliotecas:

1. Instalação das bibliotecas:
   Certifique-se de ter as bibliotecas `requests` e `beautifulsoup4` instaladas. Você pode instalá-las com o pip:

   ```
   pip install requests
   pip install beautifulsoup4
   ```

2. Importação das bibliotecas:
   No início do seu script, importe as bibliotecas necessárias:

   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

3. Fazer uma solicitação HTTP:
   Use o `requests` para obter o conteúdo HTML de uma página da web. Por exemplo:

   ```python
   url = 'https://exemplo.com'
   response = requests.get(url)
   ```

4. Analisar o conteúdo da página com BeautifulSoup:
   Crie um objeto BeautifulSoup passando o conteúdo HTML e um analisador como argumentos. Um analisador pode ser 'html.parser', 'lxml', ou 'html5lib'. Por exemplo:

   ```python
   soup = BeautifulSoup(response.text, 'html.parser')
   ```

5. Navegar e extrair dados:
   Use os recursos do BeautifulSoup para navegar na estrutura do documento HTML e extrair os dados desejados. Alguns exemplos de operações comuns:

   - Para encontrar um elemento por tag:

     ```python
     element = soup.find('tag')
     ```

   - Para encontrar todos os elementos com uma determinada classe:

     ```python
     elements = soup.find_all('tag', class_='nome_da_classe')
     ```

   - Para acessar o texto de um elemento:

     ```python
     text = element.text
     ```

   - Para acessar os atributos de um elemento:

     ```python
     attribute = element['atributo']
     ```

6. Processar e armazenar os dados:
   Uma vez que você tenha extraído os dados desejados, você pode processá-los ou armazená-los da maneira que preferir. Por exemplo, você pode salvá-los em um arquivo, armazená-los em um banco de dados, ou usá-los para análise.

Lembre-se de que ao realizar web scraping, é importante respeitar os termos de serviço dos sites que você está acessando e considerar questões de ética e legalidade. Alguns sites podem proibir a extração de dados ou impor limites à taxa de solicitações. Certifique-se de cumprir essas diretrizes para evitar problemas legais ou bloqueios.

### Encondig BS4

Em Beautiful Soup 4 (bs4), a manipulação de encoding é uma parte importante quando você está trabalhando com páginas da web que podem estar em diferentes conjuntos de caracteres (charsets). Aqui estão algumas informações sobre como o Beautiful Soup 4 lida com encoding:

1. **Deteção de encoding automática:** Beautiful Soup é capaz de detectar automaticamente o encoding da página web. Ele faz isso examinando o `<meta>` tag no cabeçalho do documento HTML e, se não encontrar, olhando para o encoding declarado na resposta HTTP. Isso ajuda a garantir que os caracteres sejam interpretados corretamente.

2. **Conversão para Unicode:** Beautiful Soup converte automaticamente os dados da página web em Unicode. Isso é importante porque o Python lida com strings em Unicode, permitindo que você trabalhe com texto de forma consistente, independentemente do encoding original da página web.

3. **Especificar um encoding manualmente:** Em alguns casos, você pode precisar especificar manualmente o encoding, especialmente se o documento HTML não contiver informações de codificação válidas ou se você souber o encoding que deve ser usado. Você pode fazer isso ao criar o objeto BeautifulSoup, passando o argumento `from_encoding`:

   ```python
   soup = BeautifulSoup(html, 'html.parser', from_encoding='iso-8859-1')
   ```

   Neste exemplo, `from_encoding` é usado para especificar o encoding ISO-8859-1. Lembre-se de que é importante usar essa opção com cuidado e apenas quando necessário.

4. **Codificação de saída:** Quando você deseja salvar os dados analisados, você deve codificá-los no encoding apropriado. Por exemplo, para salvar os dados em um arquivo, você pode usar:

   ```python
   with open('output.html', 'w', encoding='utf-8') as file:
       file.write(soup.prettify())
   ```

   Neste exemplo, os dados são codificados em UTF-8, que é amplamente utilizado para codificação de texto na web.

Em resumo, Beautiful Soup 4 é projetado para facilitar a manipulação de encoding ao lidar com páginas da web. Ele faz um bom trabalho na deteção automática de encoding e conversão para Unicode, mas também oferece a flexibilidade de especificar o encoding manualmente quando necessário. Certifique-se de estar ciente do encoding ao trabalhar com dados da web para garantir que o texto seja interpretado e exibido corretamente.

## Selenium lib

O Selenium é uma ferramenta de automação de testes amplamente usada para testar aplicativos da web por meio de scripts. Com o Selenium, você pode automatizar a interação de um navegador da web com um site ou aplicativo da web, executando ações como clicar em botões, preencher formulários, navegar por páginas e extrair informações.

O Selenium suporta várias linguagens de programação, incluindo Python, o que o torna uma escolha popular para desenvolvedores que desejam automatizar tarefas de teste em seus aplicativos da web. Para usar o Selenium com Python, você precisa do módulo Python chamado "selenium", que pode ser instalado usando um gerenciador de pacotes como o pip.

Aqui estão os passos básicos para começar a usar o Selenium com Python:

1. Instale o Selenium: Você pode instalar o Selenium para Python executando o seguinte comando no seu terminal ou prompt de comando:

```bash
pip install selenium
```

2. Baixe um driver de navegador: O Selenium requer um driver específico para o navegador que você deseja automatizar. Os drivers são essenciais para permitir que o Selenium interaja com o navegador. Alguns dos drivers populares incluem o ChromeDriver, o GeckoDriver (para o Firefox) e o WebDriver para o Safari. Certifique-se de baixar o driver correto para o seu navegador.

3. Escreva seu script de automação: Agora você pode escrever um script em Python para automatizar as ações que deseja executar no navegador. Aqui está um exemplo simples que abre o Google Chrome, acessa o site do Google e faz uma pesquisa:

```python
from selenium import webdriver

# Inicialize o driver do Chrome (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

# Abra uma página da web
driver.get("https://www.google.com")

# Encontre o campo de pesquisa e digite algo nele
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium with Python")

# Clique no botão de pesquisa
search_box.submit()

# Feche o navegador
driver.quit()
```

4. Execute o script: Salve o script em um arquivo Python (.py) e execute-o. O Selenium abrirá o navegador, executará as ações especificadas e, em seguida, fechará o navegador.

O Selenium com Python oferece muitos recursos avançados, como a capacidade de esperar por elementos, manipular cookies, alternar entre janelas e frames, tirar screenshots e muito mais. É uma ferramenta poderosa para automação de tarefas relacionadas à web, testes de software e scraping de dados da web.
