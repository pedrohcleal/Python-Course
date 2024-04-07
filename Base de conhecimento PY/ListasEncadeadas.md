# ListasEncadeadas

Uma lista encadeada em Python é uma estrutura de dados linear composta por nós. Cada nó contém um valor e um ponteiro (ou referência) para o próximo nó na sequência. Ao contrário das listas em Python (como `list`), onde os elementos são armazenados sequencialmente na memória, em uma lista encadeada, os nós podem ser espalhados aleatoriamente na memória, conectados apenas por meio de ponteiros.

As listas encadeadas em Python podem ser implementadas usando classes. Aqui está um exemplo básico de como definir uma lista encadeada:

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
```

Nesta definição:

- `ListNode` é a classe que representa um nó na lista encadeada.
- O método `__init__` é um construtor que é chamado quando um novo objeto `ListNode` é criado. Ele inicializa o valor do nó e o ponteiro `next` como `None`, indicando que inicialmente o nó não está conectado a nenhum outro nó.

Para criar uma lista encadeada, você cria uma instância da classe `ListNode` para cada elemento e os conecta através dos ponteiros `next`. Aqui está um exemplo de como criar uma lista encadeada com três nós:

```python
# Criando nós
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Conectando os nós
node1.next = node2
node2.next = node3
```

Neste exemplo, `node1` é o primeiro nó, `node2` é o segundo nó e `node3` é o terceiro nó. Cada nó contém um valor e um ponteiro para o próximo nó na sequência.

Para percorrer uma lista encadeada, geralmente começamos com o primeiro nó (cabeça) e iteramos sobre os nós usando os ponteiros `next` até chegarmos ao último nó. Aqui está um exemplo de como iterar sobre a lista encadeada criada acima:

```python
current_node = node1  # Começa com o primeiro nó (cabeça)
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
```

Este código irá imprimir os valores dos nós da lista encadeada: 1, 2 e 3. Quando `current_node.next` é `None`, sabemos que alcançamos o final da lista encadeada.

## Como criar nodes a partir de uma lista[]?

Para criar nós a partir de uma lista em Python e conectá-los em uma lista encadeada, você pode iterar sobre os elementos da lista e criar um novo nó para cada elemento. Aqui está um exemplo de como fazer isso:

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    if not values:
        return None

    # Cria o primeiro nó da lista encadeada
    head = ListNode(values[0])
    current_node = head

    # Itera sobre os valores restantes na lista
    for value in values[1:]:
        new_node = ListNode(value)  # Cria um novo nó com o valor atual
        current_node.next = new_node  # Conecta o nó atual ao novo nó
        current_node = new_node  # Atualiza o nó atual para o novo nó

    return head  # Retorna a cabeça da lista encadeada

# Lista de valores
values = [1, 2, 3, 4, 5]

# Criação da lista encadeada a partir da lista de valores
head = create_linked_list(values)

# Itera sobre a lista encadeada resultante para imprimir os valores dos nós
current_node = head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
```

Neste exemplo:

- A classe `ListNode` define um nó na lista encadeada, contendo um valor e um ponteiro para o próximo nó.
- A função `create_linked_list` recebe uma lista de valores como entrada e retorna a cabeça da lista encadeada resultante.
- A lista de valores é percorrida, e para cada valor, um novo nó é criado e conectado ao nó anterior na lista encadeada.
- Por fim, a função retorna a cabeça da lista encadeada, que é o primeiro nó na sequência.

Este código cria uma lista encadeada a partir dos valores da lista e imprime os valores dos nós na lista encadeada resultante.
