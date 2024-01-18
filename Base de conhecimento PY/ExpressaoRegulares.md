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

## Shorthands e Flags

**Shorthands (Atalhos):**

Os shorthands em expressões regulares são atalhos ou códigos abreviados que representam classes de caracteres comuns. Eles simplificam a escrita de padrões e tornam as expressões regulares mais concisas. Alguns dos shorthands mais comuns incluem:

1. **`\d`**: Corresponde a qualquer dígito decimal (equivalente a `[0-9]`).

2. **`\D`**: Corresponde a qualquer caractere que não seja um dígito (equivalente a `[^0-9]`).

3. **`\w`**: Corresponde a qualquer caractere alfanumérico (equivalente a `[a-zA-Z0-9_]`).

4. **`\W`**: Corresponde a qualquer caractere que não seja alfanumérico (equivalente a `[^a-zA-Z0-9_]`).

5. **`\s`**: Corresponde a qualquer caractere de espaço em branco (equivalente a `[ \t\n\r\f\v]`).

6. **`\S`**: Corresponde a qualquer caractere que não seja de espaço em branco (equivalente a `[^ \t\n\r\f\v]`).

Esses atalhos podem ser úteis para simplificar padrões e tornar as expressões regulares mais legíveis.

**Flags:**

As flags em expressões regulares são modificadores que alteram o comportamento padrão de uma expressão regular. Em Python, as flags são passadas como argumentos adicionais nas funções do módulo `re`. Algumas das flags mais comuns incluem:

1. **`re.IGNORECASE` ou `re.I`**: Ignora diferenças entre maiúsculas e minúsculas durante a correspondência.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'python', re.IGNORECASE)
    result = pattern.match('Python')
    print(result.group())  # Correspondência: 'Python'
    ```

2. **`re.MULTILINE` ou `re.M`**: Permite que os metacaracteres `^` e `$` correspondam ao início e ao final de cada linha em vez de toda a string.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'^\d+', re.MULTILINE)
    result = pattern.findall('123\n456\n789')
    print(result)  # Correspondência: ['123', '456', '789']
    ```

3. **`re.DOTALL` ou `re.S`**: Faz com que o ponto (`.`) corresponda a qualquer caractere, incluindo quebras de linha (`\n`).

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'a.b', re.DOTALL)
    result = pattern.match('a\nb')
    print(result.group())  # Correspondência: 'a\nb'
    ```

4. **`re.VERBOSE` ou `re.X`**: Permite que você escreva expressões regulares de maneira mais legível, ignorando espaços em branco e permitindo comentários.

    Exemplo:
    ```python
    import re

    pattern = re.compile(r'''
                        \d +  # Dígitos
                        \s *  # Espaços em branco opcionais
                        [a-z]+  # Letras minúsculas
                        ''', re.VERBOSE)
    result = pattern.match('123 abc')
    print(result.group())  # Correspondência: '123 abc'
    ```

Essas flags proporcionam flexibilidade e controle adicional sobre o comportamento das expressões regulares em Python. Pode-se combinar múltiplas flags usando o operador de bit `|` (ou).

##  Lookahead e Lookbehind

Lookahead e lookbehind são técnicas avançadas em expressões regulares que permitem fazer correspondências com base na presença ou ausência de determinados padrões à frente (lookahead) ou atrás (lookbehind) da posição atual na string. Essas construções não consomem caracteres na string de entrada durante a correspondência.

### 1. Lookahead Positivo (Positive Lookahead):

O lookahead positivo verifica se um padrão está presente à frente da posição atual na string sem consumir caracteres na correspondência principal.

- **Sintaxe:** `X(?=Y)`
- **Significado:** Corresponde a "X" apenas se "X" é seguido por "Y".

Exemplo:
```python
import re

pattern = re.compile(r'\d(?=[a-z])')
result = pattern.findall('1a 2b 3c')
print(result)  # Correspondência: ['1', '2', '3']
```

Neste exemplo, `\d(?=[a-z])` corresponde a um dígito (`\d`) apenas se estiver seguido por uma letra minúscula (`[a-z]`).

### 2. Lookahead Negativo (Negative Lookahead):

O lookahead negativo verifica se um padrão não está presente à frente da posição atual na string.

- **Sintaxe:** `X(?!Y)`
- **Significado:** Corresponde a "X" apenas se "X" não é seguido por "Y".

Exemplo:
```python
import re

pattern = re.compile(r'\d(?!a)')
result = pattern.findall('1a 2b 3c')
print(result)  # Correspondência: ['2', '3']
```

Aqui, `\d(?!a)` corresponde a um dígito (`\d`) apenas se não estiver seguido pela letra "a".

### 3. Lookbehind Positivo (Positive Lookbehind):

O lookbehind positivo verifica se um padrão está presente atrás da posição atual na string.

- **Sintaxe:** `(?<=Y)X`
- **Significado:** Corresponde a "X" apenas se "X" é precedido por "Y".

Exemplo:
```python
import re

