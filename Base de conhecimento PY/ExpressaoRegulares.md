# Expressão regulares

## Intro

Expressões regulares (também conhecidas como regex ou regexp) são sequências de caracteres que formam um padrão de pesquisa. Elas são utilizadas para realizar operações de busca, correspondência e manipulação de strings com base em padrões específicos. Em Python, o módulo `re` fornece suporte para expressões regulares.

Aqui estão alguns conceitos e funcionalidades básicos relacionados a expressões regulares em Python:

### Importando o módulo `re`

```python
import re
```

### Funções Principais:

1. **`re.search(pattern, string)`**: Procura por um padrão em toda a string, retorna a primeira correspondência encontrada.

```python
result = re.search(r'pattern', 'string')
if result:
    print('Padrão encontrado')
else:
    print('Padrão não encontrado')
```

2. **`re.match(pattern, string)`**: Verifica se o padrão ocorre no início da string.

```python
result = re.match(r'pattern', 'string')
if result:
    print('Padrão encontrado no início')
else:
    print('Padrão não encontrado no início')
```

3. **`re.findall(pattern, string)`**: Retorna todas as ocorrências do padrão na string como uma lista.

```python
result = re.findall(r'pattern', 'string')
print(result)
```

4. **`re.sub(pattern, replacement, string)`**: Substitui todas as ocorrências do padrão por uma string de substituição.

```python
new_string = re.sub(r'pattern', 'replacement', 'string')
print(new_string)
```

### Símbolos Básicos:

1. **`.` (ponto)**: Corresponde a qualquer caractere, exceto uma nova linha.

2. **`^`**: Corresponde ao início da string.

3. **`$`**: Corresponde ao final da string.

4. **`*`**: Corresponde a zero ou mais ocorrências do caractere anterior.

5. **`+`**: Corresponde a uma ou mais ocorrências do caractere anterior.

6. **`?`**: Torna o caractere anterior opcional.

### Classes de Caracteres:

1. **`[ ]`**: Corresponde a qualquer caractere dentro dos colchetes.

2. **`[^ ]`**: Corresponde a qualquer caractere que não esteja dentro dos colchetes.

### Quantificadores:

1. **`{n}`**: Corresponde exatamente a n ocorrências do caractere anterior.

2. **`{n,}`**: Corresponde a n ou mais ocorrências do caractere anterior.

3. **`{n,m}`**: Corresponde a pelo menos n e no máximo m ocorrências do caractere anterior.

### Grupos de Captura:

Os parênteses `()` são usados para criar grupos de captura.

```python
result = re.search(r'(\d+)-(\d+)-(\d+)', 'Data: 2022-01-15')
print(result.group(0))  # Retorna a string correspondente completa
print(result.group(1))  # Retorna a parte correspondente ao primeiro grupo
print(result.group(2))  # Retorna a parte correspondente ao segundo grupo
print(result.group(3))  # Retorna a parte correspondente ao terceiro grupo
```

Esses são apenas conceitos básicos sobre expressões regulares em Python. Elas são poderosas e flexíveis, permitindo a criação de padrões complexos para manipulação eficaz de strings.

## Meta caracteres:

Os metacaracteres em expressões regulares são caracteres especiais com significados específicos, proporcionando flexibilidade e poder na definição de padrões de busca. Aqui estão alguns dos metacaracteres mais comuns:

1. **`.` (ponto)**: Corresponde a qualquer caractere, exceto uma nova linha. Por exemplo, o padrão `a.c` corresponderá a "abc", "adc", etc.

2. **`^`**: Corresponde ao início da string. Por exemplo, o padrão `^abc` corresponderá a "abc" apenas se estiver no início da string.

3. **`$`**: Corresponde ao final da string. Por exemplo, o padrão `abc$` corresponderá a "abc" apenas se estiver no final da string.

4. **`*`**: Corresponde a zero ou mais ocorrências do caractere anterior. Por exemplo, o padrão `ab*c` corresponderá a "ac", "abc", "abbc", etc.

5. **`+`**: Corresponde a uma ou mais ocorrências do caractere anterior. Por exemplo, o padrão `ab+c` corresponderá a "abc", "abbc", "abbbc", etc.

6. **`?`**: Torna o caractere anterior opcional (zero ou uma ocorrência). Por exemplo, o padrão `ab?c` corresponderá a "ac" e "abc".

