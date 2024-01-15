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
