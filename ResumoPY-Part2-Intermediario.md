### Parte 2

# Dict

Em Python, o tipo de dados "dict" (dicionário) é uma estrutura de dados extremamente útil e versátil. Ele é usado para armazenar coleções de pares chave-valor, em que cada chave deve ser única. Os dicionários são conhecidos como "hash maps" ou "hash tables" em outras linguagens de programação.

A principal característica distintiva de um dicionário é que ele permite acessar os valores associados às chaves de forma muito eficiente. Em vez de usar um índice numérico, como em listas ou tuplas, os dicionários utilizam as chaves para acessar os valores correspondentes.

Aqui está um exemplo de como criar um dicionário em Python:

```python
# Criando um dicionário vazio
meu_dict = {}

# Ou usando a função built-in dict()
meu_dict = dict()

# Criando um dicionário com pares chave-valor
meu_dict = {"chave1": valor1, "chave2": valor2, "chave3": valor3}
```

As chaves em um dicionário podem ser de qualquer tipo imutável, como strings, números, tuplas, etc. Os valores podem ser de qualquer tipo de dados, incluindo listas, dicionários e objetos personalizados.

Principais características dos dicionários em Python:

1. Acesso aos elementos: Os elementos de um dicionário são acessados utilizando as chaves como índices:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

print(meu_dict["idade"])  # Saída: 30
print(meu_dict["nome"])   # Saída: João
print(meu_dict["cidade"]) # Saída: São Paulo
```

2. Inclusão e atualização de elementos: É possível adicionar novos pares chave-valor ao dicionário ou atualizar os valores existentes:

```python
# Adicionando um novo par chave-valor
meu_dict["profissão"] = "Engenheiro"

# Atualizando o valor associado a uma chave existente
meu_dict["idade"] = 31
```

3. Remoção de elementos: Os elementos podem ser removidos através do uso da palavra-chave "del" ou do método "pop":

```python
# Removendo uma chave específica
del meu_dict["cidade"]

# Removendo e obtendo o valor de uma chave específica
valor_removido = meu_dict.pop("idade")
```

4. Verificação de existência de uma chave: É possível verificar se uma chave existe no dicionário usando a palavra-chave "in":

```python
if "nome" in meu_dict:
    print("A chave 'nome' existe no dicionário.")
```

5. Tamanho do dicionário: Para obter o número de pares chave-valor em um dicionário, pode-se usar a função len():

```python
tamanho = len(meu_dict)
```

Os dicionários são amplamente utilizados em Python e são extremamente úteis para mapear e organizar dados de maneira eficiente e flexível. Sua flexibilidade e facilidade de uso os tornam uma escolha popular para resolver uma variedade de problemas de programação.
