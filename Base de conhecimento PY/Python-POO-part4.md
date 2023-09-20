# POO Part4

## Context Manager with Class

Em Python, um contexto (context manager) é uma abstração que permite que você defina um bloco de código que deve ser executado antes e depois de um contexto específico. Isso é particularmente útil quando você precisa configurar recursos, como abrir e fechar arquivos, conexões de banco de dados ou sockets de rede, de maneira segura e garantir que os recursos sejam liberados corretamente, mesmo em caso de exceções.

Existem duas maneiras principais de implementar um contexto manager em Python: usando classes ou usando a sintaxe `with`. Vou explicar ambas:

**Usando uma classe:**

A maneira mais comum de criar um contexto manager é criando uma classe que implementa dois métodos especiais: `__enter__` e `__exit__`.

- O método `__enter__` é chamado quando o bloco `with` é iniciado e é usado para configurar o contexto e retornar um valor opcional que será associado à variável após o `as` no bloco `with`.
- O método `__exit__` é chamado quando o bloco `with` é concluído, seja normalmente ou devido a uma exceção. Ele é responsável por liberar os recursos e manipular exceções, se necessário.

Aqui está um exemplo de um contexto manager simples que lida com a abertura e o fechamento de arquivos:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Usando o contexto manager para abrir um arquivo
with FileManager('arquivo.txt', 'w') as file:
    file.write('Olá, contexto manager!')
# O arquivo é automaticamente fechado quando saímos do bloco "with"
```

**Usando a sintaxe `with` diretamente:**

Além de criar uma classe para um contexto manager, você também pode usar a função `contextlib.contextmanager` para criar um contexto manager de forma mais concisa usando geradores. Isso é útil quando você deseja criar um contexto manager mais simples.

Aqui está um exemplo usando a função `contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Usando o contexto manager para abrir um arquivo
with file_manager('arquivo.txt', 'w') as file:
    file.write('Olá, contexto manager!')
# O arquivo é automaticamente fechado quando saímos do bloco "with"
```

Ambos os exemplos acima ilustram como criar e usar context managers em Python para gerenciar recursos e garantir que eles sejam liberados adequadamente, o que é uma prática recomendada para escrever código mais seguro e eficiente.

## Exceptions em Context Manager

Em contexto managers criados usando classes em Python, você pode manipular exceções dentro dos métodos `__enter__` e `__exit__` para realizar ações específicas em caso de erros e garantir que os recursos sejam liberados corretamente, mesmo em cenários com exceções. Aqui está uma descrição de como lidar com exceções em um contexto manager com classes:

1. **`__enter__` e exceções**: No método `__enter__`, você pode lidar com exceções que ocorrem durante a configuração do contexto. Por exemplo, se você estiver abrindo um arquivo e ele não existir, pode tratar essa exceção no método `__enter__` e decidir como deseja lidar com ela. Você também pode levantar exceções personalizadas se necessário.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
            # Você pode tomar medidas, como criar o arquivo, se desejar.
            raise  # Re-levanta a exceção para que o código cliente possa lidar com ela
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Usando o contexto manager com tratamento de exceções
try:
    with FileManager('arquivo_inexistente.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Erro ao abrir o arquivo: {e}")
# O código continua a ser executado após o tratamento da exceção
```

2. **`__exit__` e exceções**: No método `__exit__`, você também pode lidar com exceções que ocorrem durante o bloco `with` e decidir como deseja tratá-las. O método `__exit__` recebe três argumentos que representam o tipo de exceção (`exc_type`), o valor da exceção (`exc_value`) e o traceback (rastreamento da pilha) da exceção. Você pode usar esses argumentos para tomar decisões com base no tipo de exceção ou em outros critérios.

```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        try:
            self.connection = connect_to_database(self.host, self.port)
            return self.connection
        except DatabaseError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            if exc_type is not None and issubclass(exc_type, DatabaseError):
                # Se ocorreu uma exceção do tipo DatabaseError, podemos lidar com ela aqui
                print(f"Erro ao executar a transação: {exc_value}")
                self.connection.rollback()
            else:
                # Caso contrário, a transação foi bem-sucedida, então fazemos o commit
                self.connection.commit()
            self.connection.close()

# Usando o contexto manager com tratamento de exceções
with DatabaseConnection('localhost', 5432) as conn:
    # Execute uma operação no banco de dados
    result = execute_query(conn, "INSERT INTO tabela (coluna) VALUES (valor)")

# O código continua a ser executado após o tratamento da exceção, ou o commit é feito.
```

Em resumo, ao criar um contexto manager com classes em Python, você pode personalizar o comportamento em caso de exceções tanto no método `__enter__` quanto no método `__exit__`, o que permite um controle mais granular sobre o tratamento de erros e a liberação de recursos.

## Decorador `contextlib.contextmanager`

O `contextlib.contextmanager` é um decorador em Python que simplifica a criação de context managers usando geradores. Permite que você defina um contexto manager usando uma função geradora, tornando a criação de context managers mais concisa e legível. Isso é particularmente útil quando você precisa criar context managers simples e não deseja criar uma classe completa com os métodos `__enter__` e `__exit__`.

