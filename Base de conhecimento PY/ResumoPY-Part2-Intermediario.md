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

1. `dict.get(key, default=None)`:

```python
my_dict = {"apple": 2, "orange": 3}
apple_value = my_dict.get("apple")
print(apple_value)  # Saída: 2

grape_value = my_dict.get("grape", 0)
print(grape_value)  # Saída: 0 (chave "grape" não existe, então retorna o valor padrão 0)
```

2. `dict.keys()`:

```python
my_dict = {"apple": 2, "orange": 3}
keys_list = my_dict.keys()
print(keys_list)  # Saída: dict_keys(['apple', 'orange'])
```

3. `dict.values()`:

```python
my_dict = {"apple": 2, "orange": 3}
values_list = my_dict.values()
print(values_list)  # Saída: dict_values([2, 3])
```

4. `dict.items()`:

```python
my_dict = {"apple": 2, "orange": 3}
items_list = my_dict.items()
print(items_list)  # Saída: dict_items([('apple', 2), ('orange', 3)])
```

5. `dict.pop(key, default=None)`:

```python
my_dict = {"apple": 2, "orange": 3}
orange_value = my_dict.pop("orange")
print(orange_value)  # Saída: 3

grape_value = my_dict.pop("grape", 0)
print(grape_value)  # Saída: 0 (chave "grape" não existe, então retorna o valor padrão 0)
```

6. `dict.popitem()`:

```python
my_dict = {"apple": 2, "orange": 3, "banana": 1}
item = my_dict.popitem()
print(item)  # Saída: ('banana', 1) ou ('apple', 2) ou ('orange', 3) - um par aleatório é retornado e removido do dicionário
```

7. `dict.clear()`:

```python
my_dict = {"apple": 2, "orange": 3}
my_dict.clear()
print(my_dict)  # Saída: {}
```

8. `dict.update(other_dict)`:

```python
my_dict = {"apple": 2, "orange": 3}
other_dict = {"banana": 1, "grape": 4}
my_dict.update(other_dict)
print(my_dict)  # Saída: {'apple': 2, 'orange': 3, 'banana': 1, 'grape': 4}
```

9. `dict.setdefault(key, default=None)`:

```python
my_dict = {"apple": 2, "orange": 3}
grape_value = my_dict.setdefault("grape", 0)
print(grape_value)  # Saída: 0 (chave "grape" não existe, então insere a chave com o valor padrão 0)

banana_value = my_dict.setdefault("banana", 5)
print(banana_value)  # Saída: 5 (chave "banana" já existe, retorna o valor existente 5)
```

10. `dict.fromkeys(keys, value=None)`:

```python
keys_list = ["apple", "orange", "banana"]
my_dict = dict.fromkeys(keys_list, 0)
print(my_dict)  # Saída: {'apple': 0, 'orange': 0, 'banana': 0}

my_dict = dict.fromkeys(keys_list)
print(my_dict)  # Saída: {'apple': None, 'orange': None, 'banana': None}
```

11. `dict.copy()`:

```python
my_dict = {"apple": 2, "orange": 3}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Saída: {'apple': 2, 'orange': 3}
```

## Shallow Copy & Deep Copy

Em Python, os conceitos de "shallow copy" (cópia superficial) e "deep copy" (cópia profunda) referem-se à forma como os dicionários (dicts) são copiados ou clonados. Vamos entender as diferenças entre eles:

**Shallow Copy (Cópia Superficial):**
Uma shallow copy de um dicionário cria uma nova cópia do dicionário, mas os valores internos (objetos) não são copiados. Em vez disso, os objetos originais são referenciados na nova cópia. Isso significa que a nova cópia do dicionário compartilha as mesmas referências de objetos que o dicionário original. Portanto, alterações nos objetos internos dentro do dicionário copiado serão refletidas no dicionário original e vice-versa.

Em Python, podemos fazer uma shallow copy usando o método `.copy()` ou a função `copy.copy()` do módulo `copy`.

Exemplo de shallow copy:

```python
import copy

original_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
shallow_copied_dict = original_dict.copy()

# Modificando o valor dentro da cópia
shallow_copied_dict['a'][0] = 100

print(original_dict)      # Output: {'a': [100, 2, 3], 'b': [4, 5, 6]}
print(shallow_copied_dict) # Output: {'a': [100, 2, 3], 'b': [4, 5, 6]}
```

**Deep Copy (Cópia Profunda):**
Uma deep copy de um dicionário cria uma nova cópia do dicionário e também copia todos os objetos internos, criando novas referências independentes. Dessa forma, alterações nos objetos internos dentro do dicionário copiado não afetarão o dicionário original e vice-versa.

Em Python, podemos fazer uma deep copy usando a função `copy.deepcopy()` do módulo `copy`.

Exemplo de deep copy:

```python
import copy

original_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
deep_copied_dict = copy.deepcopy(original_dict)

# Modificando o valor dentro da cópia
deep_copied_dict['a'][0] = 100

print(original_dict)   # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}
print(deep_copied_dict) # Output: {'a': [100, 2, 3], 'b': [4, 5, 6]}
```

Portanto, ao usar uma deep copy, você obtém uma cópia totalmente independente do dicionário original, garantindo que quaisquer alterações feitas na cópia não afetem o original e vice-versa.

## Sets

Em Python, um set (conjunto) é uma coleção de elementos não ordenada, não indexada e que não permite elementos duplicados. Ele é definido usando chaves `{}` e pode conter elementos de diferentes tipos de dados, como inteiros, strings, floats, entre outros.

Principais características dos sets em Python:

1. Elementos únicos: Os sets não podem conter elementos duplicados. Se você tentar adicionar um elemento que já existe no conjunto, ele será ignorado.

2. Desordem: Os elementos dentro de um set não possuem uma ordem específica. Isso significa que você não pode acessá-los por meio de índices, como em listas ou tuplas.

3. Mutabilidade: Os sets são mutáveis, o que significa que você pode adicionar e remover elementos depois de criá-los.

4. Imutabilidade dos elementos: Os elementos dentro do set devem ser imutáveis, ou seja, você não pode ter listas ou outros sets como elementos, mas pode ter tuplas, inteiros, strings, entre outros.

Aqui estão algumas operações comuns que você pode realizar com sets em Python:

1. Criar um set:
```python
meu_set = {1, 2, 3, 4}
```

2. Adicionar elementos:
```python
meu_set.add(5)
```

3. Remover elementos:
```python
meu_set.remove(3)
```

4. Verificar se um elemento está no set:
```python
if 4 in meu_set:
    print("O elemento 4 está no set.")
```

5. União de sets:
```python
outro_set = {3, 4, 5, 6}
uniao = meu_set.union(outro_set)
# ou simplesmente: uniao = meu_set | outro_set
```

6. Interseção de sets:
```python
intersecao = meu_set.intersection(outro_set)
# ou simplesmente: intersecao = meu_set & outro_set
```

7. Diferença entre sets:
```python
diferenca = meu_set.difference(outro_set)
# ou simplesmente: diferenca = meu_set - outro_set
```

8. Verificar se um set é subconjunto de outro:
```python
e_subconjunto = meu_set.issubset(outro_set)
# ou simplesmente: e_subconjunto = meu_set <= outro_set
```

Sets podem ser uma ótima escolha quando você precisa garantir que não haja elementos duplicados em uma coleção e não precisa de uma ordem específica para os elementos. Eles também podem ser úteis para realizar operações matemáticas de conjuntos, como uniões, interseções e diferenças.
