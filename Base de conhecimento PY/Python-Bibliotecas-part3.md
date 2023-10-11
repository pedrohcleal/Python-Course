# Bibliotecas Py part 3

## CSV

CSV, que significa "Comma-Separated Values" (Valores Separados por Vírgula), é um formato comum para armazenar dados tabulares em texto plano. No Python, você pode trabalhar com arquivos CSV usando a biblioteca `csv`, que oferece funcionalidades para ler, escrever e manipular dados nesse formato.

Aqui está uma visão geral das principais operações com arquivos CSV em Python:

1. **Leitura de Arquivos CSV:**
   Para ler dados de um arquivo CSV, você pode usar a classe `csv.reader`. Aqui está um exemplo de como fazer isso:

   ```python
   import csv

   with open('arquivo.csv', 'r') as arquivo_csv:
       leitor_csv = csv.reader(arquivo_csv)
       for linha in leitor_csv:
           print(linha)
   ```

   Isso abrirá o arquivo 'arquivo.csv' e lerá suas linhas como listas de valores, onde os valores são separados por vírgulas.

2. **Escrita em Arquivos CSV:**
   Para escrever dados em um arquivo CSV, você pode usar a classe `csv.writer`. Aqui está um exemplo simples:

   ```python
   import csv

   dados = [
       ['Nome', 'Idade', 'Cidade'],
       ['João', 30, 'São Paulo'],
       ['Maria', 25, 'Rio de Janeiro']
   ]

   with open('arquivo.csv', 'w', newline='') as arquivo_csv:
       escritor_csv = csv.writer(arquivo_csv)
       for linha in dados:
           escritor_csv.writerow(linha)
   ```

   Isso criará um arquivo 'arquivo.csv' com os dados fornecidos, separados por vírgulas.

3. **Manipulação de Dados CSV:**
   A biblioteca `csv` também fornece funcionalidades para manipular dados CSV, como adicionar, modificar ou remover linhas e colunas. Você pode ler os dados em uma estrutura de dados, como uma lista de listas ou um dicionário, fazer as manipulações necessárias e, em seguida, escrever os dados de volta no arquivo CSV.

4. **Configurações Adicionais:**
   A biblioteca `csv` oferece várias opções para personalizar a leitura e a escrita de arquivos CSV, como o delimitador (que nem sempre precisa ser uma vírgula), o caractere de escape e o comportamento de delimitação de aspas.

Em resumo, a biblioteca `csv` do Python é uma ferramenta poderosa para trabalhar com dados em formato CSV. Ela simplifica a leitura, escrita e manipulação de dados tabulares, tornando-a uma escolha popular para tarefas que envolvem processamento de dados CSV.

### DictWriter e DictReader

`DictWriter` e `DictReader` são duas classes da biblioteca `csv` do Python que permitem trabalhar com arquivos CSV usando dicionários em vez de listas. Isso pode ser muito útil quando você deseja ler ou escrever dados CSV em que cada linha é representada como um dicionário, onde as chaves são os nomes das colunas e os valores são os dados correspondentes. Essas classes tornam a manipulação de dados CSV mais intuitiva quando você tem informações tabulares com cabeçalhos nomeados.

Aqui está uma descrição de cada uma dessas classes:

1. **`DictWriter` (Escrita de Dados CSV):**
   A classe `DictWriter` é usada para escrever dados em um arquivo CSV usando dicionários como entrada. Isso significa que você pode especificar os dados a serem escritos em cada linha do arquivo CSV usando dicionários onde as chaves correspondem aos nomes das colunas.

   Exemplo de uso do `DictWriter`:

   ```python
   import csv

   dados = [
       {'Nome': 'João', 'Idade': 30, 'Cidade': 'São Paulo'},
       {'Nome': 'Maria', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
       {'Nome': 'Carlos', 'Idade': 35, 'Cidade': 'Belo Horizonte'}
   ]

   with open('dados_dictwriter.csv', 'w', newline='') as arquivo_csv:
       campos = ['Nome', 'Idade', 'Cidade']
       escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
       escritor_csv.writeheader()
       for linha in dados:
           escritor_csv.writerow(linha)
   ```

   Neste exemplo, usamos `DictWriter` para escrever dados em um arquivo CSV, especificando os campos (ou colunas) usando `fieldnames` e escrevendo os dados linha por linha.

2. **`DictReader` (Leitura de Dados CSV):**
   A classe `DictReader` é usada para ler dados de um arquivo CSV em que cada linha é representada como um dicionário. Isso facilita muito a leitura e manipulação de dados, pois você pode acessar os valores por meio de nomes de colunas em vez de índices de lista.

   Exemplo de uso do `DictReader`:

   ```python
   import csv

   with open('dados_dictwriter.csv', 'r') as arquivo_csv:
       leitor_csv = csv.DictReader(arquivo_csv)
       for linha in leitor_csv:
           print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
   ```

   Neste exemplo, usamos `DictReader` para ler os dados do arquivo CSV e acessamos os valores de cada linha usando as chaves dos dicionários correspondentes aos nomes das colunas.

