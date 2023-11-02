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