7. **`[]`**: Define uma classe de caracteres. Corresponde a qualquer caractere dentro dos colchetes. Por exemplo, `[aeiou]` corresponde a qualquer vogal.

8. **`[^ ]`**: Corresponde a qualquer caractere que não esteja dentro dos colchetes. Por exemplo, `[^0-9]` corresponde a qualquer caractere que não seja um dígito.

9. **`|` (barra vertical)**: Funciona como um operador lógico "OU". Por exemplo, o padrão `a|b` corresponde a "a" ou "b".

10. **`()`**: Cria grupos de captura. Os parênteses são usados para agrupar partes de um padrão. Por exemplo, `(ab)+` corresponderá a "ab", "abab", "ababab", etc.

11. **`\` (barra invertida)**: Escapa um metacaractere, permitindo que ele seja tratado como um caractere literal. Por exemplo, `\\` corresponde a uma barra invertida.

12. **`{ }`**: Especifica um número exato de ocorrências do caractere anterior. Por exemplo, `a{3}` corresponde a "aaa".

13. **`*?`, `+?`, `??`**: Versões não-gulosas (lazy) dos quantificadores `*`, `+`, e `?`. Eles correspondem ao menor número possível de caracteres.

14. **`\b` e `\B`**: Corresponde à posição de uma fronteira de palavra (`\b`) ou a uma posição que não é uma fronteira de palavra (`\B`).

Esses são apenas alguns dos metacaracteres básicos em expressões regulares. Eles proporcionam uma poderosa linguagem para definir padrões de busca em strings de forma flexível e eficiente. Quando você combina esses metacaracteres, pode criar padrões complexos que atendem a uma variedade de cenários de busca e manipulação de strings.

## Quantificadores

Os quantificadores em expressões regulares são metacaracteres que especificam o número de ocorrências de um caractere, grupo ou classe de caracteres em um padrão. Eles permitem que você descreva a quantidade de vezes que um elemento específico deve ocorrer para que um padrão seja considerado correspondente. Aqui estão alguns dos quantificadores mais comuns:

1. **`*` (Asterisco)**: Corresponde a zero ou mais ocorrências do elemento anterior. Por exemplo, o padrão `ab*c` corresponderá a "ac", "abc", "abbc", "abbbc", etc.

   ```python
   import re

   pattern = re.compile(r'ab*c')
   result = pattern.match('ac')
   print(result)  # Corresponde

   result = pattern.match('abbc')
   print(result)  # Corresponde
   ```

2. **`+` (Sinal de Adição)**: Corresponde a uma ou mais ocorrências do elemento anterior. Por exemplo, o padrão `ab+c` corresponderá a "abc", "abbc", "abbbc", etc.

   ```python
   import re

   pattern = re.compile(r'ab+c')
   result = pattern.match('abc')
   print(result)  # Corresponde

   result = pattern.match('ac')
   print(result)  # Não corresponde
   ```

3. **`?` (Ponto de Interrogação)**: Torna o elemento anterior opcional, correspondendo a zero ou uma ocorrência. Por exemplo, o padrão `ab?c` corresponderá a "ac" e "abc".

   ```python
   import re

   pattern = re.compile(r'ab?c')
   result = pattern.match('ac')
   print(result)  # Corresponde

   result = pattern.match('abc')
   print(result)  # Corresponde
   ```

4. **`{n}`**: Corresponde exatamente a n ocorrências do elemento anterior. Por exemplo, o padrão `a{3}` corresponderá a "aaa".

   ```python
   import re

   pattern = re.compile(r'a{3}')
   result = pattern.match('aaa')
   print(result)  # Corresponde

   result = pattern.match('aa')
   print(result)  # Não corresponde
   ```

5. **`{n,}`**: Corresponde a n ou mais ocorrências do elemento anterior. Por exemplo, o padrão `a{2,}` corresponderá a "aa", "aaa", "aaaa", etc.

   ```python
   import re

   pattern = re.compile(r'a{2,}')
   result = pattern.match('aa')
   print(result)  # Corresponde

   result = pattern.match('a')
   print(result)  # Não corresponde
   ```

6. **`{n,m}`**: Corresponde a pelo menos n e no máximo m ocorrências do elemento anterior. Por exemplo, o padrão `a{2,4}` corresponderá a "aa", "aaa" e "aaaa".

   ```python
   import re

   pattern = re.compile(r'a{2,4}')
   result = pattern.match('aaa')
   print(result)  # Corresponde

   result = pattern.match('aaaaa')
   print(result)  # Não corresponde
   ```

Os quantificadores permitem que você crie padrões mais flexíveis e generalizados, facilitando a manipulação e busca em strings com base nas regras específicas de repetição de elementos. É importante observar que os quantificadores podem ser combinados com outros metacaracteres para criar padrões mais complexos.

### greedy e non-greedy(lazy)

Os conceitos de "greedy" (ganancioso) e "non-greedy" (não ganancioso ou "lazy") referem-se ao comportamento dos quantificadores em expressões regulares. Esses quantificadores determinam quantas vezes um caractere, grupo ou classe de caracteres deve ocorrer para ser considerado uma correspondência.

- **Greedy (Ganancioso):**
  - Quantificadores são por padrão gananciosos. Eles tentam corresponder ao maior número possível de caracteres enquanto ainda mantêm uma correspondência válida.
  - O quantificador greedy padrão é representado por `*`, `+`, e `?`.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'<.*>')
    result = pattern.search('<foo> <bar> <baz>')
    print(result.group())  # Correspondência gananciosa: '<foo> <bar> <baz>'
    ```

