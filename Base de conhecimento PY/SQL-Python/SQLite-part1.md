# SQLite + Python

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

## Como excluir dados da tabela, limpar por inteira e resetar sequencia da tabulação

Para excluir dados de uma tabela no SQLite usando Python, você pode usar o comando SQL `DELETE`. Você pode excluir registros específicos ou limpar a tabela inteira. Para redefinir a sequência da tabela, você pode usar o comando SQL `UPDATE`. Aqui estão exemplos de como fazer isso:

1. Excluir registros específicos:

   Você pode excluir registros com base em condições específicas. Suponhamos que você queira excluir todos os registros onde a coluna `idade` seja igual a 30:

   ```python
   cursor.execute("DELETE FROM minha_tabela WHERE idade = 30")
   conn.commit()
   ```

   Isso exclui todos os registros em `minha_tabela` onde a idade é igual a 30.

2. Limpar a tabela inteira:

   Para excluir todos os registros da tabela e, essencialmente, limpá-la completamente, você pode fazer o seguinte:

   ```python
   cursor.execute("DELETE FROM minha_tabela")
   conn.commit()
   ```

   Isso excluirá todos os registros da tabela `minha_tabela`.

3. Resetar a sequência da tabela (reiniciar o contador de autoincremento):

   Se a tabela tem uma coluna com uma sequência automática (geralmente uma coluna `INTEGER PRIMARY KEY`), você pode redefinir a sequência (reiniciar o contador de autoincremento) da seguinte maneira:

   ```python
   cursor.execute("DELETE FROM sqlite_sequence WHERE name='minha_tabela'")
   conn.commit()
   ```

   Isso excluirá a entrada correspondente na tabela `sqlite_sequence` para a tabela `minha_tabela`, o que fará com que o contador de sequência seja redefinido quando você inserir um novo registro na tabela.

Lembre-se de que é importante chamar `commit` após a execução do comando `DELETE` para confirmar as alterações no banco de dados. Certifique-se de que você tem uma conexão aberta com o banco de dados e um cursor associado a essa conexão antes de executar os comandos.

## Placeholders (segurança)

O uso de placeholders é uma prática importante ao executar consultas SQL para aumentar a segurança e evitar ataques de SQL Injection. Em Python, você pode usar placeholders com a biblioteca `sqlite3` para garantir que os valores sejam escapados e tratados corretamente. Abaixo estão as etapas para usar placeholders ao executar consultas SQL no SQLite com Python:

1. Importe a biblioteca `sqlite3` e conecte-se ao banco de dados:

   ```python
   import sqlite3

   conn = sqlite3.connect('nome_do_banco_de_dados.db')
   cursor = conn.cursor()
   ```

   Substitua `'nome_do_banco_de_dados.db'` pelo nome do seu banco de dados.

2. Use placeholders na consulta SQL:

   Ao criar sua consulta SQL, substitua os valores que você deseja inserir por placeholders `?`. Por exemplo:

   ```python
   nome = 'Alice'
   idade = 30
   cursor.execute("INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)", (nome, idade))
   ```

   Os placeholders `?` serão preenchidos com os valores de `nome` e `idade`. Isso garante que os valores sejam devidamente escapados e evita possíveis injeções de SQL.

3. Use placeholders com segurança em consultas dinâmicas:

   Se você estiver criando consultas SQL dinâmicas, certifique-se de que as variáveis sejam passadas corretamente usando placeholders. Por exemplo:

   ```python
   nome = 'Alice'
   idade = 30
   consulta = "INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)"
   cursor.execute(consulta, (nome, idade))
   ```

   Certifique-se de que as variáveis usadas nos placeholders sejam passadas como uma tupla no segundo argumento de `execute`.

4. Comitar as alterações e fechar a conexão:

   Após executar a consulta, não se esqueça de chamar `commit` para salvar as alterações e, em seguida, fechar a conexão:

   ```python
   conn.commit()
   conn.close()
   ```

Usar placeholders é uma prática fundamental para evitar problemas de segurança, como SQL Injection, pois a biblioteca `sqlite3` lida com a formatação segura dos valores para você, garantindo que os dados sejam tratados corretamente.

## Executemany

