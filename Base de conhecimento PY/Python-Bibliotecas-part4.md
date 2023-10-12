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