Aqui está um exemplo de como usar `contextlib.contextmanager` para criar um contexto manager:

```python
from contextlib import contextmanager

@contextmanager
def simple_context_manager():
    # Código de configuração que ocorre no início do bloco "with"
    print("Entrando no contexto")
    yield  # O valor opcional que você deseja associar a "as" no bloco "with"
    # Código de limpeza que ocorre no final do bloco "with"
    print("Saindo do contexto")

# Usando o contexto manager
with simple_context_manager() as value:
    print("Dentro do bloco 'with'")
    print(f"Valor associado: {value}")

# O código continua a ser executado após o bloco "with"
```

Neste exemplo, o decorador `@contextmanager` transforma a função `simple_context_manager` em um contexto manager. A função geradora é definida usando a palavra-chave `yield`. O código que está acima do `yield` é executado no início do bloco `with`, e o código abaixo do `yield` é executado no final do bloco `with`. O valor retornado após o `yield` pode ser opcionalmente associado a uma variável após o `as` no bloco `with`.

O resultado da execução deste código será:

```
Entrando no contexto
Dentro do bloco 'with'
Valor associado: None
Saindo do contexto
```

O uso de `contextlib.contextmanager` é uma maneira conveniente de criar context managers para gerenciar recursos e garantir a execução correta de código de configuração e limpeza dentro de um bloco `with`.

## Funções decoradores com Classes

Em Python, os decoradores são uma maneira poderosa de modificar o comportamento de funções ou métodos. Eles também podem ser usados em classes para modificar o comportamento de métodos de classe, como `__init__`, `__str__`, `__repr__` e outros. Vou explicar como você pode usar um decorador para modificar o método `__repr__` de uma classe.

Primeiro, vamos entender o que é o método `__repr__` em Python. O método `__repr__` é usado para fornecer uma representação de string "oficial" de um objeto. Isso significa que o resultado do método `__repr__` deve ser uma string que, quando passada para a função `eval()`, deve criar um objeto idêntico ao original. O objetivo principal do método `__repr__` é fornecer uma representação legível para programadores.

Aqui está um exemplo simples de uma classe com o método `__repr__`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
```

Neste exemplo, o método `__repr__` retorna uma string que representa uma instância da classe `Person`.

Agora, vamos criar um decorador que modifica o comportamento do método `__repr__` de uma classe:

```python
def uppercase_repr(cls):
    original_repr = cls.__repr__

    def new_repr(self):
        original_result = original_repr(self)
        return original_result.upper()

    cls.__repr__ = new_repr
    return cls
```

O decorador `uppercase_repr` pega a classe como argumento, obtém o método `__repr__` original, cria um novo método `new_repr` que chama o método original e converte a representação em maiúsculas, em seguida, atribui o novo método `new_repr` à classe. Agora, quando você aplica esse decorador a uma classe, ele transformará automaticamente a representação em maiúsculas:

```python
@uppercase_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(person)  # Saída: PERSON('ALICE', 30)
```

Neste exemplo, aplicamos o decorador `uppercase_repr` à classe `Person`, e quando chamamos `print(person)`, a representação é automaticamente convertida em maiúsculas.

Essa é uma maneira de usar decoradores para modificar o comportamento de métodos de classe, como `__repr__`, em Python. Isso pode ser útil para adicionar funcionalidades adicionais ou personalizadas a classes existentes sem modificar seu código fonte diretamente.

##  Funções decoradores em classes no python

Em Python, os decoradores são uma maneira poderosa de modificar o comportamento de funções ou métodos. Eles também podem ser usados em classes para modificar o comportamento de métodos de classe, como `__init__`, `__str__`, `__repr__` e outros. Vou explicar como você pode usar um decorador para modificar o método `__repr__` de uma classe.

Primeiro, vamos entender o que é o método `__repr__` em Python. O método `__repr__` é usado para fornecer uma representação de string "oficial" de um objeto. Isso significa que o resultado do método `__repr__` deve ser uma string que, quando passada para a função `eval()`, deve criar um objeto idêntico ao original. O objetivo principal do método `__repr__` é fornecer uma representação legível para programadores.

Aqui está um exemplo simples de uma classe com o método `__repr__`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
```

Neste exemplo, o método `__repr__` retorna uma string que representa uma instância da classe `Person`.

Agora, vamos criar um decorador que modifica o comportamento do método `__repr__` de uma classe:

```python
def uppercase_repr(cls):
    original_repr = cls.__repr__

    def new_repr(self):
        original_result = original_repr(self)
        return original_result.upper()

    cls.__repr__ = new_repr
    return cls
```

O decorador `uppercase_repr` pega a classe como argumento, obtém o método `__repr__` original, cria um novo método `new_repr` que chama o método original e converte a representação em maiúsculas, em seguida, atribui o novo método `new_repr` à classe. Agora, quando você aplica esse decorador a uma classe, ele transformará automaticamente a representação em maiúsculas:

```python
@uppercase_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(person)  # Saída: PERSON('ALICE', 30)
```

