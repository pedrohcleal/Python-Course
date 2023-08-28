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
## Packing e Unpacking das Dict
Em Python, o empacotamento (packing) e desempacotamento (unpacking) se referem a técnicas para manipular elementos em estruturas de dados, como dicionários (Dict), tuplas (Tuple) e listas (List), de uma maneira mais conveniente e eficiente. Vou focar especificamente no empacotamento e desempacotamento de dicionários (Dict).

**Empacotamento de Dicionários:**

O empacotamento de dicionários envolve criar um dicionário usando variáveis e valores existentes. Isso é útil quando você deseja criar um dicionário a partir de várias variáveis sem precisar definir explicitamente cada chave e valor.

```python
nome = "João"
idade = 30
cidade = "São Paulo"

pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
```

Neste exemplo, estamos empacotando as variáveis `nome`, `idade` e `cidade` em um dicionário chamado `pessoa`.

**Desempacotamento de Dicionários:**

O desempacotamento de dicionários permite extrair os valores associados às chaves do dicionário em variáveis individuais. Isso é especialmente útil quando você deseja trabalhar com os valores do dicionário de forma separada e mais legível.

```python
pessoa = {"nome": "Maria", "idade": 25, "cidade": "Rio de Janeiro"}

nome = pessoa["nome"]
idade = pessoa["idade"]
cidade = pessoa["cidade"]

print(nome, idade, cidade)
```

Em vez de acessar os valores do dicionário usando `pessoa["nome"]`, `pessoa["idade"]` e `pessoa["cidade"]` repetidamente, estamos desempacotando esses valores em variáveis separadas.

**Desempacotamento com `**` (Desempacotamento de Dicionário):**

Uma técnica avançada de desempacotamento envolve o uso do operador `**`, que permite desempacotar um dicionário diretamente em uma chamada de função. Isso é útil quando você deseja passar os elementos de um dicionário como argumentos nomeados para uma função.

```python
def saudacao(nome, idade, cidade):
    return f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}."

pessoa = {"nome": "Pedro", "idade": 28, "cidade": "Belo Horizonte"}

mensagem = saudacao(**pessoa)
print(mensagem)
```

Neste exemplo, o dicionário `pessoa` é desempacotado e seus valores são passados como argumentos nomeados para a função `saudacao`.

O empacotamento e desempacotamento são técnicas poderosas que tornam o código mais limpo, legível e eficiente, permitindo trabalhar com estruturas de dados complexas de maneira mais conveniente.

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

### Métodos em Sets:

Claro! Vamos adicionar informações sobre os métodos `update`, `clear` e `discard` aos sets em Python:

1. Método `update`:
O método `update` é usado para adicionar elementos de outro conjunto (ou qualquer outra coleção iterável) ao conjunto atual. Isso é semelhante à união dos conjuntos, mas, em vez de criar um novo conjunto, ele modifica o conjunto atual adicionando os elementos do conjunto passado como argumento.

Exemplo:
```python
meu_set = {1, 2, 3}
outro_set = {3, 4, 5}
meu_set.update(outro_set)
print(meu_set)  # Resultado: {1, 2, 3, 4, 5}
```

2. Método `clear`:
O método `clear` é usado para remover todos os elementos do conjunto, deixando-o vazio.

Exemplo:
```python
meu_set = {1, 2, 3, 4}
meu_set.clear()
print(meu_set)  # Resultado: set()
```

3. Método `discard`:
O método `discard` é usado para remover um elemento específico do conjunto. Se o elemento não estiver presente no conjunto, o método não gerará um erro (ao contrário do método `remove`, que gera um erro nessa situação).

Exemplo:
```python
meu_set = {1, 2, 3, 4}
meu_set.discard(3)
print(meu_set)  # Resultado: {1, 2, 4}

# Tentando remover um elemento inexistente
meu_set.discard(5)
print(meu_set)  # Resultado: {1, 2, 4} (não gera erro)
```
### operadores nos sets

Em Python, os sets possuem operadores que permitem realizar várias operações comuns entre conjuntos. Aqui estão os principais operadores utilizados com sets:

1. Operador de pertencimento `in`:
O operador `in` é usado para verificar se um elemento está presente em um conjunto.

Exemplo:
```python
meu_set = {1, 2, 3, 4}
print(2 in meu_set)  # Resultado: True
print(5 in meu_set)  # Resultado: False
```

2. Operador de não pertencimento `not in`:
O operador `not in` é usado para verificar se um elemento NÃO está presente em um conjunto.

Exemplo:
```python
meu_set = {1, 2, 3, 4}
print(2 not in meu_set)  # Resultado: False
print(5 not in meu_set)  # Resultado: True
```

3. Operadores de conjuntos: `union`, `intersection`, `difference`, `symmetric_difference`:
Esses operadores são usados para realizar operações matemáticas com conjuntos.

- `union` (ou `|`): Retorna um novo conjunto contendo todos os elementos presentes em ambos os conjuntos.
- `intersection` (ou `&`): Retorna um novo conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos.
- `difference` (ou `-`): Retorna um novo conjunto contendo os elementos presentes no primeiro conjunto, mas não no segundo.
- `symmetric_difference` (ou `^`): Retorna um novo conjunto contendo os elementos que estão em apenas um dos conjuntos.

Exemplo:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Resultado: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Resultado: {3}

difference_set = set1.difference(set2)
print(difference_set)  # Resultado: {1, 2}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Resultado: {1, 2, 4, 5}
```

4. Operadores de atualização: `update`, `intersection_update`, `difference_update`, `symmetric_difference_update`:
Esses operadores atualizam o conjunto atual com os resultados das operações de conjuntos correspondentes. Em vez de criar um novo conjunto, eles modificam o conjunto existente.

Exemplo:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Resultado: {1, 2, 3, 4, 5}

set1.intersection_update(set2)
print(set1)  # Resultado: {3}

set1.difference_update(set2)
print(set1)  # Resultado: set()

set1 = {1, 2, 3}
set1.symmetric_difference_update(set2)
print(set1)  # Resultado: {1, 2, 4, 5}
```

Esses operadores facilitam muito a manipulação e comparação de conjuntos em Python, permitindo que você realize operações comuns de conjuntos de forma eficiente e concisa.

Lembre-se de que o conjunto será modificado diretamente após a execução desses métodos, e os resultados refletirão as mudanças realizadas. Certifique-se de usar os métodos de acordo com suas necessidades específicas.

Sets podem ser uma ótima escolha quando você precisa garantir que não haja elementos duplicados em uma coleção e não precisa de uma ordem específica para os elementos. Eles também podem ser úteis para realizar operações matemáticas de conjuntos, como uniões, interseções e diferenças.
