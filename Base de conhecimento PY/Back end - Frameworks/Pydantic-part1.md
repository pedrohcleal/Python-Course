# Pydantic

Pydantic é uma biblioteca de validação de dados e parsing para Python que utiliza as funcionalidades de type hints introduzidas no Python 3.6+. Ele permite a definição de modelos de dados usando classes Python normais, oferecendo validação e parsing automáticos dos dados, além de suporte a recursos avançados como serialização e deserialização.

### Principais Recursos do Pydantic

1. **Validação de Dados**:
   Pydantic valida automaticamente os dados conforme as definições dos tipos de dados das variáveis. Se os dados fornecidos não corresponderem aos tipos esperados, Pydantic gera erros detalhados.

2. **Parsing de Dados**:
   Pydantic converte dados de tipos diferentes em objetos Python, conforme especificado nos modelos, facilitando a manipulação de dados recebidos de diversas fontes, como JSON ou bancos de dados.

3. **Uso de Type Hints**:
   Utiliza anotações de tipo do Python para definir a estrutura e os tipos dos dados esperados, aproveitando-se da sintaxe padrão do Python.

4. **Desempenho**:
   É projetado para ser rápido, utilizando internamente o `dataclasses` do Python e funções otimizadas para parsing e validação.

5. **Extensibilidade**:
   Permite a criação de validadores personalizados, métodos de configuração e integrações com outras bibliotecas.

### Exemplo Básico

Aqui está um exemplo simples de como usar o Pydantic para definir e validar um modelo de dados:

```python
from pydantic import BaseModel, ValidationError

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

# Dados válidos
usuario = Usuario(id=1, nome='João', idade=30, email='joao@example.com')
print(usuario)

# Dados inválidos
try:
    usuario_invalido = Usuario(id='um', nome='João', idade='trinta', email='joao@exemplo.com')
except ValidationError as e:
    print(e)
```

No exemplo acima:
- A classe `Usuario` herda de `BaseModel`, o que a transforma em um modelo Pydantic.
- Cada atributo da classe tem um tipo especificado (int, str).
- Ao tentar criar um objeto `Usuario` com tipos de dados inválidos, Pydantic levanta um `ValidationError`.

### Funcionalidades Avançadas

1. **Modelos Aninhados**:
   Pydantic permite aninhar modelos, o que facilita a representação de estruturas de dados complexas.

```python
class Endereco(BaseModel):
    rua: str
    cidade: str
    cep: str

class Usuario(BaseModel):
    id: int
    nome: str
    endereco: Endereco

endereco = Endereco(rua='Rua A', cidade='Cidade B', cep='12345-678')
usuario = Usuario(id=1, nome='João', endereco=endereco)
print(usuario)
```

2. **Validação Personalizada**:
   É possível definir métodos de validação personalizados para campos específicos.

```python
from pydantic import validator

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

    @validator('idade')
    def idade_minima(cls, v):
        if v < 18:
            raise ValueError('Idade deve ser maior ou igual a 18')
        return v
```

3. **Configuração Avançada**:
   Pydantic permite configurar opções de comportamento dos modelos, como permitir valores extra, uso de aliases, etc.

```python
class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

    class Config:
        allow_mutation = False
```

### Conclusão

Pydantic é uma ferramenta poderosa para validação e parsing de dados em Python, facilitando o trabalho com dados de entrada e aumentando a robustez das aplicações. Sua integração com type hints torna o código mais legível e mais fácil de manter.

## Casos de uso

Pydantic é uma biblioteca versátil que pode ser utilizada em diversos cenários onde a validação, parsing e manipulação de dados são necessárias. Aqui estão alguns casos de uso comuns para Pydantic:

### 1. **APIs e Web Services**
Pydantic é amplamente utilizado em frameworks web, como FastAPI, para validar e parsear dados de entrada e saída de APIs.

- **Validação de Entradas**:
  Ao receber dados de requisições HTTP, Pydantic pode validar automaticamente os dados conforme os modelos definidos.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    return usuario
```

- **Serialização de Saídas**:
  Pode serializar objetos Python em formatos como JSON, facilitando o retorno de respostas HTTP válidas.

### 2. **Manipulação de Configurações**
Pydantic pode ser usado para definir e validar configurações de aplicações, lendo dados de arquivos de configuração (como JSON ou YAML) ou variáveis de ambiente.

```python
import os
from pydantic import BaseSettings

class Config(BaseSettings):
    app_name: str
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

config = Config()
print(config.app_name, config.debug, config.database_url)
```

### 3. **Processamento de Dados**
Para scripts e ferramentas que processam dados de diversas fontes (arquivos CSV, JSON, bancos de dados), Pydantic pode garantir que os dados sejam válidos antes de prosseguir com o processamento.

```python
import pandas as pd
from pydantic import BaseModel, ValidationError

class Produto(BaseModel):
    id: int
    nome: str
    preco: float

data = pd.read_csv('produtos.csv')
for item in data.to_dict(orient='records'):
    try:
        produto = Produto(**item)
        print(produto)
    except ValidationError as e:
        print(e)
```

### 4. **Modelos de Dados em Projetos Científicos**
Em projetos de ciência de dados e machine learning, Pydantic pode ser usado para validar os dados de entrada dos modelos, garantindo que os dados utilizados estão no formato correto.

```python
from pydantic import BaseModel, validator
import numpy as np