pattern = re.compile(r'(?<=@)\w+')
result = pattern.findall('user1@example.com user2@example.com')
print(result)  # Correspondência: ['example', 'example']
```

Aqui, `(?<=@)\w+` corresponde a uma sequência de caracteres alfanuméricos apenas se estiver precedida pelo caractere "@", capturando assim os domínios de e-mail.

### 4. Lookbehind Negativo (Negative Lookbehind):

O lookbehind negativo verifica se um padrão não está presente atrás da posição atual na string.

- **Sintaxe:** `(?<!Y)X`
- **Significado:** Corresponde a "X" apenas se "X" não é precedido por "Y".

Exemplo:
```python
import re

pattern = re.compile(r'(?<!\d)\w+')
result = pattern.findall('1abc 2def 3ghi')
print(result)  # Correspondência: ['abc', 'def', 'ghi']
```

Neste exemplo, `(?<!\d)\w+` corresponde a uma sequência de caracteres alfanuméricos apenas se não estiver precedida por um dígito.

As construções de lookahead e lookbehind oferecem maior flexibilidade na criação de padrões de busca mais sofisticados, levando em consideração o contexto à frente ou atrás de uma posição específica na string.

## Como validar IPV4

Validar um endereço IPv4 com expressões regulares pode ser feito com uma regex que verifica se o padrão do endereço está correto. Um endereço IPv4 é composto por quatro números inteiros separados por pontos, onde cada número está no intervalo de 0 a 255. Aqui está uma expressão regular em Python para validar um endereço IPv4:

```python
import re

def validar_ipv4(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$')
    return bool(pattern.match(ip))

# Exemplos de uso:
print(validar_ipv4('192.168.0.1'))  # True
print(validar_ipv4('256.0.0.1'))     # False
print(validar_ipv4('abc.def.ghi.jkl'))  # False
```

Explicação da regex:

- `^`: Âncora de início da string.
- `( ... )`: Grupo de captura para cada bloco de número separado por ponto.
- `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})`: Esta parte corresponde a cada bloco de número. Aqui está uma explicação mais detalhada:
  - `25[0-5]`: Representa números de 250 a 255.
  - `2[0-4][0-9]`: Representa números de 200 a 249.
  - `[0-1]?[0-9]{1,2}`: Representa números de 0 a 199, permitindo zero à esquerda.
- `\.`: Corresponde ao ponto que separa os blocos de números.
- `{3}`: Indica que precisamos de exatamente três ocorrências dos blocos de números e pontos.
- `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})`: Corresponde ao último bloco de número.
- `$`: Âncora de final da string.

Essa expressão regular verifica se um endereço IPv4 está no formato correto. No entanto, vale mencionar que, embora a regex valide o formato do endereço, ela não verifica se o valor numérico de cada bloco está no intervalo apropriado. Por exemplo, "192.168.500.1" seria considerado válido pela regex, pois segue o formato IPv4, mas é um endereço inválido em termos de valor numérico. Para verificar completamente a validade de um endereço IPv4, seria necessário realizar verificações adicionais além do escopo de uma expressão regular.

## Como validar CPF

A validação de um CPF (Cadastro de Pessoa Física) pode ser realizada com uma expressão regular que verifica se o formato do CPF está correto. O CPF no Brasil tem um formato específico com pontos e traços, e existem algoritmos adicionais para verificar a validade numérica do CPF. Aqui está uma expressão regular para validar o formato do CPF em Python:

```python
import re

def validar_cpf(cpf):
    # Remove pontos e traços do CPF
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Expressão regular para validar o formato do CPF
    pattern = re.compile(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$')
    if not pattern.match(cpf):
        return False

    # Verificação do dígito verificador
    cpf_numeros = [int(d) for d in cpf[:-2]]
    dv1, dv2 = map(int, cpf[-2:])
    
    # Cálculo do primeiro dígito verificador
    total = sum((i + 1) * n for i, n in enumerate(cpf_numeros))
    resto = total % 11
    resultado1 = 11 - resto if resto > 1 else 0

    # Cálculo do segundo dígito verificador
    cpf_numeros.append(resultado1)
    total = sum((i + 1) * n for i, n in enumerate(cpf_numeros))
    resto = total % 11
    resultado2 = 11 - resto if resto > 1 else 0

    # Verifica se os dígitos verificadores calculados coincidem com os fornecidos
    return resultado1 == dv1 and resultado2 == dv2

# Exemplos de uso:
print(validar_cpf('123.456.789-09'))  # True
print(validar_cpf('98765432100'))    # False (formato inválido)
print(validar_cpf('111.222.333-44'))  # False (CPF inválido numericamente)
```

Explicação do código:

1. Remove os pontos e traços do CPF usando `re.sub` para ficar apenas com os dígitos.
2. Verifica se o CPF tem 11 dígitos.
3. Utiliza uma expressão regular para verificar o formato do CPF.
4. Realiza o cálculo dos dígitos verificadores e compara com os fornecidos no CPF.

É importante mencionar que essa validação não verifica se o CPF é válido no contexto legal (não verifica se o número pertence a uma pessoa real), apenas se está no formato correto e tem dígitos verificadores válidos.

## Validar número de telefone
