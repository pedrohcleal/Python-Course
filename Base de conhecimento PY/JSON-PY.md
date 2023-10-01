# Manipulação de json com Python

## Introdução
JSON (JavaScript Object Notation) é um formato de dados amplamente utilizado para armazenar e transmitir informações estruturadas de forma legível por humanos e facilmente interpretável por máquinas. Em Python, você pode trabalhar com JSON usando a biblioteca padrão `json`.

Aqui estão as principais operações que você pode realizar com JSON em Python:

1. **Serialização (Encode)**: Converter objetos Python em formato JSON.
   - Para serializar um objeto Python em JSON, você pode usar a função `json.dumps()`. Por exemplo:
   
     ```python
     import json
     
     data = {
         "nome": "John",
         "idade": 30,
         "cidade": "Nova York"
     }
     
     json_data = json.dumps(data)
     print(json_data)
     ```

   Isso produzirá uma representação JSON da estrutura de dados `data`.

2. **Deserialização (Decode)**: Converter dados JSON em objetos Python.
   - Para converter uma string JSON de volta para um objeto Python, você pode usar a função `json.loads()`. Por exemplo:

     ```python
     json_data = '{"nome": "John", "idade": 30, "cidade": "Nova York"}'
     
     data = json.loads(json_data)
     print(data)
     ```

   Isso transformará a string JSON em um dicionário Python.

3. **Leitura e Escrita de Arquivos JSON**: Você pode ler e escrever dados JSON em arquivos.
   - Para escrever dados JSON em um arquivo:

     ```python
     with open('dados.json', 'w') as arquivo:
         json.dump(data, arquivo)
     ```

   - Para ler dados JSON de um arquivo:

     ```python
     with open('dados.json', 'r') as arquivo:
         data = json.load(arquivo)
     ```

4. **Trabalhando com Tipos de Dados Customizados**: O módulo `json` pode serializar tipos de dados Python padrão, como dicionários, listas, strings, números, entre outros. No entanto, para tipos de dados personalizados, você pode criar funções de serialização personalizadas usando a classe `JSONEncoder` e `JSONDecoder`.

   ```python
   import json

   class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade

   def pessoa_para_dict(pessoa):
       return {"nome": pessoa.nome, "idade": pessoa.idade}

   def dict_para_pessoa(d):
       return Pessoa(d["nome"], d["idade"])

   data = [Pessoa("Alice", 25), Pessoa("Bob", 30)]

   json_data = json.dumps(data, default=pessoa_para_dict)
   decoded_data = json.loads(json_data, object_hook=dict_para_pessoa)
   ```

Isso é um resumo das operações básicas com JSON em Python. A biblioteca `json` torna simples a tarefa de lidar com dados JSON, permitindo que você integre facilmente sistemas que compartilham informações nesse formato.

## Modos
Em Python, ao trabalhar com arquivos, os modos são parâmetros que você pode passar para a função `open()` para especificar como o arquivo será aberto e manipulado. Os modos determinam se você está lendo, escrevendo, acrescentando ou executando outras operações no arquivo. Aqui estão os principais modos de abertura de arquivo:

1. Modo de Leitura (`'r'`): Este é o modo padrão de abertura de arquivo. Ele permite que você leia o conteúdo do arquivo. Se o arquivo não existir, uma exceção `FileNotFoundError` será levantada.

2. Modo de Escrita (`'w'`): Este modo permite escrever no arquivo. Se o arquivo já existir, seu conteúdo anterior será substituído. Se o arquivo não existir, ele será criado.

3. Modo de Acrescentar (`'a'`): Ao abrir o arquivo neste modo, você pode acrescentar (adicionar) conteúdo ao final do arquivo. Se o arquivo não existir, ele será criado.

4. Modo de Leitura e Escrita (`'r+'`): Este modo permite tanto a leitura quanto a escrita no arquivo. O arquivo é aberto para leitura e escrita simultaneamente.

5. Modo de Escrita e Leitura (`'w+'`): Semelhante ao modo `'r+'`, mas com a diferença de que o arquivo é truncado (se existir) e aberto para escrita e leitura.

6. Modo de Acrescentar e Leitura (`'a+'`): Semelhante ao modo `'a'`, mas permite tanto a leitura quanto a escrita. O arquivo é aberto para acrescentar e ler.

