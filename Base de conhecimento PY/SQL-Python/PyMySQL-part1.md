# PyMySql

A `pymysql` é uma biblioteca Python que fornece uma interface para se conectar a bancos de dados MySQL a partir de programas Python. Ela permite que você execute consultas SQL, recupere e manipule dados, e gerencie conexões com bancos de dados MySQL de forma programática. Abaixo estão algumas informações importantes sobre a biblioteca `pymysql`:

1. Instalação:
   Para usar o `pymysql`, você precisa instalá-lo em seu ambiente Python. Isso pode ser feito através do `pip`, o gerenciador de pacotes do Python:

   ```
   pip install pymysql
   ```

2. Conexão com o banco de dados:
   Antes de executar consultas no MySQL, você precisa estabelecer uma conexão com o banco de dados. Você pode fazer isso usando o método `connect()` da `pymysql`, fornecendo informações como nome de usuário, senha, host e nome do banco de dados.

   Exemplo de código:

   ```python
   import pymysql

   # Conectar ao banco de dados
   connection = pymysql.connect(
       host='localhost',
       user='seu_usuario',
       password='sua_senha',
       db='seu_banco_de_dados'
   )
   ```

3. Execução de consultas:
   Depois de estabelecer uma conexão, você pode executar consultas SQL no banco de dados. A `pymysql` fornece métodos para executar consultas, inserções, atualizações e exclusões de forma simples.

   Exemplo de consulta de seleção:

   ```python
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM tabela")
   results = cursor.fetchall()
   cursor.close()
   ```

4. Gerenciamento de transações:
   A `pymysql` oferece suporte a transações, permitindo que você inicie, comprometa ou reverta transações no banco de dados, garantindo a integridade dos dados.

   Exemplo de início de transação:

   ```python
   connection = pymysql.connect(...)
   try:
       with connection.cursor() as cursor:
           # Iniciar uma transação
           connection.begin()
           # Executar consultas e operações no banco de dados
           # Se tudo correr bem, faça o commit da transação
           connection.commit()
   except:
       # Em caso de erro, faça o rollback da transação
       connection.rollback()
   finally:
       connection.close()
   ```

5. Fechamento de conexão:
   É importante fechar a conexão com o banco de dados quando você terminar de usá-la para liberar recursos e evitar vazamentos de memória.

   ```python
   connection.close()
   ```

A `pymysql` é uma biblioteca popular para interagir com bancos de dados MySQL em Python e é amplamente usada em aplicativos que precisam de acesso a bancos de dados relacionais. Certifique-se de instalar a biblioteca, criar uma conexão segura com o banco de dados e seguir as melhores práticas de programação ao usá-la para evitar problemas de segurança e de desempenho.

## TRUNCATE & INSERT

No `pymysql`, que é uma biblioteca Python usada para interagir com bancos de dados MySQL, você pode realizar operações como o `TRUNCATE` e `INSERT` para manipular tabelas no banco de dados. Aqui está uma descrição de como essas operações podem ser realizadas:

1. **TRUNCATE**:

   A operação `TRUNCATE` é usada para excluir todos os registros de uma tabela, mas manter a estrutura da tabela intacta. Esta operação é irreversível e geralmente é usada quando você deseja limpar completamente os dados de uma tabela sem remover a tabela em si. Aqui está como você pode usar o `TRUNCATE` com o `pymysql`:

   ```python
   import pymysql

   # Estabeleça uma conexão com o banco de dados
   connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

   try:
       # Crie um cursor
       cursor = connection.cursor()
       
       # Execute a operação TRUNCATE em uma tabela
       table_name = 'sua_tabela'
       cursor.execute(f'TRUNCATE TABLE {table_name}')
       
       # Faça o commit para aplicar as alterações
       connection.commit()

   except pymysql.Error as e:
       print(f"Erro ao truncar a tabela: {e}")

   finally:
       # Feche o cursor e a conexão
       cursor.close()
       connection.close()
   ```

