# Resumo Python part 5

## Variáveis livres + nonlocal (locals, globals)
Em Python, variáveis são utilizadas para armazenar valores que podem ser acessados e manipulados em diferentes partes do código. As variáveis podem ser divididas em diferentes categorias, como variáveis locais, variáveis globais, variáveis de instância, entre outras. Entre essas categorias, existem também as variáveis livres e a palavra-chave `nonlocal` que afetam o escopo das variáveis.

1. **Variáveis Livres:**
Variáveis livres são aquelas que estão definidas em um escopo superior e são acessíveis a partir de um escopo interno. Em outras palavras, são variáveis globais ou pertencentes a um escopo mais amplo que podem ser usadas dentro de uma função, por exemplo, sem a necessidade de serem passadas como argumentos. As variáveis livres são automaticamente capturadas pelo Python quando você as utiliza dentro de uma função. Aqui está um exemplo:

```python
x = 10  # Variável global

def minha_funcao():
    print(x)  # Acessando a variável global 'x'

minha_funcao()  # Saída: 10
```

2. **Palavra-chave `nonlocal`:**
A palavra-chave `nonlocal` é utilizada para indicar que uma variável pertence ao escopo imediatamente superior ao escopo atual da função, mas não é global. Ela é frequentemente usada em funções aninhadas, quando você precisa modificar uma variável em um escopo acima do escopo local da função atual. Isso é especialmente útil quando há uma variável com o mesmo nome em escopos diferentes.

```python
def exterior():
    y = 20  # Variável no escopo de 'exterior'

    def interior():
        nonlocal y
        y += 5  # Modificando a variável 'y' do escopo exterior
        print(y)

    interior()  # Saída: 25

exterior()
```

3. **Funções `locals()` e `globals()`:**
As funções `locals()` e `globals()` permitem acessar os dicionários de variáveis locais e globais, respectivamente. O dicionário retornado por `locals()` contém todas as variáveis no escopo local da função, enquanto o dicionário retornado por `globals()` contém todas as variáveis no escopo global. Isso pode ser útil para inspecionar ou manipular as variáveis em diferentes escopos.

```python
x = 10  # Variável global

def minha_funcao():
    y = 5  # Variável local
    print(locals())  # Mostra as variáveis locais

print(globals())  # Mostra as variáveis globais
minha_funcao()
```

Em resumo, as variáveis livres e a palavra-chave `nonlocal` afetam o escopo das variáveis em Python. Variáveis livres são aquelas definidas em um escopo superior e podem ser acessadas em escopos internos sem serem passadas como argumentos. A palavra-chave `nonlocal` é usada para modificar variáveis de um escopo superior em funções aninhadas. As funções `locals()` e `globals()` permitem acessar as variáveis em escopos locais e globais, respectivamente.