Além desses modos básicos, existem também variações que lidam com arquivos binários:

- Adicione `'b'` ao modo para trabalhar com arquivos binários. Por exemplo: `'rb'`, `'wb+'`, `'ab'`.

Por exemplo, para abrir um arquivo chamado "exemplo.txt" para leitura, você usaria:

```python
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
```

Ou para abrir um arquivo binário para escrita e leitura:

```python
with open("arquivo_binario", "wb+") as binario:
    binario.write(b"conteudo_binario")
    binario.seek(0)
    conteudo = binario.read()
```

Lembre-se de que ao usar o gerenciador de contexto `with`, o arquivo será fechado automaticamente quando sair do bloco `with`, independentemente do modo de abertura utilizado..

## Métodos
Quando você abre um arquivo em Python usando a função `open()`, o objeto retornado possui diversos métodos que permitem interagir com o arquivo de várias maneiras. Aqui estão alguns dos métodos mais comuns associados a objetos de arquivo:

1. `read(size=-1)`: Lê e retorna o conteúdo do arquivo como uma string. Se o argumento `size` for especificado, apenas essa quantidade de caracteres será lida. Se `size` não for especificado ou for negativo, o arquivo inteiro é lido. 

2. `readline()`: Lê e retorna uma linha do arquivo como uma string. A próxima linha é lida a cada chamada subsequente.

3. `readlines()`: Lê todas as linhas do arquivo e retorna uma lista de strings, onde cada string representa uma linha.

4. `write(string)`: Escreve a string fornecida no arquivo. Retorna o número de caracteres escritos.

5. `writelines(lines)`: Escreve uma lista de strings no arquivo. Cada string representa uma linha. Não adiciona automaticamente quebras de linha entre as linhas, então você deve incluí-las se necessário.

6. `seek(offset, whence=0)`: Move a posição do "cursor" de leitura/escrita no arquivo. O argumento `offset` define o deslocamento em relação ao ponto de referência especificado por `whence`. Os valores possíveis para `whence` são 0 (início do arquivo), 1 (posição atual) e 2 (fim do arquivo).

7. `tell()`: Retorna a posição atual do cursor no arquivo.

8. `close()`: Fecha o arquivo, liberando os recursos associados a ele.

9. `flush()`: Força a gravação de qualquer conteúdo em buffer para o arquivo.

10. `truncate(size=None)`: Reduz o tamanho do arquivo para `size` bytes. Se o tamanho não for especificado, o arquivo será truncado na posição atual do cursor.

11. `__enter__()` e `__exit__()`: Esses métodos especiais permitem que o objeto de arquivo seja usado como um gerenciador de contexto usando o bloco `with`. O método `__enter__()` pode ser usado para configurar o contexto (por exemplo, abrir o arquivo), e o método `__exit__()` pode ser usado para liberar recursos (por exemplo, fechar o arquivo).

Aqui está um exemplo de uso de alguns desses métodos:

```python
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("novo_arquivo.txt", "w") as novo_arquivo:
    novo_arquivo.write("Olá, mundo!\n")
    novo_arquivo.write("Essa é uma nova linha.\n")
```

Lembrando que usar o bloco `with` é recomendado para garantir que o arquivo seja fechado corretamente após o uso.

## Conversão de dados JSON -> Python

Em Python, você pode converter dados JSON para tipos de dados Python usando o módulo `json`. O módulo `json` oferece funções para serializar (conversão de Python para JSON) e desserializar (conversão de JSON para Python) dados JSON. Aqui estão algumas das conversões mais comuns de JSON para tipos de dados Python:

1. **JSON para Dicionário (Python Dictionary):**
   
   Use `json.loads()` para converter um objeto JSON em um dicionário Python.

   ```python
   import json

   json_str = '{"nome": "João", "idade": 30}'
   data = json.loads(json_str)

   # Resultado: data é agora um dicionário Python
   ```

2. **JSON para Lista (Python List):**

   Use `json.loads()` para converter um array JSON em uma lista Python.

   ```python
   import json

   json_str = '[1, 2, 3, 4, 5]'
   data = json.loads(json_str)

   # Resultado: data é agora uma lista Python
   ```