O uso de `DictWriter` e `DictReader` torna a leitura e escrita de dados CSV mais legível e mais fácil de trabalhar, especialmente quando você tem dados CSV com muitas colunas ou precisa realizar manipulações complexas em seus dados tabulares.

## Biblioteca Random

A biblioteca `random` no Python é um módulo embutido que fornece funcionalidades para gerar números aleatórios. Essa biblioteca é amplamente utilizada em uma variedade de aplicações, desde jogos até simulações e análises estatísticas. Aqui estão algumas das principais funções e recursos oferecidos pela biblioteca `random`:

1. Geração de Números Aleatórios:
   - `random.random()`: Retorna um número de ponto flutuante no intervalo [0, 1).

2. Geração de Inteiros Aleatórios:
   - `random.randint(a, b)`: Retorna um número inteiro no intervalo [a, b], incluindo ambos os limites.
   - `random.randrange(start, stop, step)`: Retorna um número aleatório a partir de um intervalo definido por `start`, `stop` e `step`.

3. Amostragem Aleatória:
   - `random.choice(sequence)`: Retorna um elemento aleatório de uma sequência.
   - `random.choices(population, weights=None, k=1)`: Retorna uma lista de `k` elementos amostrados aleatoriamente de uma população, com ou sem pesos.
   - `random.sample(population, k)`: Retorna uma lista de `k` elementos exclusivos amostrados aleatoriamente de uma população.

4. Embaralhamento de Sequências:
   - `random.shuffle(sequence)`: Embaralha uma sequência, como uma lista, de forma aleatória in-place.

5. Geradores de Números Aleatórios Personalizados:
   - `random.seed(seed)`: Define a semente (seed) para o gerador de números aleatórios, permitindo a reproducibilidade dos resultados.
   - `random.Random()`: Permite criar objetos `Random` personalizados para controle mais granular sobre a geração de números aleatórios.

6. Distribuições Estatísticas:
   - `random.uniform(a, b)`: Gera um número de ponto flutuante uniformemente distribuído no intervalo [a, b].
   - `random.gauss(mu, sigma)`: Gera números seguindo uma distribuição normal (gaussiana) com média `mu` e desvio padrão `sigma`.

A biblioteca `random` é útil para adicionar aleatoriedade aos seus programas e simulações. No entanto, é importante lembrar que os números gerados são pseudoaleatórios e dependem de uma semente inicial (seed). Portanto, se você precisar de resultados reproduzíveis, deve definir a semente usando `random.seed()`.

Aqui está um exemplo simples de como usar a biblioteca `random` para gerar um número inteiro aleatório:

```python
import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)
```

Este código gerará e imprimirá um número inteiro aleatório entre 1 e 100.

## Secrets -> Segurança

O módulo `secrets` no Python é uma biblioteca que oferece uma maneira segura de gerar números e sequências de caracteres aleatórios para aplicações que requerem alta segurança, como geração de senhas, tokens de autenticação, chaves de criptografia e similares. A principal diferença entre o módulo `secrets` e o módulo `random` é que o `secrets` é projetado para ser criptograficamente seguro, enquanto o `random` é mais adequado para fins não criptográficos.

Aqui estão algumas das funções e recursos oferecidos pelo módulo `secrets`:

1. Geração de Sequências Aleatórias:
   - `secrets.randbelow(n)`: Gera um número inteiro aleatório no intervalo [0, n), de forma criptograficamente segura.

2. Geração de Bytes Aleatórios:
   - `secrets.token_bytes(n)`: Gera `n` bytes aleatórios seguros.

3. Geração de Strings Aleatórios:
   - `secrets.token_hex(nbytes=None)`: Gera uma string hexadecimal aleatória de `nbytes` bytes ou de tamanho padrão se `nbytes` não for especificado.
   - `secrets.token_urlsafe(nbytes=None)`: Gera uma string aleatória adequada para uso em URLs, de `nbytes` bytes ou de tamanho padrão se `nbytes` não for especificado.

4. Geração de Senhas Seguras:
   - `secrets.choice(seq)`: Escolhe um elemento aleatório de uma sequência.
   - `secrets.randbits(k)`: Gera `k` bits aleatórios seguros como um número inteiro.

O módulo `secrets` é particularmente útil em cenários nos quais a segurança é uma preocupação primordial. Ele usa fontes de entropia do sistema operacional subjacente para gerar números e sequências aleatórios, tornando-os adequados para criptografia e autenticação. Além disso, o módulo `secrets` é uma escolha melhor do que o módulo `random` para a geração de senhas, uma vez que os resultados gerados são menos previsíveis e mais seguros.

Aqui está um exemplo simples de como usar o módulo `secrets` para gerar uma senha segura:

