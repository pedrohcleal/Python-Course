# SQLite part2

## Connection Management Pattern

O **Connection Management Pattern** no contexto do SQLite3 em Python refere-se às práticas recomendadas para gerenciar conexões com o banco de dados de forma eficiente e segura. Isso é particularmente importante em aplicações que realizam múltiplas operações de banco de dados ou que são acessadas por múltiplas threads/processos. Abaixo estão os componentes principais e práticas comuns associadas ao gerenciamento de conexões no SQLite3 em Python:

### 1. Abertura e Fechamento de Conexões
#### Abertura de Conexões
Ao conectar-se a um banco de dados SQLite3, você usa a função `sqlite3.connect()`, que retorna um objeto de conexão.

```python
import sqlite3

conn = sqlite3.connect('example.db')
```

#### Fechamento de Conexões
É essencial fechar a conexão após concluir as operações com o banco de dados para liberar recursos.

```python
conn.close()
```

### 2. Uso de Context Managers
Usar um context manager (`with` statement) garante que a conexão será fechada automaticamente após o bloco de código ser executado, mesmo que ocorra uma exceção.

```python
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
```

### 3. Reutilização de Conexões
Para evitar a sobrecarga de abrir e fechar conexões repetidamente, especialmente em aplicações de longo prazo, é comum reutilizar conexões existentes. Um padrão comum é usar um pool de conexões ou manter uma única conexão global.

```python
class Database:
    _connection = None

    @staticmethod
    def get_connection():
        if Database._connection is None:
            Database._connection = sqlite3.connect('example.db')
        return Database._connection
```

### 4. Gerenciamento de Transações
SQLite3 suporta transações que podem ser usadas para garantir a consistência do banco de dados. Você pode iniciar uma transação e confirmar (`commit`) ou reverter (`rollback`) conforme necessário.

```python
conn = sqlite3.connect('example.db')
try:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO my_table (column) VALUES (?)', (value,))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f'Error: {e}')
finally:
    conn.close()
```

### 5. Concorrência e Thread Safety
SQLite3 permite o uso em múltiplas threads, mas uma única conexão não é segura para threads. Para aplicações multithreaded, cada thread deve ter sua própria conexão. Isso pode ser gerenciado usando um pool de conexões ou um `thread-local storage`.

```python
import threading

class Database:
    _local = threading.local()

    @staticmethod
    def get_connection():
        if not hasattr(Database._local, 'connection'):
            Database._local.connection = sqlite3.connect('example.db')
        return Database._local.connection
```

### 6. Pool de Conexões
Embora o SQLite3 não tenha suporte nativo para pool de conexões, você pode implementar um simples pool manualmente ou usar bibliotecas de terceiros.

```python
from queue import Queue

class ConnectionPool:
    def __init__(self, database, pool_size=5):
        self._pool = Queue(pool_size)
        for _ in range(pool_size):
            self._pool.put(sqlite3.connect(database))
    
    def get_connection(self):
        return self._pool.get()
    
    def return_connection(self, connection):
        self._pool.put(connection)

pool = ConnectionPool('example.db')

# Usando uma conexão do pool
conn = pool.get_connection()
try:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
finally:
    pool.return_connection(conn)
```

### 7. Erros e Exceções
Tratar erros e exceções é parte do gerenciamento de conexões. O SQLite3 em Python lança exceções específicas que podem ser tratadas para garantir que as conexões sejam sempre fechadas apropriadamente.

```python
try:
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
except sqlite3.Error as e:
    print(f'SQLite error: {e}')
finally:
    if conn:
        conn.close()
```

Implementar o Connection Management Pattern de maneira eficaz é crucial para a robustez e eficiência de uma aplicação que utiliza o SQLite3. Isso ajuda a evitar problemas de desempenho e garante a integridade dos dados.

## Decorador @app.teardown_appcontext

O decorador `@app.teardown_appcontext` é usado no Flask, um framework web em Python, para registrar uma função que deve ser executada quando o contexto da aplicação é finalizado. Este contexto é finalizado no final de cada solicitação. A principal finalidade desse decorador é realizar operações de limpeza, como fechar conexões de banco de dados ou liberar outros recursos que foram alocados durante a solicitação.

### Contexto da Aplicação no Flask
No Flask, há dois tipos de contextos: o contexto da solicitação e o contexto da aplicação. O contexto da aplicação é criado quando a aplicação é inicializada e destruído quando a aplicação é finalizada. Ele é usado para armazenar dados globais que podem ser acessados durante toda a vida útil da aplicação.

### Uso do Decorador `@app.teardown_appcontext`
O decorador `@app.teardown_appcontext` é aplicado a uma função que deve ser chamada quando o contexto da aplicação está prestes a ser finalizado. Essa função pode ser usada para realizar qualquer tarefa de limpeza necessária.

### Exemplo de Uso
Um exemplo comum é fechar a conexão com o banco de dados ao final de cada solicitação. Isso garante que todos os recursos sejam liberados apropriadamente.

```python
from flask import Flask, g
import sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('example.db')
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    # Operações com o banco de dados
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

### Explicação do Código
1. **Inicialização da Aplicação**:
   ```python
   app = Flask(__name__)
   ```
   Inicializa a aplicação Flask.

2. **Função `get_db`**:
   ```python
   def get_db():
       if 'db' not in g:
           g.db = sqlite3.connect('example.db')
       return g.db
   ```
   Esta função obtém uma conexão com o banco de dados e a armazena no contexto global (`g`). Se a conexão já existir, ela é reutilizada.

3. **Função `close_db`**:
   ```python
   @app.teardown_appcontext
   def close_db(exception):
       db = g.pop('db', None)
       if db is not None:
           db.close()
   ```
   Esta função é registrada com o decorador `@app.teardown_appcontext`. Ela é chamada quando o contexto da aplicação é finalizado. A função remove a conexão do contexto global (`g`) e fecha a conexão se ela existir.

4. **Rota `index`**:
   ```python
   @app.route('/')
   def index():
       db = get_db()
       # Operações com o banco de dados
       return 'Hello, World!'
   ```
   Define uma rota simples que obtém uma conexão com o banco de dados e executa operações (não especificadas no exemplo).

### Vantagens do Uso de `@app.teardown_appcontext`
- **Liberação de Recursos**: Garante que todos os recursos, como conexões de banco de dados, sejam liberados corretamente ao final de cada solicitação.
- **Segurança**: Reduz o risco de vazamento de recursos, que pode levar a problemas de desempenho e falhas na aplicação.
- **Manutenção do Código**: Facilita a manutenção do código, separando claramente as operações de limpeza do restante da lógica da aplicação.

Usar o `@app.teardown_appcontext` é uma prática recomendada em aplicações Flask para garantir que os recursos sejam gerenciados de forma eficiente e segura.