2. **INSERT**:

   A operação `INSERT` é usada para adicionar novos registros a uma tabela. Você pode inserir dados em uma tabela usando o `pymysql` da seguinte maneira:

   ```python
   import pymysql

   # Estabeleça uma conexão com o banco de dados
   connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

   try:
       # Crie um cursor
       cursor = connection.cursor()
       
       # Execute a operação INSERT em uma tabela
       data = {
           'campo1': 'valor1',
           'campo2': 'valor2',
       }
       table_name = 'sua_tabela'
       query = f"INSERT INTO {table_name} (campo1, campo2) VALUES (%s, %s)"
       cursor.execute(query, (data['campo1'], data['campo2']))
       
       # Faça o commit para aplicar as alterações
       connection.commit()

   except pymysql.Error as e:
       print(f"Erro ao inserir dados na tabela: {e}")

   finally:
       # Feche o cursor e a conexão
       cursor.close()
       connection.close()
   ```

   Neste exemplo, você deve adaptar a estrutura da tabela e os valores que deseja inserir de acordo com suas necessidades.

Lembre-se de que, ao executar operações que modificam o banco de dados, como o `TRUNCATE` ou `INSERT`, é importante lidar com exceções e realizar operações de forma segura, incluindo o uso do `commit` para confirmar as alterações no banco de dados e o fechamento adequado dos cursores e conexões para evitar vazamentos de recursos.

## Como evitar sql injection ao usar placeholders

Para evitar injeção de SQL ao usar placeholders em consultas SQL, você está no caminho certo, pois o uso de placeholders é uma das práticas mais eficazes para proteger seu código contra esse tipo de ataque. No entanto, você deve seguir algumas diretrizes específicas ao usar placeholders para garantir a segurança de suas consultas. Aqui estão algumas dicas:

1. **Use Bibliotecas Seguras**:

   Em vez de construir manualmente suas consultas SQL com strings interpoladas, use bibliotecas de acesso a banco de dados que suportam placeholders. A maioria das bibliotecas modernas, incluindo o `pymysql`, suporta essa funcionalidade. Ao usar essas bibliotecas, você delega a responsabilidade de lidar com os placeholders de maneira segura.

2. **Não Concatene Dados Não Confiáveis**:

   Nunca concatene diretamente dados de entrada do usuário em consultas SQL. Em vez disso, forneça os valores como argumentos separados para a função de execução da consulta. Por exemplo, não faça o seguinte:

   ```python
   user_input = request.form['username']
   cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
   ```

   Em vez disso, use placeholders:

   ```python
   user_input = request.form['username']
   cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
   ```

3. **Evite Dados Não Sanitizados**:

   Certifique-se de que os dados de entrada do usuário sejam devidamente sanitizados antes de usá-los em consultas. Isso inclui a validação e limpeza dos dados para remover qualquer característica maliciosa. No entanto, a melhor prática é confiar nos placeholders e não depender da sanitização.

4. **Use Parâmetros Nomeados**:

   Além dos marcadores de posição posicionais, algumas bibliotecas de acesso a banco de dados também suportam marcadores de posição nomeados. Isso pode tornar seu código mais legível e seguro, pois você faz referência aos valores por nome em vez de posição. Por exemplo:

   ```python
   user_input = request.form['username']
   cursor.execute("SELECT * FROM users WHERE username = %(name)s", {'name': user_input})
   ```

5. **Limite as Permissões do Banco de Dados**:

   Certifique-se de que sua aplicação tenha permissões mínimas no banco de dados. Evite conceder privilégios de superusuário, pois isso pode permitir que atacantes potenciais façam mais danos em caso de sucesso na injeção de SQL.

6. **Auditoria e Monitoramento**:

   Implemente auditoria e monitoramento de consultas SQL em seu aplicativo para identificar atividades suspeitas ou tentativas de injeção de SQL.

7. **Atualizações e Patches**:

   Mantenha sua biblioteca de acesso a banco de dados atualizada para garantir que qualquer correção de segurança seja aplicada.

8. **Treinamento e Conscientização**:

   Eduque sua equipe de desenvolvimento sobre as melhores práticas de segurança em relação às consultas SQL e à prevenção de injeção de SQL.

Lembrando que a prevenção da injeção de SQL é uma parte crítica da segurança de aplicativos da web. Ao seguir as melhores práticas, você reduz significativamente o risco de vulnerabilidades desse tipo.

## Como inserir valor usando dicionarios ou só utilizando iteráveis

Para inserir valores em um banco de dados MySQL usando o `pymysql`, você pode usar dicionários ou iteráveis, como listas ou tuplas, dependendo de como você deseja fornecer os valores dos campos na sua consulta SQL. A seguir, mostrarei como inserir valores usando ambas as abordagens.