3. **JSON para String:**

   Não é necessário converter explicitamente uma string JSON em uma string Python, pois as strings JSON são representadas como strings Python.

   ```python
   json_str = '"Isso é uma string JSON"'
   # json_str é uma string Python
   ```

4. **JSON para Número (int, float):**

   Use `json.loads()` para converter um número JSON em um número Python.

   ```python
   import json

   json_str = '42'
   data = json.loads(json_str)

   # Resultado: data é agora um número Python
   ```

5. **JSON para Booleano:**

   Use `json.loads()` para converter um valor JSON booleano em um valor Python booleano.

   ```python
   import json

   json_str = 'true'
   data = json.loads(json_str)

   # Resultado: data é agora True (booleano Python)
   ```

6. **JSON para None (Nulo):**

   Use `json.loads()` para converter o valor JSON nulo em `None` em Python.

   ```python
   import json

   json_str = 'null'
   data = json.loads(json_str)

   # Resultado: data é agora None (nulo Python)
   ```

Essas são as conversões básicas que você pode realizar ao converter dados JSON para tipos de dados Python. Lembre-se de que a estrutura e o tipo de dados no JSON devem corresponder ao que você espera para evitar erros durante a conversão.

## JSON - Salvando e carregando classe
### Salvar
Passo a passo como você pode salvar uma classe Python como um arquivo JSON de forma didática. Para fazer isso, você precisa seguir os seguintes passos:

Passo 1: Crie uma classe Python
Primeiro, crie uma classe Python que deseja salvar como JSON. Vamos criar um exemplo simples de uma classe chamada `Person` com atributos de nome e idade:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Passo 2: Crie uma instância da classe
Agora, crie uma instância da classe `Person` com alguns dados:

```python
person = Person("João", 30)
```

Passo 3: Converta a instância para um dicionário
Para salvar a classe como JSON, você precisa converter a instância da classe em um dicionário Python. Você pode fazer isso implementando um método na classe ou usando uma abordagem mais genérica, como esta:

```python
person_dict = vars(person)  # Converte a instância para um dicionário
```

Passo 4: Importe o módulo `json`
Certifique-se de que você tenha o módulo `json` importado em seu código. O módulo `json` é necessário para lidar com operações JSON em Python.

```python
import json
```

Passo 5: Salve o dicionário como um arquivo JSON
Agora que você tem o dicionário `person_dict`, você pode salvá-lo como um arquivo JSON usando o método `dump` do módulo `json`. Certifique-se de especificar um nome de arquivo válido e o modo de abertura (por exemplo, 'w' para escrita).

```python
with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)
```

Aqui está o código completo:

```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("João", 30)
person_dict = vars(person)

with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)
```

Depois de executar este código, você terá um arquivo chamado `person.json` no mesmo diretório do seu script Python, contendo os dados da classe `Person` no formato JSON. Você pode ler este arquivo JSON mais tarde e reconstruir a instância da classe se desejar.

### Carregar:
Para carregar uma classe a partir de um arquivo JSON, você precisará seguir estes passos:

**Passo 1: Importe o módulo `json`**
Certifique-se de que você importou o módulo `json` em seu código para lidar com operações JSON em Python.

```python
import json
```

**Passo 2: Crie uma função para carregar a classe**
Crie uma função que recebe o nome do arquivo JSON como argumento e retorna uma instância da classe com base nos dados do arquivo JSON. A função deve abrir o arquivo JSON, carregar os dados e, em seguida, criar uma instância da classe com esses dados.

Aqui está um exemplo de função que faz isso:

```python
def load_person_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        person = Person(**data)  # Cria uma instância da classe com os dados do JSON
        return person
```

**Passo 3: Use a função para carregar a classe**
Agora você pode usar a função `load_person_from_json` para carregar uma instância da classe `Person` a partir do arquivo JSON. Certifique-se de que o arquivo JSON existe no mesmo diretório ou forneça o caminho completo para o arquivo.

```python
loaded_person = load_person_from_json('person.json')
print(f"Nome: {loaded_person.name}, Idade: {loaded_person.age}")
```

Aqui está o código completo, incluindo a função de carregamento:

```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def load_person_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        person = Person(**data)
        return person

loaded_person = load_person_from_json('person.json')
print(f"Nome: {loaded_person.name}, Idade: {loaded_person.age}")
```

