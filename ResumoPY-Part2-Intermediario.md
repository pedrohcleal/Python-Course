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

## Manipução de Dict:

Em Python, os dicionários são uma estrutura de dados poderosa e versátil que permite diversas manipulações para adicionar, modificar, acessar e remover elementos. Abaixo estão algumas das principais manipulações que podem ser feitas em dicionários:

1. Acesso a elementos:

Para acessar os valores associados às chaves, basta utilizar a chave como índice:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

print(meu_dict["idade"])    # Saída: 30
print(meu_dict["nome"])     # Saída: João
print(meu_dict.get("cidade"))  # Saída: São Paulo (usando o método get())
```

2. Adicionar ou atualizar elementos:

Para adicionar um novo par chave-valor ou atualizar um valor existente:

```python
meu_dict = {"idade": 30, "nome": "João"}

# Adicionando um novo par chave-valor
meu_dict["cidade"] = "São Paulo"

# Atualizando o valor associado a uma chave existente
meu_dict["idade"] = 31
```

3. Remover elementos:

Para remover um par chave-valor específico:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

# Removendo uma chave específica
del meu_dict["cidade"]

# Removendo e obtendo o valor de uma chave específica
valor_removido = meu_dict.pop("idade")
```

4. Verificação de existência de uma chave:

Para verificar se uma chave existe no dicionário:

```python
meu_dict = {"idade": 30, "nome": "João"}

if "nome" in meu_dict:
    print("A chave 'nome' existe no dicionário.")
```

5. Iteração sobre chaves, valores e pares chave-valor:

É possível iterar sobre as chaves, valores ou pares chave-valor do dicionário usando loops:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

# Iteração sobre as chaves
for chave in meu_dict:
    print(chave)

# Iteração sobre os valores
for valor in meu_dict.values():
    print(valor)

# Iteração sobre os pares chave-valor
for chave, valor in meu_dict.items():
    print(f"Chave: {chave}, Valor: {valor}")
```

6. Limpar ou copiar o dicionário:

Para limpar todos os elementos do dicionário:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

meu_dict.clear()  # Limpar o dicionário
```

Para copiar o dicionário:

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

copia_dict = meu_dict.copy()  # Copiar o dicionário para 'copia_dict'
```

### Métodos úteis em Dict

1. `keys()`: Retorna uma visão (view) dos objetos-chave no dicionário.

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

chaves = meu_dict.keys()
print(chaves)  # Saída: dict_keys(['idade', 'nome', 'cidade'])
```

2. `values()`: Retorna uma visão (view) dos valores no dicionário.

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

valores = meu_dict.values()
print(valores)  # Saída: dict_values([30, 'João', 'São Paulo'])
```

3. `items()`: Retorna uma visão (view) de tuplas contendo pares chave-valor no dicionário.

```python
meu_dict = {"idade": 30, "nome": "João", "cidade": "São Paulo"}

pares_chave_valor = meu_dict.items()
print(pares_chave_valor)  # Saída: dict_items([('idade', 30), ('nome', 'João'), ('cidade', 'São Paulo')])
```

4. `update()`: Mescla dois dicionários, adicionando pares chave-valor do dicionário passado como argumento.

```python
meu_dict = {"idade": 30, "nome": "João"}
outro_dict = {"cidade": "São Paulo", "profissão": "Engenheiro"}

meu_dict.update(outro_dict)
print(meu_dict)  # Saída: {'idade': 30, 'nome': 'João', 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}
```

5. `fromkeys()`: Cria um novo dicionário com chaves fornecidas e um valor padrão (opcional).

```python
chaves = ["idade", "nome", "cidade"]
valor_padrao = "N/A"

meu_dict = dict.fromkeys(chaves, valor_padrao)
print(meu_dict)  # Saída: {'idade': 'N/A', 'nome': 'N/A', 'cidade': 'N/A'}
```

6. `get()`: Retorna o valor associado a uma chave especificada. Se a chave não existir, retorna um valor padrão (opcional) em vez de gerar um erro.

```python
meu_dict = {"idade": 30, "nome": "João"}

valor = meu_dict.get("idade")
print(valor)  # Saída: 30

valor = meu_dict.get("profissão", "Desconhecida")
print(valor)  # Saída: Desconhecida
```