Usando um dicionário:
```python
import pymysql

# Dados a serem inseridos
data = {
    'campo1': 'valor1',
    'campo2': 'valor2',
    'campo3': 42
}

# Estabeleça uma conexão com o banco de dados
connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

try:
    # Crie um cursor
    cursor = connection.cursor()
    
    # Construa a consulta SQL inserindo valores do dicionário
    table_name = 'sua_tabela'
    columns = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    
    # Execute a consulta com os valores do dicionário
    cursor.execute(query, tuple(data.values()))
    
    # Faça o commit para aplicar as alterações
    connection.commit()

except pymysql.Error as e:
    print(f"Erro ao inserir dados na tabela: {e}")

finally:
    # Feche o cursor e a conexão
    cursor.close()
    connection.close()
```

Usando uma lista ou tupla:
```python
import pymysql

# Dados a serem inseridos como uma lista ou tupla
data = ('valor1', 'valor2', 42)

# Estabeleça uma conexão com o banco de dados
connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

try:
    # Crie um cursor
    cursor = connection.cursor()
    
    # Construa a consulta SQL inserindo valores da lista/tupla
    table_name = 'sua_tabela'
    query = f"INSERT INTO {table_name} (campo1, campo2, campo3) VALUES (%s, %s, %s)"
    
    # Execute a consulta com os valores da lista/tupla
    cursor.execute(query, data)
    
    # Faça o commit para aplicar as alterações
    connection.commit()

except pymysql.Error as e:
    print(f"Erro ao inserir dados na tabela: {e}")

finally:
    # Feche o cursor e a conexão
    cursor.close()
    connection.close()
```

Ambas as abordagens são válidas, e você pode escolher a que melhor se adapte ao seu cenário específico. A chave é garantir que os valores correspondam aos campos na tabela na ordem correta e usar placeholders (%s) para evitar a injeção de SQL. Certifique-se de lidar com exceções e realizar operações de forma segura, incluindo o uso do `commit` para confirmar as alterações no banco de dados e o fechamento adequado dos cursores e conexões para evitar vazamentos de recursos.

## Fetchall & Fetchone

No contexto do acesso a bancos de dados com bibliotecas como o `pymysql`, os métodos `cursor.execute`, `cursor.fetchall` e `cursor.fetchone` são usados para executar consultas SQL e recuperar resultados do banco de dados. Aqui está uma descrição de cada um deles:

1. **`cursor.execute(query, params=None)`**:

   O método `cursor.execute` é usado para executar uma consulta SQL no banco de dados. Ele aceita dois argumentos principais:

   - `query`: Uma string contendo a consulta SQL que você deseja executar. Você pode usar marcadores de posição (%s) na consulta para substituí-los por valores fornecidos em uma tupla ou dicionário (o argumento `params`).

   - `params` (opcional): Um valor que pode ser uma tupla ou um dicionário contendo os valores que serão substituídos nos marcadores de posição na consulta. Por exemplo, se a sua consulta contiver `%s` como marcador de posição, você pode fornecer uma tupla de valores que corresponderão aos marcadores de posição na ordem em que aparecem na consulta.

   Exemplo:

   ```python
   cursor.execute("SELECT * FROM tabela WHERE coluna1 = %s AND coluna2 = %s", (valor1, valor2))
   ```

   Após a execução bem-sucedida da consulta, você pode prosseguir para recuperar os resultados.

2. **`cursor.fetchall()`**:

   O método `cursor.fetchall` é usado para recuperar todos os resultados de uma consulta SQL que foi executada com `cursor.execute`. Ele retorna os resultados como uma lista de tuplas, onde cada tupla representa uma linha do conjunto de resultados. Se a consulta não retornar nenhum resultado, o método `fetchall` retornará uma lista vazia.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM pessoas")
   resultados = cursor.fetchall()
   for resultado in resultados:
       print(resultado[0], resultado[1])
   ```

   Neste exemplo, `resultados` conterá uma lista de tuplas, onde cada tupla contém o nome e a idade de uma pessoa da tabela.

3. **`cursor.fetchone()`**:

   O método `cursor.fetchone` é usado para recuperar apenas a próxima linha do conjunto de resultados de uma consulta. Ele retorna uma única tupla representando a próxima linha de resultados. Se não houver mais resultados, o método retornará `None`.

   Exemplo:

   ```python
   cursor.execute("SELECT nome, idade FROM pessoas")
   resultado = cursor.fetchone()
   while resultado is not None:
       print(resultado[0], resultado[1])
       resultado = cursor.fetchone()
   ```

   Neste exemplo, `fetchone` é usado para recuperar uma linha de cada vez em um loop até que não haja mais resultados.

Esses métodos são fundamentais ao trabalhar com bancos de dados em Python e são usados para executar consultas, recuperar dados do banco de dados e iterar sobre os resultados. É importante lembrar de fechar o cursor e a conexão adequadamente após a conclusão de todas as operações para evitar vazamentos de recursos.

## DELETE, WHERE e placeholders com PyMySQL

Para apagar valores de uma tabela em um banco de dados MySQL usando o `pymysql`, você pode empregar a cláusula `DELETE` juntamente com a cláusula `WHERE` para especificar as condições dos registros a serem removidos. A utilização de placeholders ajuda a prevenir a injeção de SQL ao passar parâmetros para a consulta. Aqui está um exemplo de como fazer isso:

```python
import pymysql

