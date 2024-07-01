# Alembic

O Alembic é uma ferramenta de migração de banco de dados para projetos Python, desenvolvida pela SQLAlchemy, um dos frameworks mais populares para trabalhar com bancos de dados em Python. Ele é usado principalmente para gerenciar alterações no esquema do banco de dados de forma sistemática e controlada.

Aqui estão os principais aspectos e características do Alembic:

### 1. **O que é Alembic?**

Alembic é uma ferramenta de migração de banco de dados para o SQLAlchemy, que permite aos desenvolvedores alterar o esquema do banco de dados ao longo do tempo, mantendo um histórico das mudanças e possibilitando a aplicação dessas mudanças de maneira organizada.

### 2. **Principais Funcionalidades**

- **Criação e Aplicação de Migrações**: Alembic permite criar e aplicar migrações que atualizam o esquema do banco de dados, como adicionar ou remover tabelas, colunas, índices e outros objetos.
- **Geração Automática de Scripts de Migração**: A partir das alterações no modelo de dados, Alembic pode gerar automaticamente scripts de migração com base nas diferenças entre o estado atual e o novo estado desejado.
- **Histórico de Migrações**: Alembic mantém um histórico das migrações aplicadas, permitindo a visualização e a aplicação de versões anteriores ou posteriores do esquema.
- **Reversão de Migrações**: É possível reverter migrações aplicadas, permitindo voltar a versões anteriores do esquema do banco de dados, se necessário.

### 3. **Estrutura Básica**

O Alembic utiliza uma estrutura básica de diretórios e arquivos para gerenciar migrações. Aqui estão os principais componentes:

- **`alembic.ini`**: Arquivo de configuração principal do Alembic.
- **`versions/`**: Diretório onde os arquivos de migração são armazenados. Cada arquivo de migração é um script Python que define as alterações a serem feitas no banco de dados.
- **`env.py`**: Script de ambiente que configura a conexão com o banco de dados e a configuração do Alembic.

### 4. **Comandos Comuns**

- **`alembic init <diretório>`**: Inicializa uma nova estrutura de diretórios para um projeto Alembic.
- **`alembic revision -m "mensagem"`**: Cria um novo arquivo de migração com uma mensagem descritiva.
- **`alembic upgrade <versão>`**: Aplica as migrações até a versão especificada (ou a versão mais recente, se nenhuma for especificada).
- **`alembic downgrade <versão>`**: Reverte as migrações para a versão especificada.
- **`alembic history`**: Exibe um histórico das migrações aplicadas.
- **`alembic current`**: Mostra a versão atual do esquema do banco de dados.

### 5. **Exemplo de Uso**

Aqui está um exemplo básico de como você pode usar o Alembic em um projeto Python:

1. **Instalação**

   Primeiro, você precisa instalar o Alembic. Isso pode ser feito usando pip:

   ```bash
   pip install alembic
   ```

2. **Inicialização**

   Em um diretório de projeto, inicialize o Alembic:

   ```bash
   alembic init alembic
   ```

   Isso criará uma estrutura de diretórios e um arquivo de configuração.

3. **Configuração**

   Edite o arquivo `alembic.ini` para configurar a URL de conexão com o banco de dados.

4. **Criação de uma Migração**

   Gere uma nova migração:

   ```bash
   alembic revision -m "Criação da tabela users"
   ```

   Isso criará um novo arquivo no diretório `versions/`.

5. **Definindo Alterações**

   Edite o arquivo de migração gerado para definir as alterações no esquema do banco de dados. Por exemplo:

   ```python
   def upgrade():
       op.create_table(
           'users',
           sa.Column('id', sa.Integer, primary_key=True),
           sa.Column('username', sa.String(50), unique=True, nullable=False),
           sa.Column('email', sa.String(100), unique=True, nullable=False)
       )

   def downgrade():
       op.drop_table('users')
   ```

6. **Aplicando Migrações**

   Aplique a migração ao banco de dados:

   ```bash
   alembic upgrade head
   ```

### 6. **Documentação e Recursos**

Para mais detalhes e recursos, você pode consultar a [documentação oficial do Alembic](https://alembic.sqlalchemy.org/en/latest/).

O Alembic é uma ferramenta poderosa para gerenciar alterações em bancos de dados em projetos Python e é bastante utilizado em aplicações web e outras soluções que requerem um banco de dados relacional.
