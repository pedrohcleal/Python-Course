# Python Intermediário part 6

## filter()
A função `filter()` é outra função integrada em Python que permite filtrar elementos de uma sequência (como uma lista, tupla ou outro iterável) com base em uma função de teste. Ela retorna um iterador contendo os elementos da sequência original que passam no teste definido pela função.

A sintaxe básica da função `filter()` é a seguinte:

```python
filter(função_de_teste, sequência)
```

- `função_de_teste`: Uma função que define o critério de filtragem. Deve retornar `True` para os elementos que você deseja manter na sequência e `False` para os elementos que deseja filtrar.
- `sequência`: A sequência de elementos que você deseja filtrar.

Aqui está um exemplo simples de uso da função `filter()`:

```python
def é_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(é_par, numeros)
numeros_pares_lista = list(numeros_pares)  # Convertendo o iterador resultante em uma lista
print(numeros_pares_lista)  # Saída: [2, 4, 6, 8, 10]
```

No exemplo acima, a função `é_par()` é usada como critério de filtro. A função `filter()` aplica a função `é_par()` a cada elemento da lista `numeros`, retornando apenas os números pares.

Outra forma comum de usar `filter()` é com funções lambda (funções anônimas) para criar filtros simples:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(lambda x: x % 2 == 0, numeros)
numeros_pares_lista = list(numeros_pares)
print(numeros_pares_lista)  # Saída: [2, 4, 6, 8, 10]
```

A função `filter()` é útil quando você deseja extrair elementos de uma sequência com base em algum critério específico, economizando tempo e código comparado a loops explícitos de iteração.

## reduce()
A função `reduce()` também é uma função integrada em Python, mas, diferente das funções `map()` e `filter()`, ela não faz parte das funções built-in a partir do Python 3. A partir da versão 3, a função `reduce()` foi movida para o módulo `functools`, portanto, para usá-la, é necessário importá-la primeiro.

A função `reduce()` é projetada para acumular ou reduzir uma sequência de elementos a um único valor aplicando uma função repetidamente aos elementos da sequência. Ela foi inspirada por uma operação comum em programação funcional chamada "fold" ou "fold/reduce". A ideia é aplicar uma operação binária iterativa a todos os elementos da sequência, acumulando um resultado.

A sintaxe básica da função `reduce()` é a seguinte:

```python
functools.reduce(função, sequência, valor_inicial)
```

- `função`: Uma função que recebe dois argumentos e realiza a operação binária entre eles.
- `sequência`: A sequência de elementos que você deseja reduzir.
- `valor_inicial`: O valor inicial para o acumulador. Esse argumento é opcional.

Aqui está um exemplo simples de uso da função `reduce()`:

```python
from functools import reduce