Ao executar este código, ele carregará os dados do arquivo JSON `person.json` e criará uma instância da classe `Person` com esses dados, permitindo que você acesse e utilize os atributos da classe normalmente. Certifique-se de que o arquivo JSON tenha a mesma estrutura esperada para a classe `Person` para que a reconstrução funcione corretamente.

## TextIOWrapper

`TextIOWrapper` é uma classe em Python que fornece uma interface para trabalhar com arquivos de texto. Você pode criar um arquivo e escrever nele usando métodos úteis da classe `TextIOWrapper`. Aqui estão os passos para criar um arquivo e escrever nele:

1. **Abra o arquivo para escrita**:

   Você pode usar a função `open()` para criar um arquivo em modo de escrita. O modo de escrita é representado pelo argumento `"w"`.

   ```python
   with open('arquivo.txt', 'w') as arquivo:
       # Aqui você pode escrever no arquivo
   ```

2. **Escreva no arquivo**:

   Agora que você abriu o arquivo, pode escrever nele usando métodos da classe `TextIOWrapper`, como `write()` ou `writelines()`. Aqui estão alguns exemplos:

   - **`write()`**: Escreve uma string no arquivo.

     ```python
     with open('arquivo.txt', 'w') as arquivo:
         arquivo.write('Este é um exemplo de escrita em arquivo.\n')
     ```

   - **`writelines()`**: Escreve uma lista de strings no arquivo, cada elemento da lista se torna uma linha no arquivo.

     ```python
     linhas = ['Linha 1\n', 'Linha 2\n', 'Linha 3\n']
     with open('arquivo.txt', 'w') as arquivo:
         arquivo.writelines(linhas)
     ```

3. **Feche o arquivo automaticamente**:

   Usar o bloco `with` como mostrado nos exemplos acima é uma prática recomendada, pois ele garante que o arquivo seja fechado automaticamente após o bloco `with`. Isso é importante para garantir que os recursos do sistema sejam gerenciados adequadamente e que as alterações sejam gravadas no arquivo.

4. **Manipulação de exceções**:

   Lembre-se de lidar com exceções ao trabalhar com arquivos, pois podem ocorrer erros durante a escrita, como falta de espaço em disco ou permissões insuficientes. Você pode usar um bloco `try...except` para capturar e lidar com exceções, se necessário.

   ```python
   try:
       with open('arquivo.txt', 'w') as arquivo:
           arquivo.write('Este é um exemplo de escrita em arquivo.\n')
   except IOError as e:
       print(f"Erro ao escrever no arquivo: {e}")
   ```

Certifique-se de adaptar o código acima para suas necessidades específicas. Com esses passos, você pode criar um arquivo e escrever nele de forma eficiente em Python usando a classe `TextIOWrapper`.

## Enconding

No contexto de manipulação de texto e arquivos, "encoding" se refere à forma como os caracteres de um conjunto de caracteres (como ASCII, UTF-8, ISO-8859-1, etc.) são representados e armazenados em bytes. O encoding é essencial para garantir que o texto seja interpretado corretamente, especialmente ao ler ou escrever em diferentes sistemas, idiomas e plataformas.

Aqui estão algumas considerações importantes relacionadas ao encoding no contexto de programação:

1. **UTF-8 é amplamente recomendado**: UTF-8 é um dos encodings mais comuns e é altamente recomendado para uso na maioria das situações. Ele suporta uma ampla variedade de caracteres, incluindo caracteres não latinos (por exemplo, caracteres chineses, árabes, etc.). É o padrão de facto na web e em muitas linguagens de programação, incluindo Python.

2. **Escolha do Encoding**: Ao trabalhar com texto, é importante escolher o encoding correto para a tarefa em questão. Você deve estar ciente do encoding usado para ler ou escrever arquivos e dados, pois isso afetará a forma como os caracteres são interpretados. Em Python, ao abrir um arquivo, você pode especificar o encoding usando o argumento `encoding` da função `open()`.

   ```python
   with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
       arquivo.write('Texto em UTF-8: Olá, mundo!')
   ```

