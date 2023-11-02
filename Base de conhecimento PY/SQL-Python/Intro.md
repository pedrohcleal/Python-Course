# Intro Python + SQL

O SQLite é um sistema de gerenciamento de banco de dados relacional (RDBMS) embutido, que significa que não requer um servidor ou configurações complexas para ser usado. O SQLite é muito popular no desenvolvimento de aplicativos devido à sua simplicidade, eficiência e facilidade de uso. No Python, você pode usar a biblioteca `sqlite3` para interagir com bancos de dados SQLite.

Aqui estão os passos básicos para usar o SQLite no Python:

1. Importe a biblioteca `sqlite3`:

   ```python
   import sqlite3
   ```

2. Conecte-se a um banco de dados ou crie um novo:

   ```python
   conn = sqlite3.connect('nome_do_banco_de_dados.db')
   ```

   Substitua 'nome_do_banco_de_dados.db' pelo nome que você deseja dar ao seu banco de dados. Se o banco de dados não existir, ele será criado automaticamente.

3. Crie um objeto `cursor`:

   ```python
   cursor = conn.cursor()
   ```

   O cursor é usado para executar comandos SQL no banco de dados.

4. Execute comandos SQL:

   Você pode executar comandos SQL, como criar tabelas, inserir dados, atualizar registros e consultar dados, usando o cursor. Aqui estão alguns exemplos:

   - Criar uma tabela:

     ```python
     cursor.execute('CREATE TABLE IF NOT EXISTS minha_tabela (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')
     ```

   - Inserir dados:

     ```python
     cursor.execute('INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)', ('Alice', 30))
     ```

   - Consultar dados:

     ```python
     cursor.execute('SELECT * FROM minha_tabela')
     rows = cursor.fetchall()
     for row in rows:
         print(row)
     ```

5. Comitar as alterações e fechar a conexão:

   Após executar as operações desejadas no banco de dados, você deve chamar `commit` para salvar as alterações e, em seguida, fechar a conexão:

   ```python
   conn.commit()
   conn.close()
   ```

6. Tratamento de exceções:

   Lembre-se de tratar exceções ao trabalhar com SQLite no Python para lidar com erros de maneira apropriada.

O SQLite é uma ótima escolha para aplicativos leves que precisam de um banco de dados local. Ele é amplamente utilizado em aplicativos móveis, desktop e até mesmo em sistemas incorporados devido à sua simplicidade e desempenho.

## Inserindo dados na tabela

Para inserir dados em uma tabela usando o SQLite no Python, você pode usar o comando SQL `INSERT INTO`. Aqui estão os comandos básicos para inserir dados em uma tabela:

1. Inserção de um único registro:

   Você pode inserir um único registro na tabela da seguinte forma:

   ```python
   cursor.execute("INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3) VALUES (?, ?, ?)", (valor1, valor2, valor3))
   ```

   Substitua `nome_da_tabela` pelo nome da tabela em que você deseja inserir os dados. `coluna1`, `coluna2`, `coluna3`, etc., devem ser substituídos pelos nomes das colunas nas quais você deseja inserir os valores. `valor1`, `valor2`, `valor3`, etc., devem ser substituídos pelos valores que você deseja inserir.

   Exemplo:

   ```python
   cursor.execute("INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)", ('Alice', 30))
   ```

2. Inserção de vários registros de uma só vez:

   Para inserir vários registros de uma só vez, você pode usar o método `executemany` do cursor. Isso é útil quando você deseja inserir uma lista de registros de uma só vez. Aqui está um exemplo:

   ```python
   registros = [
       ('Bob', 25),
       ('Carol', 28),
       ('David', 32)
   ]
   cursor.executemany("INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)", registros)
   ```

   Neste exemplo, uma lista de tuplas chamada `registros` é inserida na tabela `minha_tabela`, onde cada tupla contém o nome e a idade.

3. Usando placeholders e segurança contra SQL Injection:

   É importante usar placeholders (no exemplo, `?`) ao inserir dados em uma tabela para evitar ataques de SQL Injection. O SQLite3 cuida da formatação segura dos valores.

Após a execução do comando `execute` ou `executemany`, é importante chamar `commit` para confirmar a inserção dos dados no banco de dados:

```python
conn.commit()
```

Lembre-se de que, antes de executar comandos de inserção, você deve ter uma conexão aberta com o banco de dados e um cursor associado a essa conexão. Certifique-se também de que a tabela na qual você está inserindo os dados já tenha sido criada com as colunas apropriadas.

