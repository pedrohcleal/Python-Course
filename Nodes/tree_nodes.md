# 📘 Documentação Introdutória — Árvore Binária em Python 3

## 1. O que é uma Árvore Binária?

Uma **árvore binária** é uma estrutura de dados hierárquica onde cada nó pode ter no máximo dois filhos:

* Filho da esquerda (`left`)
* Filho da direita (`right`)

Cada nó possui:

* Um valor (`value`)
* Uma referência para o filho esquerdo
* Uma referência para o filho direito

### Representação visual

```
        10
       /  \
      5   15
     / \    \
    2   7    20
```

---

## 2. Estrutura básica de um nó em Python

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## 3. Criando uma árvore manualmente

```python
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)
```

---

## 4. Tipos de percurso (traversal)

Percorrer uma árvore significa visitar todos os nós em uma determinada ordem.

---

### 4.1 Pré-Ordem (Root → Left → Right)

Usado para copiar árvores ou gerar expressões prefixas.

```python
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)
```

Saída:

```
10 5 2 7 15 20
```

---

### 4.2 Em-Ordem (Left → Root → Right)

Muito usado em Árvores Binárias de Busca (BST), pois retorna valores ordenados.

```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)
```

Saída:

```
2 5 7 10 15 20
```

---

### 4.3 Pós-Ordem (Left → Right → Root)

Usado para deletar árvores ou avaliar expressões.

```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)
```

Saída:

```
2 7 5 20 15 10
```

---

### 4.4 Em Largura (Level Order / BFS)

Percorre nível por nível.

```python
from collections import deque

def level_order(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

Saída:

```
10 5 15 2 7 20
```

---

## 5. Árvore Binária de Busca (BST)

Uma **BST (Binary Search Tree)** segue a regra:

* Valores menores ficam à esquerda
* Valores maiores ficam à direita

---

### Inserção em uma BST

```python
def insert(root, value):
    if not root:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root
```

Uso:

```python
values = [10, 5, 15, 2, 7, 20]
root = None

for v in values:
    root = insert(root, v)
```

---

### Busca em uma BST

```python
def search(root, value):
    if not root or root.value == value:
        return root

    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)
```

---

## 6. Complexidade

| Operação | Melhor Caso | Pior Caso |
| -------- | ----------- | --------- |
| Busca    | O(log n)    | O(n)      |
| Inserção | O(log n)    | O(n)      |
| Percurso | O(n)        | O(n)      |

> O pior caso acontece quando a árvore fica desbalanceada (parecendo uma lista).

---

## 7. Quando usar árvores binárias?

Use quando você precisa:

* Manter dados ordenados
* Fazer buscas rápidas
* Representar hierarquias
* Criar expressões matemáticas
* Implementar sistemas de decisão

---

## 8. Próximos passos

Você pode evoluir para:

* Árvores AVL (balanceadas)
* Árvores Red-Black
* Árvores B (banco de dados)
* Heap binário (fila de prioridade)

---

Perfeito — segue uma documentação **didática, prática e focada em Python 3** cobrindo exatamente os pontos que você pediu:

* Busca em árvore binária (BST)
* Inserção automática
* Versão iterativa (sem recursão)
* Árvore balanceada (AVL)

Pode usar direto como material de estudo ou README.

---

# 📘 Árvores Binárias em Python 3 — Busca, Inserção, Versão Iterativa e AVL

---

## 1) Árvore Binária de Busca (BST)

Uma **BST (Binary Search Tree)** segue a regra:

* Valores **menores** ficam à esquerda
* Valores **maiores** ficam à direita

Isso permite buscas rápidas.

---

## Estrutura do nó

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## 2) Inserção automática em uma BST (recursiva)

```python
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root
```

Uso:

```python
values = [10, 5, 15, 2, 7, 20]
root = None

for v in values:
    root = insert(root, v)
```

A árvore será montada automaticamente respeitando as regras da BST.

---

## 3) Busca em uma BST (recursiva)

```python
def search(root, value):
    if root is None or root.value == value:
        return root

    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)
```

Uso:

```python
result = search(root, 7)

if result:
    print("Encontrado:", result.value)
else:
    print("Não encontrado")
```

---

## 4) Versão iterativa (sem recursão)

### Inserção iterativa

```python
def insert_iterative(root, value):
    new_node = Node(value)

    if not root:
        return new_node

    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root
```

---

### Busca iterativa

```python
def search_iterative(root, value):
    current = root

    while current:
        if current.value == value:
            return current
        elif value < current.value:
            current = current.left
        else:
            current = current.right

    return None
```

---

## 5) Problema da BST: árvore desbalanceada

Se você inserir valores já ordenados:

```python
values = [1, 2, 3, 4, 5]
```

A árvore vira praticamente uma lista:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

A busca passa a ser **O(n)** em vez de **O(log n)**.

---

## 6) Árvore Balanceada — AVL

A **AVL** é uma BST que se auto-balanceia após cada inserção.

Ela mantém a propriedade:

```
|altura_esquerda - altura_direita| ≤ 1
```

Quando isso é violado, rotações são aplicadas.

---

## Estrutura do nó AVL

```python
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
```

---

## Funções auxiliares

```python
def height(node):
    return node.height if node else 0

def balance(node):
    return height(node.left) - height(node.right)
```

---

## Rotações

### Rotação à direita

```python
def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x
```

---

### Rotação à esquerda

```python
def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y
```

---

## Inserção em uma AVL

```python
def insert_avl(root, value):
    if not root:
        return AVLNode(value)

    if value < root.value:
        root.left = insert_avl(root.left, value)
    else:
        root.right = insert_avl(root.right, value)

    root.height = 1 + max(height(root.left), height(root.right))

    balance_factor = balance(root)

    # Caso LL
    if balance_factor > 1 and value < root.left.value:
        return rotate_right(root)

    # Caso RR
    if balance_factor < -1 and value > root.right.value:
        return rotate_left(root)

    # Caso LR
    if balance_factor > 1 and value > root.left.value:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Caso RL
    if balance_factor < -1 and value < root.right.value:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root
```

---

## 7) Complexidade

| Estrutura     | Busca    | Inserção |
| ------------- | -------- | -------- |
| BST normal    | O(log n) | O(log n) |
| BST pior caso | O(n)     | O(n)     |
| AVL           | O(log n) | O(log n) |

---

## 8) Quando usar cada uma?

| Situação                         | Estrutura        |
| -------------------------------- | ---------------- |
| Simples e rápida de implementar  | BST              |
| Precisa de performance garantida | AVL              |
| Ambiente com pouca recursão      | Versão iterativa |
| Dados muito grandes              | AVL ou Red-Black |