```python
import secrets
import string

# Defina os caracteres possíveis para a senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gere uma senha segura com 12 caracteres
senha_segura = ''.join(secrets.choice(caracteres) for _ in range(12))
print(senha_segura)
```

Este código irá gerar uma senha aleatória de 12 caracteres que inclui letras maiúsculas, letras minúsculas, dígitos e caracteres especiais.

## Locale lib

A biblioteca locale em Python fornece serviços de internacionalização, permitindo que os programas Python sejam adaptados para diferentes idiomas e regiões.

A biblioteca define um conjunto de variáveis ​​globais que representam as configurações de localidade atuais, como o idioma, o fuso horário e o sistema de numeração. Essas variáveis ​​podem ser usadas para formatar e interpretar dados de acordo com as convenções locais.

A biblioteca também fornece funções para manipular as configurações de localidade. Por exemplo, a função `setlocale()` pode ser usada para definir as configurações de localidade atuais.

A seguir, alguns exemplos de como usar a biblioteca locale em Python:

```python
# Define as configurações de localidade para o Brasil
locale.setlocale(locale.LC_ALL, "pt_BR")

# Formata uma data de acordo com as convenções locais
print(datetime.date.today().strftime("%d/%m/%Y"))
# Saída: 11/10/2023

# Interpreta uma string de acordo com as convenções locais
print(locale.atoi("1.234.567,89"))
# Saída: 123456789
```

Alguns dos recursos disponíveis na biblioteca locale incluem:

* Formatação de datas, números e moedas
* Localização de mensagens de erro
* Internacionalização de interfaces gráficas de usuário

A biblioteca locale é um recurso importante para programadores Python que desejam criar aplicativos que sejam compatíveis com diferentes idiomas e regiões.

Aqui estão alguns exemplos de como a biblioteca locale pode ser usada em aplicativos Python:

* Um aplicativo de comércio eletrônico pode usar a biblioteca locale para exibir preços em moeda local.
* Um aplicativo de mensagens pode usar a biblioteca locale para traduzir mensagens para diferentes idiomas.
* Um aplicativo de viagem pode usar a biblioteca locale para exibir informações de fuso horário e clima.

A biblioteca locale é um recurso poderoso que pode ser usado para tornar os aplicativos Python mais abrangentes e acessíveis a um público global.

## Variáveis de ambiente

Vou descrever as bibliotecas `os.getenv`, `os.environ` e `python-dotenv` em Python:

1. `os.getenv`:
   - `os.getenv` é uma função da biblioteca padrão `os` em Python que permite acessar variáveis de ambiente do sistema operacional. Ela é usada para recuperar o valor de uma variável de ambiente específica.
   - Sintaxe: `os.getenv(nome_da_variável, valor_padrão)`
   - `nome_da_variável` é o nome da variável de ambiente que você deseja recuperar.
   - `valor_padrão` (opcional) é o valor que será retornado se a variável de ambiente não estiver definida.

   Exemplo:
   ```python
   import os

   valor = os.getenv('VARIAVEL_DE_AMBIENTE', 'Valor_Padrão')
   print(valor)
   ```

2. `os.environ`:
   - `os.environ` é um dicionário que representa todas as variáveis de ambiente disponíveis no sistema operacional no qual o Python está sendo executado. Você pode acessar as variáveis de ambiente diretamente através desse dicionário.
   - `os.environ` fornece um mapeamento de nomes de variáveis de ambiente para seus valores.
   
   Exemplo:
   ```python
   import os

   # Acessando uma variável de ambiente específica
   valor = os.environ['VARIAVEL_DE_AMBIENTE']
   print(valor)

   # Listando todas as variáveis de ambiente
   for chave, valor in os.environ.items():
       print(f'{chave}: {valor}')
   ```

3. `python-dotenv`:
   - `python-dotenv` é uma biblioteca Python que facilita o carregamento de variáveis de ambiente a partir de arquivos de configuração, como o formato `.env`. Isso é útil para manter informações sensíveis ou configurações em um arquivo separado e carregá-las em seu aplicativo de maneira segura.
   - Para usar `python-dotenv`, você precisa instalar a biblioteca e criar um arquivo `.env` com suas variáveis de ambiente.

   Exemplo de arquivo `.env`:
   ```
   API_KEY=your_api_key
   DEBUG=True
   SECRET_KEY=my_secret_key
   ```

   Exemplo de uso em Python:
   ```python
   from dotenv import load_dotenv

   # Carrega as variáveis de ambiente do arquivo .env
   load_dotenv()

   import os

   # Acesse as variáveis de ambiente carregadas
   api_key = os.getenv('API_KEY')
   debug = os.getenv('DEBUG')
   secret_key = os.getenv('SECRET_KEY')

   print(api_key, debug, secret_key)
   ```

   O `python-dotenv` ajuda a manter as configurações do seu aplicativo separadas do código-fonte e a facilitar a configuração e a manutenção de variáveis de ambiente em diferentes ambientes, como desenvolvimento, teste e produção.
