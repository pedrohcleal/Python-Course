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
