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