O método `executemany` é uma função oferecida pela biblioteca `sqlite3` em Python que permite executar a mesma consulta SQL várias vezes com diferentes conjuntos de parâmetros de maneira eficiente. Isso é útil quando você deseja inserir múltiplos registros em uma tabela com a mesma consulta SQL, evitando a necessidade de executar a consulta várias vezes manualmente.

A assinatura do método `executemany` é a seguinte:

```python
cursor.executemany(consulta, sequencia_de_parametros)
```

- `cursor`: Um objeto de cursor que representa a conexão com o banco de dados.
- `consulta`: A consulta SQL que você deseja executar. A consulta deve conter os placeholders `?` que serão substituídos pelos parâmetros da sequência de parâmetros.
- `sequencia_de_parametros`: Uma sequência iterável (geralmente uma lista de tuplas) que contém os parâmetros que serão usados para substituir os placeholders na consulta.

A principal vantagem do método `executemany` é a eficiência. Em vez de executar a mesma consulta várias vezes em um loop, você pode usar `executemany` para consolidar a execução de várias consultas em uma única operação. Isso reduz a sobrecarga de comunicação com o banco de dados e pode melhorar significativamente o desempenho ao inserir grandes quantidades de dados.

Aqui está um exemplo de uso do `executemany` para inserir vários registros em uma tabela:

```python
registros = [
    ('Alice', 30),
    ('Bob', 25),
    ('Carol', 28)
]

consulta = "INSERT INTO minha_tabela (nome, idade) VALUES (?, ?)"

cursor.executemany(consulta, registros)
conn.commit()
```

Neste exemplo, a consulta SQL é executada três vezes com diferentes conjuntos de parâmetros, com base nos valores contidos na lista `registros`. Os registros são inseridos na tabela `minha_tabela` de uma só vez, melhorando a eficiência em comparação com a execução da consulta em um loop. Certifique-se de chamar `commit` para salvar as alterações no banco de dados após a execução do `executemany`.

## SELECT do SQL com fetch no SQLite3

Quando você executa uma consulta SELECT no SQLite3 em Python, você obtém um conjunto de resultados como resposta. Para recuperar os dados desse conjunto de resultados, você pode usar métodos como `fetchone()`, `fetchall()`, ou até mesmo iterar diretamente pelo cursor. Aqui está uma descrição desses métodos:

1. `fetchone()`: Este método é usado para recuperar a próxima linha do conjunto de resultados como uma tupla. Se não houver mais linhas a serem recuperadas, ele retornará `None`. Você pode chamar `fetchone()` repetidamente para recuperar cada linha do resultado.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM minha_tabela")
   primeira_linha = cursor.fetchone()
   segunda_linha = cursor.fetchone()
   ```

2. `fetchall()`: Este método é usado para recuperar todas as linhas do conjunto de resultados como uma lista de tuplas. Cada tupla representa uma linha de dados. Se não houver resultados, ele retornará uma lista vazia.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM minha_tabela")
   resultados = cursor.fetchall()
   for linha in resultados:
       print(linha)
   ```

3. Iterar diretamente pelo cursor: Você pode iterar diretamente pelo cursor usando um loop `for`. Isso permite que você percorra as linhas do conjunto de resultados uma por uma sem a necessidade de chamar `fetchone()` explicitamente.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM minha_tabela")
   for linha in cursor:
       print(linha)
   ```

   Quando você itera diretamente pelo cursor, ele se comporta como um iterável e automaticamente chama `fetchone()` para você.

4. Usando `fetchmany()`: Você também pode usar `fetchmany(n)` para recuperar um número específico de linhas do conjunto de resultados de uma só vez. Por exemplo, `fetchmany(5)` recuperaria as próximas 5 linhas como uma lista de tuplas.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM minha_tabela")
   primeiras_cinco_linhas = cursor.fetchmany(5)
   ```

Dependendo do tamanho do conjunto de resultados e da quantidade de dados que você deseja recuperar, você pode escolher o método mais apropriado. Certifique-se de chamar `execute` antes de chamar qualquer um desses métodos para executar sua consulta SELECT. Além disso, é importante lembrar de chamar `commit` se você tiver realizado modificações no banco de dados que precisam ser confirmadas.