3. **Decodificação e Codificação**: Decodificação é o processo de converter bytes em texto, enquanto codificação é o processo de converter texto em bytes. Você geralmente faz a decodificação ao ler dados de um arquivo e a codificação ao escrever dados em um arquivo.

   ```python
   # Lendo dados de um arquivo com decodificação
   with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
       texto = arquivo.read()
   
   # Escrevendo dados em um arquivo com codificação
   with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
       arquivo.write('Texto em UTF-8: Olá, mundo!')
   ```

4. **Erros de Encoding**: Às vezes, você pode encontrar problemas de encoding ao lidar com dados que não correspondem ao encoding especificado. Isso pode resultar em erros de codificação/descodificação. É importante tratar esses erros adequadamente usando as opções apropriadas, como `errors='ignore'` para ignorar caracteres inválidos ou `errors='replace'` para substituí-los.

   ```python
   with open('arquivo.txt', 'r', encoding='utf-8', errors='ignore') as arquivo:
       texto = arquivo.read()
   ```

Em resumo, entender e gerenciar encoding é crucial ao lidar com texto em programação, pois isso garante que os dados sejam interpretados corretamente, evitando problemas de caracteres inválidos e garantindo a portabilidade de seus aplicativos em diferentes ambientes e idiomas. UTF-8 é geralmente a escolha recomendada de encoding devido à sua capacidade de suportar uma ampla gama de caracteres.

## Sobre 'ensure_ascii' & 'indent'

`ensure_ascii` e `indent` são parâmetros opcionais que podem ser usados ao serializar um objeto Python em formato JSON usando a função `json.dump()` ou `json.dumps()` da biblioteca padrão `json` em Python.

1. **`ensure_ascii`**:

   - O parâmetro `ensure_ascii` é um parâmetro booleano que controla se os caracteres não-ASCII devem ser escapados (codificados) como sequências de escape Unicode ou não ao serializar em JSON.
   - Se `ensure_ascii` for definido como `True` (o padrão), os caracteres não-ASCII serão escapados, ou seja, representados como sequências de escape Unicode, garantindo que o JSON resultante seja ASCII válido.
   - Se `ensure_ascii` for definido como `False`, os caracteres não-ASCII serão incluídos diretamente no JSON sem serem escapados, resultando em um JSON que pode conter caracteres não-ASCII.
   - Use `ensure_ascii=False` quando você quiser preservar caracteres não-ASCII em seu JSON, mas esteja ciente de que isso pode não ser compatível com todos os parsers JSON.

   Exemplo:

   ```python
   import json

   dados = {"nome": "José", "idade": 30}
   
   # Com ensure_ascii=True (padrão)
   json_com_ensure_ascii = json.dumps(dados, ensure_ascii=True)
   # Resultado: '{"nome": "Jos\u00e9", "idade": 30}'

   # Com ensure_ascii=False
   json_sem_ensure_ascii = json.dumps(dados, ensure_ascii=False)
   # Resultado: '{"nome": "José", "idade": 30}'
   ```

2. **`indent`**:

   - O parâmetro `indent` é usado para controlar a formatação (indentação) do JSON resultante, tornando-o mais legível para os humanos. Ele define o número de espaços ou caracteres de tabulação usados para cada nível de aninhamento no JSON.
   - Se `indent` for definido como `None` (o padrão), o JSON será compacto, sem espaços em branco adicionais.
   - Se `indent` for um número inteiro, esse número de espaços em branco será usado para indentar cada nível de aninhamento no JSON.
   - Se `indent` for uma string, essa string será usada para indentação em cada nível.

   Exemplo:

   ```python
   import json

   dados = {"nome": "Alice", "idade": 25}

   # JSON compacto (sem indentação)
   json_compacto = json.dumps(dados, indent=None)
   # Resultado: '{"nome": "Alice", "idade": 25}'

   # JSON com indentação usando 4 espaços
   json_com_indentacao = json.dumps(dados, indent=4)
   # Resultado:
   # '{
   #     "nome": "Alice",
   #     "idade": 25
   # }'

   # JSON com indentação usando uma tabulação
   json_com_tabulacao = json.dumps(dados, indent='\t')
   # Resultado:
   # '{
   #     "nome": "Alice",
   #     "idade": 25
   # }'
   ```

O uso desses parâmetros é útil para controlar a aparência e a representação de JSON gerado a partir de objetos Python, tornando-o mais adequado para leitura e depuração por humanos ou adaptando-o às necessidades de parsers JSON específicos.