# Dados para a cláusula WHERE (valores a serem deletados)
valores_para_deletar = ('valor1', 'valor2')

# Estabelecer uma conexão com o banco de dados
connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

try:
    # Criar um cursor
    cursor = connection.cursor()

    # Construir a consulta DELETE com WHERE e placeholders
    table_name = 'sua_tabela'
    query = f"DELETE FROM {table_name} WHERE campo1 = %s AND campo2 = %s"

    # Executar a consulta DELETE com os valores dos placeholders
    cursor.execute(query, valores_para_deletar)

    # Fazer o commit para aplicar as alterações
    connection.commit()

except pymysql.Error as e:
    print(f"Erro ao deletar dados da tabela: {e}")

finally:
    # Fechar o cursor e a conexão
    cursor.close()
    connection.close()
```

No exemplo acima, `campo1` e `campo2` são os campos na tabela pelos quais você deseja filtrar os registros a serem deletados. `valores_para_deletar` é uma tupla contendo os valores que correspondem aos critérios da cláusula `WHERE`. Isso permite deletar registros que tenham o valor 'valor1' no `campo1` e 'valor2' no `campo2`.

Ao usar placeholders, os valores são passados separadamente da consulta SQL, o que previne a injeção de SQL, uma vez que o banco de dados trata os valores como dados, não como parte da própria consulta. Certifique-se de ajustar os campos, valores e condições conforme necessário para a sua situação específica.

## ```pymysql.cursors.DictCursor```

No `pymysql`, o `DictCursor` é uma variação do cursor que retorna os resultados das consultas como dicionários em vez de tuplas padrão. Isso significa que em vez de acessar os valores por índice, você pode acessá-los por nome de coluna, o que muitas vezes torna o código mais legível e mais fácil de entender. Aqui está como usar o `DictCursor`:

```python
import pymysql.cursors

# Estabelecer uma conexão com o banco de dados
connection = pymysql.connect(host='localhost',
                             user='seu_usuario',
                             password='sua_senha',
                             db='seu_banco_de_dados',
                             cursorclass=pymysql.cursors.DictCursor)  # Especifica o uso de DictCursor

try:
    # Criar um cursor
    with connection.cursor() as cursor:
        # Executar uma consulta usando DictCursor
        cursor.execute("SELECT * FROM sua_tabela")
        results = cursor.fetchall()

        for row in results:
            # Os resultados são retornados como dicionários
            print(row['nome_da_coluna'])

finally:
    # Fechar a conexão
    connection.close()
```

Ao usar `pymysql.cursors.DictCursor`, o objeto de cursor retornado pela conexão executará consultas SQL e retornará os resultados como dicionários. Isso permite acessar os valores recuperados pelos nomes das colunas, facilitando a compreensão do código, especialmente em consultas mais complexas ou ao lidar com grandes conjuntos de dados.

#  `SSCursor`, `SSDictCursor` e `scroll.()`

No contexto do `pymysql`, as opções `SSCursor` e `SSDictCursor` são tipos especiais de cursores que oferecem funcionalidades específicas para manipular grandes conjuntos de resultados no banco de dados.

### SSCursor

`SSCursor`, ou "Server Side Cursor", é um cursor no `pymysql` que é otimizado para recuperar grandes conjuntos de resultados sem armazenar todos os resultados na memória do cliente de uma vez. Em vez disso, ele faz uso de um cursor do lado do servidor para percorrer os resultados à medida que são necessários, minimizando a quantidade de memória usada.

Exemplo de uso:

```python
import pymysql.cursors

# Estabelecer uma conexão com o banco de dados usando SSCursor
connection = pymysql.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    db='seu_banco_de_dados',
    cursorclass=pymysql.cursors.SSCursor
)

