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

## Migrations

Alembic é uma ferramenta de migração de banco de dados para SQLAlchemy, o toolkit SQL para Python. Ela fornece um sistema simples e eficaz para gerenciar alterações no esquema de banco de dados. Migrações automáticas com Alembic podem simplificar bastante o processo de manter o banco de dados sincronizado com as alterações no código do aplicativo.

Aqui está uma visão geral sobre como configurar e usar migrações automáticas com Alembic:

### Configurando Alembic

1. **Instalação**:
   Primeiro, instale o Alembic usando pip:
   ```sh
   pip install alembic
   ```

2. **Inicialização**:
   Inicialize Alembic no seu projeto:
   ```sh
   alembic init alembic
   ```
   Isso criará um diretório `alembic` e um arquivo de configuração `alembic.ini`.

3. **Configuração**:
   Edite o arquivo `alembic.ini` para configurar o banco de dados. Localize a linha `sqlalchemy.url` e configure-a com a URL do seu banco de dados:
   ```ini
   sqlalchemy.url = sqlite:///your_database.db  # Exemplo para SQLite
   ```

   No diretório `alembic`, edite o arquivo `env.py` para adicionar a conexão com seu modelo SQLAlchemy:
   ```python
   from myapp import mymodel  # Importe seu modelo aqui
   target_metadata = mymodel.Base.metadata
   ```

### Criando e Aplicando Migrações

1. **Criando uma Migração**:
   Quando você fizer alterações no seu modelo SQLAlchemy, crie uma nova migração:
   ```sh
   alembic revision --autogenerate -m "Descrição da mudança"
   ```
   Isso gerará um script de migração no diretório `alembic/versions`.

2. **Revisando e Editando Migração**:
   Revise o script gerado no diretório `alembic/versions`. Alembic tentará detectar automaticamente as alterações no esquema, mas pode ser necessário ajustar o script manualmente para refletir corretamente as mudanças desejadas.

3. **Aplicando Migrações**:
   Aplique as migrações ao seu banco de dados:
   ```sh
   alembic upgrade head
   ```
   Isso aplicará todas as migrações pendentes até a última versão.

### Gerenciamento de Migrações

- **Verificar Status das Migrações**:
  Para ver quais migrações foram aplicadas e o status atual, use:
  ```sh
  alembic current
  ```

- **Reverter Migrações**:
  Se você precisar reverter uma migração, use:
  ```sh
  alembic downgrade -1
  ```
  Isso reverterá a última migração aplicada. Para reverter para uma versão específica, use:
  ```sh
  alembic downgrade <version>
  ```

### Exemplo Prático

Suponha que você tenha um modelo `User` definido em SQLAlchemy:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```

Se você adicionar um novo campo `email` ao modelo `User`:

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)  # Novo campo adicionado
```

Você criaria uma migração para refletir essa mudança:

```sh
alembic revision --autogenerate -m "Add email field to User"
alembic upgrade head
```

### Conclusão

Alembic facilita o gerenciamento de mudanças no esquema do banco de dados, permitindo que você mantenha o banco de dados em sincronia com as alterações do código de forma controlada e reprodutível. É uma ferramenta poderosa que, quando integrada ao SQLAlchemy, pode simplificar significativamente o desenvolvimento e a manutenção do banco de dados.