- **Non-Greedy (Lazy):**
  - Para tornar um quantificador não ganancioso, você pode adicionar um `?` após os quantificadores gananciosos `*`, `+`, ou `?`.
  - Isso faz com que o quantificador correspondente ao menor número possível de caracteres, satisfazendo ainda a condição de correspondência.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'<.*?>')
    result = pattern.search('<foo> <bar> <baz>')
    print(result.group())  # Correspondência não gananciosa: '<foo>'
    ```

Ao adicionar `?` após um quantificador, você indica que ele deve ser lazy (não ganancioso). No exemplo acima, o padrão `<.*?>` corresponde ao menor número possível de caracteres entre `<` e `>`, resultando em correspondências não gananciosas.

A distinção entre ganancioso e não ganancioso é crucial ao lidar com padrões em que existem várias correspondências possíveis na string. O uso apropriado desses quantificadores ajuda a evitar correspondências indesejadas e a obter os resultados desejados em expressões regulares complexas.

## Grupos e Retrovisores

Grupos e retrovisores são recursos avançados em expressões regulares que proporcionam maior controle e flexibilidade ao criar padrões de busca. Vamos entender cada um deles:

### 1. Grupos:

Os grupos em expressões regulares são criados usando parênteses `()` e servem para agrupar partes do padrão. Eles oferecem vários benefícios:

- **Agrupamento de elementos:**
  - Permitem agrupar caracteres ou padrões inteiros para aplicar quantificadores ou operadores a eles.
  
    Exemplo:
    ```python
    import re

    pattern = re.compile(r'(ab)+')
    result = pattern.match('ababab')
    print(result.group())  # Correspondência: 'ababab'
    ```

- **Captura de grupos:**
  - Facilitam a captura de partes específicas do padrão. Você pode acessar esses grupos após uma correspondência usando o método `group()` do objeto de correspondência.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    result = pattern.match('15/01/2022')
    print(result.group(1))  # Dia: '15'
    print(result.group(2))  # Mês: '01'
    print(result.group(3))  # Ano: '2022'
    ```

### 2. Retrovisores:

Os retrovisores permitem se referir a grupos já capturados dentro da própria expressão regular. Eles são úteis para criar padrões mais complexos ou referenciar repetições de padrões anteriormente capturados.

- **Referência a grupos:**
  - Utiliza `\n` onde `n` é o número do grupo que você deseja referenciar. Por exemplo, `\1` refere-se ao primeiro grupo, `\2` ao segundo, e assim por diante.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'(\w+) and \1')
    result = pattern.search('apple and apple')
    print(result.group())  # Correspondência: 'apple and apple'
    ```

- **Uso em substituições:**
  - Também podem ser usados ao realizar substituições em strings usando a função `re.sub()`.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    result = pattern.sub(r'\2-\1-\3', '15/01/2022')
    print(result)  # Substituição: '01-15-2022'
    ```

O uso eficiente de grupos e retrovisores torna as expressões regulares mais poderosas e expressivas, permitindo a criação de padrões complexos e a manipulação eficaz de strings. Esses recursos são particularmente úteis em situações em que é necessário lidar com partes específicas de um padrão ou fazer referência a partes anteriormente capturadas.