def soma(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
soma_total = reduce(soma, numeros)
print(soma_total)  # Saída: 15 (1 + 2 + 3 + 4 + 5)
```

Neste exemplo, a função `soma()` é aplicada repetidamente aos elementos da lista `numeros`, acumulando um valor total.

Se você quiser fornecer um valor inicial para o acumulador, você pode fazer assim:

```python
soma_total_com_inicial = reduce(soma, numeros, 10)
print(soma_total_com_inicial)  # Saída: 25 (10 + 1 + 2 + 3 + 4 + 5)
```

A função `reduce()` pode ser poderosa para situações em que você precisa combinar todos os elementos de uma sequência usando uma operação específica, como cálculos matemáticos ou manipulação de dados. No entanto, observe que a função `reduce()` não é tão comum quanto as funções `map()` e `filter()`, pois sua funcionalidade pode muitas vezes ser atingida de maneira mais clara e legível com loops simples ou list comprehensions.

## Funções recursivas 

A recursão é um conceito fundamental na programação onde uma função se chama a si mesma para resolver um problema. A ideia é dividir um problema em subproblemas menores e, em seguida, resolver esses subproblemas, muitas vezes de forma idêntica à solução do problema original. No contexto do Python, as funções recursivas são aquelas que se invocam a si mesmas para realizar um determinado cálculo ou tarefa.

A recursividade é útil quando se lida com problemas que podem ser divididos em casos menores e semelhantes. Ela pode tornar o código mais elegante e conciso em alguns casos, mas também é importante usá-la com cuidado, pois pode levar a problemas de desempenho e até causar erros se não for usada corretamente.

Vamos dar uma olhada em um exemplo simples para entender como a recursão funciona em Python:

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120
```

Neste exemplo, a função `fatorial` calcula o fatorial de um número `n`. Ela se chama recursivamente para calcular o fatorial de `n - 1` até atingir o caso base onde `n` é igual a 0. A recursão acontece porque a função chama a si mesma durante a sua execução.

No entanto, é importante ter em mente que a recursão pode levar a problemas como estouro de pilha (quando há muitas chamadas aninhadas, esgotando a memória disponível), portanto, é aconselhável usar recursão com parcimônia e sempre garantir que haja um caso base para encerrar as chamadas recursivas.

Além disso, em alguns casos, a recursão pode ser menos eficiente do que uma abordagem iterativa (usando loops). Portanto, é bom considerar outras alternativas de implementação, dependendo do problema que você está resolvendo.

Em resumo, a recursão em Python permite que as funções chamem a si mesmas para resolver problemas divididos em subproblemas menores. É uma ferramenta poderosa, mas que deve ser usada com cuidado e atenção aos detalhes para evitar problemas de desempenho e lógicos.

## Context Manager with
Um "context manager" em Python é uma ferramenta que ajuda a gerenciar recursos, como arquivos, conexões de rede ou qualquer outro objeto que precise ser configurado e liberado de maneira apropriada. O gerenciamento adequado desses recursos é importante para evitar vazamentos de memória e garantir que eles sejam tratados corretamente, mesmo quando ocorrem exceções.

O gerenciador de contexto é definido usando os blocos `with` (com) em Python. Ele fornece um contexto no qual um objeto é criado e configurado no início do bloco `with`, e é automaticamente liberado (ou finalizado) no final do bloco `with`, independentemente de qualquer exceção que possa ter ocorrido durante a execução desse bloco.

A sintaxe básica é a seguinte:

```python
with GerenciadorDeContexto() as objeto:
    # Código dentro do contexto
    # O objeto está configurado e disponível aqui

# Fora do bloco 'with'
# O objeto foi liberado e os recursos foram tratados
```

Aqui está um exemplo prático usando um contexto para abrir e fechar automaticamente um arquivo:

```python
# Sem contexto
arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
arquivo.close()

# Com contexto
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
# O arquivo é automaticamente fechado ao sair do bloco 'with'
```

Neste exemplo, o arquivo é aberto dentro do bloco `with` e o Python se encarregará de fechá-lo automaticamente quando o bloco `with` for concluído, independentemente de ocorrerem exceções ou não.

### Modos
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
### Métodos
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

### Enconding

O UTF-8 utiliza de 1 a 4 bytes para representar diferentes caracteres, permitindo que caracteres comuns em línguas ocidentais (como inglês, francês, alemão, etc.) sejam representados em um único byte, enquanto caracteres menos comuns em scripts e idiomas diversos são representados em múltiplos bytes.

Em Python, você pode especificar o encoding UTF-8 ao abrir um arquivo usando a função `open()` e o argumento `encoding`. Por exemplo:

```python
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

Da mesma forma, ao escrever em um arquivo, você pode usar o mesmo argumento `encoding` para garantir que o texto seja salvo em formato UTF-8:

```python
with open("novo_arquivo.txt", "w", encoding="utf-8") as novo_arquivo:
    novo_arquivo.write("Olá, mundo!\n")
    novo_arquivo.write("こんにちは、世界！\n")  # Texto em japonês
```

Lembre-se de que usar a codificação correta é importante para garantir que os caracteres sejam interpretados e exibidos corretamente, especialmente quando se lida com textos em diferentes idiomas. O UTF-8 é uma escolha amplamente recomendada, pois oferece suporte a uma ampla gama de caracteres Unicode.

## JSON - py

JSON (JavaScript Object Notation) é um formato leve e amplamente utilizado para troca de dados entre sistemas. Ele é legível tanto por humanos quanto por máquinas e é frequentemente utilizado para representar estruturas de dados simples e complexas. No Python, o JSON é suportado nativamente por meio do módulo `json`.

O módulo `json` fornece funções para codificar (serializar) e decodificar (desserializar) dados JSON. Isso permite que você converta objetos Python em strings JSON e vice-versa. Aqui estão algumas funções importantes do módulo `json`:

1. `json.dumps()`: Esta função é usada para serializar objetos Python em strings JSON. Ela aceita um objeto Python como argumento e retorna uma string JSON correspondente.

Exemplo:
```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)
```

2. `json.dump()`: Semelhante ao `json.dumps()`, esta função também serializa objetos Python em strings JSON, mas escreve diretamente em um arquivo (ou em um objeto semelhante a arquivo). Isso é útil para salvar dados em um arquivo JSON.

Exemplo:
```python
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)
```

3. `json.loads()`: Essa função é usada para desserializar uma string JSON em um objeto Python. Ela aceita uma string JSON como argumento e retorna um objeto Python correspondente.

Exemplo:
```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data["name"])
```

4. `json.load()`: Essa função lê um arquivo JSON e desserializa seu conteúdo diretamente em um objeto Python.

Exemplo:
```python
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data["name"])
```

Lembrando que o JSON suporta tipos de dados simples como números, strings, booleanos e valores nulos, bem como listas e dicionários aninhados. Ao lidar com tipos de dados mais complexos, como objetos personalizados em Python, pode ser necessário fornecer funções de serialização e desserialização personalizadas usando o parâmetro `default` do `json.dumps()` ou o parâmetro `object_hook` do `json.loads()`.

Em resumo, o módulo `json` no Python é uma ferramenta poderosa para trabalhar com dados no formato JSON, permitindo que você converta facilmente entre objetos Python e strings JSON, tornando a troca de dados entre diferentes sistemas mais eficiente e conveniente.