try:
    # Criar um cursor
    with connection.cursor() as cursor:
        # Executar uma consulta usando SSCursor
        cursor.execute("SELECT * FROM sua_tabela")

        # Permite iterar sobre os resultados sem carregar todos os resultados de uma vez
        for row in cursor:
            print(row)

finally:
    # Fechar a conexão
    connection.close()
```

### SSDictCursor

`SSDictCursor`, ou "Server Side DictCursor", é uma variante do `SSCursor` que, além de usar o cursor do lado do servidor, também retorna os resultados como dicionários. Isso oferece a vantagem de acessar os valores das colunas pelo nome em vez de índices numéricos, facilitando a leitura e manipulação dos dados.

Exemplo de uso:

```python
import pymysql.cursors

# Estabelecer uma conexão com o banco de dados usando SSDictCursor
connection = pymysql.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    db='seu_banco_de_dados',
    cursorclass=pymysql.cursors.SSDictCursor
)

try:
    # Criar um cursor
    with connection.cursor() as cursor:
        # Executar uma consulta usando SSDictCursor
        cursor.execute("SELECT * FROM sua_tabela")

        # Iterar sobre os resultados retornados como dicionários
        for row in cursor:
            print(row)

finally:
    # Fechar a conexão
    connection.close()
```

### Scroll

`scroll()` é um método que pode ser utilizado com os cursores SSCursor e SSDictCursor para navegar pelos resultados. Ele permite mover o cursor para uma posição específica nos resultados. Por exemplo, você pode mover o cursor para uma posição relativa ao início dos resultados ou uma posição relativa à posição atual.

```python
import pymysql.cursors

# Estabelecer uma conexão com o banco de dados usando SSCursor
connection = pymysql.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    db='seu_banco_de_dados',
    cursorclass=pymysql.cursors.SSCursor
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sua_tabela")

        # Mover para a terceira linha (posição 2, considerando 0-index)
        cursor.scroll(2, mode='absolute')
        result = cursor.fetchone()
        print(result)

        # Mover para a segunda linha a partir da posição atual
        cursor.scroll(2, mode='relative')
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
```

`scroll()` é útil para situações em que você precisa percorrer grandes conjuntos de resultados de maneira eficiente, movendo o cursor para posições específicas ao invés de carregar todos os resultados de uma vez na memória do cliente.

## `rowcount`, `rownumber` e `lastrowid`

`rowcount`, `rownumber` e `lastrowid` são atributos ou métodos associados a conexões ou cursores em bibliotecas de acesso a banco de dados. Cada um deles fornece informações diferentes relacionadas aos resultados de consultas executadas em um banco de dados.

### `rowcount`

`rowcount` é um atributo disponível em objetos de cursor em várias bibliotecas de acesso a banco de dados, incluindo o `pymysql`. Ele retorna o número de linhas afetadas pela operação SQL mais recente executada com o cursor. Para operações de seleção (como `SELECT`), `rowcount` pode não retornar um valor preciso, ou seja, pode retornar `-1` ou `0` em muitos casos, já que não se aplica a operações de busca.

Exemplo de uso:

```python
import pymysql

connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

try:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sua_tabela WHERE id = 10")
        print(cursor.rowcount)  # Número de linhas afetadas pela operação DELETE

finally:
    connection.close()
```

### `rownumber`

O conceito de `rownumber` não está diretamente associado a bibliotecas de acesso a banco de dados como o `pymysql`. No entanto, em contextos SQL, pode ser usado para denotar uma função que atribui um número de linha sequencial a cada linha de um conjunto de resultados, mas isso é mais comum em bancos de dados como o PostgreSQL, SQL Server ou Oracle.

### `lastrowid`

`lastrowid` é um atributo específico do `pymysql`. Ele retorna o ID do último registro inserido em uma tabela com uma coluna autoincrementável (como uma chave primária autoincrementável) após uma operação de `INSERT`. Este atributo é útil quando se deseja recuperar o ID do último registro inserido.

Exemplo de uso:

```python
import pymysql

connection = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', db='seu_banco_de_dados')

try:
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO sua_tabela (nome) VALUES ('Novo registro')")
        print(cursor.lastrowid)  # ID do último registro inserido

finally:
    connection.close()
```

Estes atributos e métodos fornecem informações úteis e específicas sobre as operações realizadas em bancos de dados, permitindo obter dados como o número de linhas afetadas, o ID do último registro inserido ou, em alguns contextos, o número de linha dentro de um conjunto de resultados retornado pela consulta.
