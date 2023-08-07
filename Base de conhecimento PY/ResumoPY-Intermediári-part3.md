# Resumo PYthon intermediário

## List Comprehension

A list comprehension é uma construção sintática poderosa e concisa na linguagem de programação Python que permite criar listas de forma eficiente. Ela é usada para criar novas listas aplicando uma expressão a cada elemento de uma sequência (como uma lista, tupla, string, etc.), ao mesmo tempo que permite filtrar os elementos da sequência original com base em uma condição.

A estrutura básica de uma list comprehension é a seguinte:

```python
nova_lista = [expressão for elemento in sequência original if condição]
```

Aqui está uma explicação dos componentes:

- `expressão`: É a operação que você deseja executar em cada elemento da sequência original para criar o novo valor na lista resultante.

- `elemento`: Variável que representa cada elemento da sequência original conforme ela é percorrida.

- `sequência original`: A coleção de elementos sobre a qual você está iterando, como uma lista, tupla ou string.

- `condição` (opcional): Uma expressão booleana que permite filtrar os elementos da sequência original. Apenas os elementos que atendem à condição serão incluídos na lista resultante.

Aqui estão alguns exemplos para ilustrar como as list comprehensions funcionam:

1. Criar uma lista de quadrados dos números de 0 a 9:
```python
quadrados = [x**2 for x in range(10)]
```

2. Filtrar apenas os números pares de uma lista:
```python
numeros_pares = [x for x in range(20) if x % 2 == 0]
```

3. Converter uma lista de strings em uma lista de seus comprimentos correspondentes:
```python
palavras = ['python', 'é', 'incrível']
comprimentos = [len(word) for word in palavras]
```

4. Criar uma lista de números positivos de outra lista:
```python
numeros = [-2, 5, -9, 10, -3, 7]
numeros_positivos = [x for x in numeros if x > 0]
```

As list comprehensions são uma maneira eficiente e legível de criar listas em Python, tornando o código mais conciso e fácil de entender. No entanto, lembre-se de não exagerar na complexidade das expressões e condições dentro das list comprehensions, pois isso pode prejudicar a legibilidade do código.