class DadosEntrada(BaseModel):
    features: np.ndarray
    labels: np.ndarray

    @validator('features', 'labels', pre=True, each_item=True)
    def check_dimensions(cls, v):
        if not isinstance(v, np.ndarray):
            raise ValueError('Must be a numpy array')
        return v

dados = DadosEntrada(features=np.array([[1, 2], [3, 4]]), labels=np.array([0, 1]))
```

### 5. **Integração com Bancos de Dados**
Pydantic pode ser usado junto com ORMs (Object-Relational Mappers) para validar dados antes de inseri-los no banco de dados, garantindo integridade dos dados.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

Base = declarative_base()

class UsuarioORM(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    email = Column(String, unique=True, index=True)

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Exemplo de criação e validação de um usuário
usuario_data = {'id': 1, 'nome': 'João', 'idade': 30, 'email': 'joao@example.com'}
usuario = Usuario(**usuario_data)

# Inserindo no banco de dados
usuario_orm = UsuarioORM(**usuario.dict())
db.add(usuario_orm)
db.commit()
```

### Conclusão

Pydantic é uma ferramenta poderosa para garantir a integridade dos dados em várias etapas do desenvolvimento de software, desde a validação de entradas de APIs até o processamento de grandes volumes de dados. Sua flexibilidade e integração com as funcionalidades do Python moderno fazem dela uma escolha popular para desenvolvedores que buscam robustez e facilidade na manipulação de dados.

# Basic

Pydantic oferece uma série de funções básicas que são essenciais para a validação, parsing e manipulação de dados. Aqui estão algumas das funções e características principais:

### 1. **BaseModel**

`BaseModel` é a classe fundamental de Pydantic, a partir da qual todos os modelos de dados são derivados. Ela fornece a infraestrutura para validação, parsing e serialização de dados.

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str
```

### 2. **Validação Automática**

Pydantic valida automaticamente os dados de entrada conforme os tipos definidos nos modelos. Se os dados não corresponderem aos tipos esperados, um `ValidationError` é levantado.

```python
try:
    usuario = Usuario(id='um', nome='João', idade='trinta', email='joao@example.com')
except ValidationError as e:
    print(e)
```

### 3. **Parsing e Conversão de Tipos**

Pydantic é capaz de converter tipos de dados automaticamente. Por exemplo, strings podem ser convertidas para inteiros se forem compatíveis.

```python
usuario = Usuario(id='1', nome='João', idade='30', email='joao@example.com')
print(usuario)
```

### 4. **Serialização**

Pydantic facilita a serialização de modelos para formatos como JSON, utilizando métodos como `json()` e `dict()`.

```python
usuario = Usuario(id=1, nome='João', idade=30, email='joao@example.com')
print(usuario.json())
print(usuario.dict())
```

### 5. **Validação Personalizada**

Pydantic permite a definição de validadores personalizados através do decorador `@validator`. Esses validadores podem ser usados para impor restrições adicionais aos dados.

```python
from pydantic import validator

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

    @validator('idade')
    def idade_minima(cls, v):
        if v < 18:
            raise ValueError('Idade deve ser maior ou igual a 18')
        return v
```

### 6. **Modelos Aninhados**

Pydantic permite a criação de modelos aninhados, onde um modelo pode conter outros modelos, facilitando a representação de estruturas de dados complexas.

```python
class Endereco(BaseModel):
    rua: str
    cidade: str
    cep: str

class Usuario(BaseModel):
    id: int
    nome: str
    endereco: Endereco

endereco = Endereco(rua='Rua A', cidade='Cidade B', cep='12345-678')
usuario = Usuario(id=1, nome='João', endereco=endereco)
print(usuario)
```

### 7. **Configuração de Modelos**

A classe interna `Config` permite configurar opções avançadas para os modelos, como permitir valores extra, usar aliases, imutabilidade, entre outros.

```python
class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

    class Config:
        allow_mutation = False
```

### 8. **Campos Opcionais e Valores Padrão**

Pydantic permite definir campos opcionais usando `Optional` e definir valores padrão para os campos.

```python
from typing import Optional

class Usuario(BaseModel):
    id: int
    nome: str
    idade: Optional[int] = None
    email: str = 'email@exemplo.com'
```

### 9. **Validação de Campos Complexos**

Pydantic suporta validação de campos complexos, como listas e dicionários, com verificações automáticas de tipos.

```python
from typing import List

class Usuario(BaseModel):
    id: int
    nome: str
    amigos: List[str]

usuario = Usuario(id=1, nome='João', amigos=['Maria', 'Pedro'])
print(usuario)
```

### 10. **Uso de Anotações de Tipo**

Pydantic utiliza as anotações de tipo do Python para definir e validar os dados, o que torna o código mais claro e fácil de manter.

```python
class Produto(BaseModel):
    id: int
    nome: str
    preco: float
```

### Conclusão

Pydantic oferece uma rica funcionalidade para trabalhar com dados de forma segura e eficiente, utilizando os tipos nativos do Python para garantir a integridade dos dados. Seja para validação simples ou para estruturas de dados complexas, Pydantic proporciona uma interface poderosa e fácil de usar.


