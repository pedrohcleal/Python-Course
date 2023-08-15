# O básico do SQL

### Principais comandos em SQL (Structured Query Language) juntamente com detalhes sobre o que eles fazem. SQL é uma linguagem usada para gerenciar e manipular bancos de dados relacionais.

1. **SELECT**: O comando SELECT é usado para recuperar dados de uma tabela ou visualização no banco de dados. Ele permite que você especifique as colunas que deseja recuperar e as condições que devem ser atendidas para filtrar os resultados.

   Exemplo:
   ```sql
   SELECT nome, idade FROM usuarios WHERE idade > 18;
   ```

2. **INSERT**: O comando INSERT é usado para adicionar novas linhas de dados a uma tabela existente.

   Exemplo:
   ```sql
   INSERT INTO produtos (nome, preco) VALUES ('Notebook', 1000);
   ```

3. **UPDATE**: O comando UPDATE é usado para modificar os valores de uma ou mais linhas em uma tabela.

   Exemplo:
   ```sql
   UPDATE clientes SET status = 'Inativo' WHERE ultima_compra < '2023-01-01';
   ```

4. **DELETE**: O comando DELETE é usado para remover uma ou mais linhas de uma tabela.

   Exemplo:
   ```sql
   DELETE FROM pedidos WHERE status = 'Cancelado';
   ```

5. **CREATE**: O comando CREATE é usado para criar novos objetos no banco de dados, como tabelas, visões ou índices.

   Exemplo (criação de tabela):
   ```sql
   CREATE TABLE produtos (
       id INT PRIMARY KEY,
       nome VARCHAR(50),
       preco DECIMAL(10, 2)
   );
   ```

6. **ALTER**: O comando ALTER é usado para modificar a estrutura de objetos existentes no banco de dados, como adicionar colunas a uma tabela ou modificar restrições.

   Exemplo (adicionar coluna):
   ```sql
   ALTER TABLE clientes ADD COLUMN telefone VARCHAR(15);
   ```

7. **DROP**: O comando DROP é usado para excluir objetos do banco de dados, como tabelas, visões ou índices.

   Exemplo (excluir tabela):
   ```sql
   DROP TABLE produtos;
   ```

8. **JOIN**: O comando JOIN é usado para combinar dados de várias tabelas com base em uma condição especificada, criando uma visualização combinada dos dados.

   Exemplo (inner join):
   ```sql
   SELECT pedidos.id, clientes.nome
   FROM pedidos
   INNER JOIN clientes ON pedidos.cliente_id = clientes.id;
   ```

9. **GROUP BY**: O comando GROUP BY é usado para agrupar os resultados de uma consulta com base em uma ou mais colunas e aplicar funções de agregação, como SUM, COUNT, AVG, etc.

   Exemplo:
   ```sql
   SELECT departamento, AVG(salario) FROM funcionarios GROUP BY departamento;
   ```

10. **ORDER BY**: O comando ORDER BY é usado para classificar os resultados de uma consulta com base em uma ou mais colunas.

    Exemplo:
    ```sql
    SELECT nome, idade FROM usuarios ORDER BY idade DESC;
    ```

Estes são apenas alguns dos principais comandos em SQL. A linguagem oferece muitos outros recursos para consultas mais avançadas, manipulação de dados e administração de bancos de dados.
