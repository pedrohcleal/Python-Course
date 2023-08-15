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

## Funções decoradoras

Em Python, as funções decoradoras são uma característica poderosa que permitem modificar ou aprimorar o comportamento de outras funções ou métodos. Essa abordagem segue o conceito de "metaprogramação", onde você escreve código que manipula código. Isso é especialmente útil para adicionar funcionalidades comuns, como logging, autenticação, medição de desempenho etc., a várias funções sem repetir o mesmo código em cada uma delas.

Vamos entender o conceito de decoradores passo a passo:

1. **Funções de Ordem Superior:** Em Python, as funções são cidadãos de primeira classe, o que significa que elas podem ser tratadas como qualquer outra variável. Isso inclui passá-las como argumentos para outras funções e retorná-las de funções. Esse recurso é a base para a implementação de decoradores.

2. **Sintaxe de Decorador Básica:**
   ```python
   def decorator_function(original_function):
       def wrapper_function(*args, **kwargs):
           # Código a ser executado antes da função original
           result = original_function(*args, **kwargs)
           # Código a ser executado depois da função original
           return result
       return wrapper_function
   ```

   Nesse exemplo, `decorator_function` é um decorador que recebe uma função original como argumento e retorna uma nova função chamada `wrapper_function` que incorpora a funcionalidade extra. A função `wrapper_function` chama a função original e, opcionalmente, executa código antes e depois dela.

3. **Aplicando Decoradores:**
   Você pode aplicar um decorador a uma função usando a sintaxe de "@" antes da definição da função:
   
   ```python
   @decorator_function
   def my_function():
       # Código da função
   ```

4. **Decoradores com Parâmetros:**
   Os decoradores também podem aceitar argumentos. Isso é útil quando você deseja configurar o comportamento do decorador. A estrutura geral é ligeiramente diferente:

   ```python
   def decorator_with_arguments(arg1, arg2):
       def decorator_function(original_function):
           def wrapper_function(*args, **kwargs):
               # Usar arg1, arg2
               result = original_function(*args, **kwargs)
               return result
           return wrapper_function
       return decorator_function
   ```

   Você aplicaria um decorador com argumentos da seguinte maneira:

   ```python
   @decorator_with_arguments(arg1, arg2)
   def my_function():
       # Código da função
   ```

5. **Ordem de Múltiplos Decoradores:**
   É possível aplicar vários decoradores a uma única função. A ordem em que eles são aplicados é importante e segue da parte interna (mais próxima da função original) para a parte externa. Por exemplo:

   ```python
   @decorator1
   @decorator2
   @decorator3
   def my_function():
       # Código da função
   ```

   Nesse caso, `decorator3` será aplicado primeiro, seguido por `decorator2` e, por fim, `decorator1`.

Decoradores são uma ferramenta poderosa para melhorar a modularidade e a reutilização de código em Python. Eles permitem separar as preocupações, mantendo a funcionalidade adicional fora das funções principais e facilitando a manutenção do código.