Neste exemplo, aplicamos o decorador `uppercase_repr` à classe `Person`, e quando chamamos `print(person)`, a representação é automaticamente convertida em maiúsculas.

Essa é uma maneira de usar decoradores para modificar o comportamento de métodos de classe, como `__repr__`, em Python. Isso pode ser útil para adicionar funcionalidades adicionais ou personalizadas a classes existentes sem modificar seu código fonte diretamente.

## Classes decoradoras:

Em Python, as classes decoradoras são uma técnica avançada que permite modificar ou estender o comportamento de funções, métodos ou classes de uma maneira modular e reutilizável. As classes decoradoras são usadas principalmente em conjunto com funções decoradoras para adicionar funcionalidades extras a objetos de função ou métodos de classe sem modificar diretamente o código-fonte original.

Aqui está uma visão geral de como as classes decoradoras funcionam em Python:

1. Classes decoradoras:
   - Uma classe decoradora é uma classe que implementa os métodos especiais `__init__` e `__call__`.
   - O método `__init__` é usado para configurar a classe decoradora e armazenar qualquer estado necessário.
   - O método `__call__` é invocado quando um objeto da classe decoradora é chamado como uma função.

2. Funções decoradoras:
   - Funções decoradoras são usadas para modificar o comportamento de funções ou métodos.
   - Uma função decoradora recebe como argumento a função que ela está decorando e pode fazer qualquer manipulação desejada nessa função.
   - A função decoradora geralmente retorna uma nova função (ou método) que é uma versão modificada da função original.

Aqui está um exemplo simples de como criar e usar uma classe decoradora em Python:

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Antes da chamada da função")
        result = self.func(*args, **kwargs)
        print("Depois da chamada da função")
        return result

@MyDecorator
def minha_funcao():
    print("Executando minha_funcao")

minha_funcao()
```

Neste exemplo, `MyDecorator` é uma classe decoradora que adiciona um comportamento adicional antes e depois da chamada da função `minha_funcao`. O uso do `@MyDecorator` acima da definição da função é uma forma de aplicar a decoração à função.

Ao executar `minha_funcao()`, você verá a saída:

```
Antes da chamada da função
Executando minha_funcao
Depois da chamada da função
```

As classes decoradoras são úteis quando você precisa aplicar a mesma funcionalidade a várias funções ou métodos em seu código, pois permitem encapsular essa funcionalidade em uma classe reutilizável. Isso pode ser especialmente útil em situações como loggin, autenticação, validação de entrada e muito mais.

## Teoria das Metaclasses(avançado)

Em Python, metaclasses são classes especiais que definem o comportamento de outras classes, conhecidas como "classes de instância". Basicamente, uma metaclasse é uma classe de uma classe, o que significa que ela controla como as classes são criadas e se comportam. As metaclasses são uma parte avançada da linguagem Python e não são frequentemente utilizadas na programação cotidiana, mas podem ser poderosas quando necessário.

Aqui estão alguns conceitos e informações importantes sobre metaclasses em Python:

1. **Classes são objetos:** Em Python, as classes são objetos de primeira classe. Isso significa que você pode atribuí-las a variáveis, passá-las como argumentos de funções e criar novas classes em tempo de execução. Isso é fundamental para entender metaclasses.

2. **type - A metaclass padrão:** Todas as classes em Python têm uma metaclass associada, e por padrão, essa metaclass é a classe `type`. `type` é uma metaclass embutida que é responsável por criar todas as classes em Python. Você pode usar `type` para criar novas classes também.

   Exemplo de criação de classe usando `type`:

   ```python
   MinhaClasse = type('MinhaClasse', (object,), {'atributo': 42})
   ```

3. **Personalizando metaclasses:** Você pode criar suas próprias metaclasses personalizadas definindo uma classe que herda de `type` e sobrescrevendo seus métodos especiais, como `__new__` e `__init__`. Esses métodos permitem que você controle como as classes são criadas e personalizem seu comportamento.

   ```python
   class MinhaMetaclasse(type):
       def __new__(cls, nome, bases, attrs):
           # Personalize a criação da classe aqui
           return super().__new__(cls, nome, bases, attrs)

   class MinhaClasse(metaclass=MinhaMetaclasse):
       pass
   ```

4. **Uso de metaclasses:** As metaclasses podem ser usadas para várias finalidades, como a aplicação de regras de validação, a injeção automática de métodos ou atributos em classes, a criação de classes de registro, entre outras. Elas são frequentemente usadas em estruturas e bibliotecas avançadas que precisam de metadados adicionais sobre as classes.

5. **Cuidado ao usar metaclasses:** Embora as metaclasses ofereçam um poder considerável, é importante usá-las com cautela. O código que faz uso extensivo de metaclasses pode se tornar complexo e difícil de entender. Portanto, é geralmente recomendado recorrer a metaclasses apenas quando não há alternativa mais simples para atingir o objetivo desejado.

Em resumo, metaclasses são uma ferramenta avançada em Python que permite personalizar a criação e o comportamento das classes. Elas são mais úteis em cenários complexos onde é necessário controlar o comportamento das classes de forma mais profunda. Para a maioria dos casos, o uso de classes normais é suficiente.
