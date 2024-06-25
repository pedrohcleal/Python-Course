# Pytests

O `pytest` é um framework popular para a realização de testes em código Python. Ele é amplamente utilizado devido à sua simplicidade, flexibilidade e poder. Aqui estão alguns aspectos chave do `pytest`:

### 1. **Instalação**
Para instalar o `pytest`, você pode usar o `pip`:
```sh
pip install pytest
```

### 2. **Estrutura Básica**
Os testes no `pytest` são geralmente funções que começam com a palavra `test_`. Aqui está um exemplo básico:

```python
def test_soma():
    assert soma(1, 2) == 3
```

### 3. **Recursos Principais**

#### a. **Detecção Automática de Testes**
O `pytest` detecta automaticamente todos os arquivos de teste que começam com `test_` ou terminam com `_test.py`, e todas as funções de teste dentro desses arquivos que começam com `test_`.

#### b. **Assertions**
O `pytest` usa as declarações de assert do Python para realizar os testes. Se a expressão dentro do assert for falsa, o teste falhará.

```python
def test_soma():
    assert soma(1, 2) == 3
```

#### c. **Fixtures**
Fixtures são funções que o `pytest` usa para configurar algum estado antes que os testes rodem. Elas podem ser usadas para preparar dados de teste, instanciar objetos e muito mais.

```python
import pytest

@pytest.fixture
def setup_dados():
    return {"a": 1, "b": 2}

def test_dados(setup_dados):
    assert setup_dados["a"] == 1
    assert setup_dados["b"] == 2
```

#### d. **Parametrização**
Você pode parametrizar testes usando a marcação `@pytest.mark.parametrize`, permitindo que você execute o mesmo teste com diferentes conjuntos de dados.

```python
import pytest

@pytest.mark.parametrize("a,b,resultado", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_soma(a, b, resultado):
    assert soma(a, b) == resultado
```

### 4. **Plugins**
O `pytest` possui uma vasta coleção de plugins que podem estender suas funcionalidades. Alguns exemplos incluem:
- `pytest-cov` para cobertura de código.
- `pytest-django` para testes em projetos Django.
- `pytest-xdist` para executar testes em paralelo.

### 5. **Execução de Testes**
Para rodar os testes, você simplesmente executa o comando `pytest` no terminal na raiz do seu projeto. O `pytest` procurará automaticamente por arquivos de teste e executará os testes encontrados.

```sh
pytest
```

### 6. **Relatórios**
O `pytest` gera relatórios detalhados por padrão, mas também permite a customização e a geração de relatórios em diferentes formatos, como JUnit XML, que é útil para integração com sistemas de integração contínua (CI).

### 7. **Integração com CI/CD**
O `pytest` se integra facilmente com sistemas de CI/CD como Jenkins, GitLab CI, Travis CI, entre outros, ajudando a automatizar o processo de teste e garantir a qualidade contínua do código.

### Exemplo Completo
Aqui está um exemplo mais completo que combina vários aspectos do `pytest`:

```python
# calc.py
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

# test_calc.py
import pytest
from calc import soma, subtrai

@pytest.fixture
def setup_numeros():
    return {"x": 10, "y": 5}

def test_soma(setup_numeros):
    assert soma(setup_numeros["x"], setup_numeros["y"]) == 15

def test_subtrai(setup_numeros):
    assert subtrai(setup_numeros["x"], setup_numeros["y"]) == 5

@pytest.mark.parametrize("a,b,resultado", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_soma_parametrizada(a, b, resultado):
    assert soma(a, b) == resultado
```

Em resumo, o `pytest` é uma ferramenta poderosa e fácil de usar para escrever e executar testes em Python, oferecendo uma variedade de funcionalidades que tornam o processo de teste mais eficiente e eficaz.

## FastAPI + Pytest

O `FastAPI` é um framework moderno, rápido (alta performance), para construir APIs com Python 3.7+ baseado em padrões como OpenAPI e JSON Schema. Usar `pytest` com `FastAPI` é uma combinação poderosa para garantir que sua API esteja funcionando corretamente através de testes automatizados. Aqui está uma visão geral de como usar `pytest` no contexto de um projeto `FastAPI`.

### 1. **Instalação**
Primeiro, instale o `pytest` e as bibliotecas necessárias para testar `FastAPI`:
```sh
pip install pytest pytest-asyncio httpx
```

### 2. **Configuração Básica**
Vamos criar um exemplo básico de uma aplicação `FastAPI`.

**app/main.py**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### 3. **Criando Testes**
Com `pytest`, podemos criar testes para garantir que os endpoints da nossa aplicação `FastAPI` estão funcionando como esperado. Utilizaremos a biblioteca `httpx` para realizar as solicitações HTTP de maneira assíncrona.

**tests/test_main.py**
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/42", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "foo"}
```

### 4. **Explicação dos Componentes**
- **`AsyncClient`**: Usado para fazer solicitações HTTP de maneira assíncrona.
- **`@pytest.mark.asyncio`**: Marca os testes que devem ser executados de forma assíncrona.
- **`app`**: Importa a instância da aplicação FastAPI.

### 5. **Fixtures para Configuração de Testes**
Podemos usar fixtures para configurar e limpar os recursos necessários para os testes.

**tests/conftest.py**
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
```

**tests/test_main.py** atualizado para usar a fixture:
```python
import pytest

@pytest.mark.asyncio
async def test_read_root(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_read_item(async_client):
    response = await async_client.get("/items/42", params={"q": "foo"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "foo"}
```

### 6. **Executando os Testes**
Para executar os testes, basta rodar o comando `pytest` no terminal:
```sh
pytest
```

### 7. **Testando Rotas Protegidas**
Para rotas que exigem autenticação, você pode usar fixtures para fornecer tokens ou credenciais necessárias.

**app/main.py** atualizado com rota protegida:
```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected")
async def read_protected(token: str = Depends(oauth2_scheme)):
    if token != "fake-super-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Protected data"}
```

**tests/test_main.py** com teste de rota protegida:
```python
import pytest

@pytest.mark.asyncio
async def test_read_protected(async_client):
    response = await async_client.get("/protected", headers={"Authorization": "Bearer fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"message": "Protected data"}

    response = await async_client.get("/protected", headers={"Authorization": "Bearer wrong-token"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid authentication credentials"}
```

### Conclusão
O `pytest` fornece um ambiente robusto e flexível para testar aplicações `FastAPI`, permitindo garantir que os endpoints funcionem corretamente e que as respostas estejam conforme esperado. A combinação do `FastAPI` com `pytest` e `httpx` facilita a escrita e execução de testes assíncronos, essenciais para aplicações web modernas.

## Flask + PyTest

O Flask é um microframework leve para web em Python, e `pytest` é uma ferramenta poderosa para escrever e executar testes. A combinação de Flask com `pytest` permite testar aplicações web de forma eficiente e abrangente. Abaixo, descrevo como utilizar `pytest` para testar uma aplicação Flask, cobrindo desde a configuração básica até testes mais complexos.

### 1. **Instalação**
Para começar, você precisará instalar o Flask e o `pytest`:
```sh
pip install Flask pytest pytest-flask
```

### 2. **Configuração Básica**
Vamos criar um exemplo básico de uma aplicação Flask.

**app.py**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return jsonify(item_id=item_id, name=f'Item {item_id}')
```

### 3. **Configurando o Pytest**
Para começar a testar, criaremos uma estrutura básica de diretórios de testes. Normalmente, isso inclui um diretório `tests` onde colocaremos nossos arquivos de teste.

**tests/conftest.py**
```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```

### 4. **Escrevendo Testes**
Vamos criar um arquivo de teste para testar nossos endpoints.

**tests/test_app.py**
```python
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}

def test_get_item(client):
    response = client.get('/items/42')
    assert response.status_code == 200
    assert response.get_json() == {'item_id': 42, 'name': 'Item 42'}
```

### 5. **Explicação dos Componentes**
- **`client`**: É uma fixture configurada em `conftest.py` que cria um cliente de teste para enviar solicitações à nossa aplicação Flask.
- **`response`**: Objeto retornado pelas chamadas aos endpoints da aplicação, utilizado para verificar o status e o conteúdo das respostas.

### 6. **Testando Endpoints com Métodos Diferentes**
Para testar endpoints que utilizam métodos HTTP diferentes, como POST, PUT, DELETE, podemos criar funções de teste específicas.

**app.py** atualizado com novos endpoints:
```python
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    return jsonify(item_id=data['id'], name=data['name']), 201
```

**tests/test_app.py** atualizado para incluir testes de POST:
```python
def test_create_item(client):
    response = client.post('/items', json={'id': 1, 'name': 'Item 1'})
    assert response.status_code == 201
    assert response.get_json() == {'item_id': 1, 'name': 'Item 1'}
```

### 7. **Testando Rotas Protegidas**
Se sua aplicação Flask inclui rotas que requerem autenticação, você pode adicionar testes que simulam usuários autenticados.

**app.py** atualizado com rota protegida:
```python
from flask import abort

@app.route('/protected', methods=['GET'])
def protected():
    auth = request.headers.get('Authorization')
    if auth == 'Bearer fake-token':
        return jsonify(message='This is protected')
    else:
        abort(401)
```

**tests/test_app.py** atualizado para incluir testes de rota protegida:
```python
def test_protected(client):
    response = client.get('/protected', headers={'Authorization': 'Bearer fake-token'})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'This is protected'}

    response = client.get('/protected')
    assert response.status_code == 401
```

### 8. **Executando os Testes**
Para executar os testes, basta rodar o comando `pytest` no terminal:
```sh
pytest
```

### Conclusão
Usar `pytest` no contexto de uma aplicação Flask oferece uma maneira poderosa e flexível de garantir que sua aplicação esteja funcionando corretamente. A combinação de `pytest` com fixtures e o cliente de teste do Flask facilita a escrita de testes para endpoints HTTP, inclusive aqueles que exigem autenticação ou manipulação de dados complexos. A estrutura modular dos testes permite adicionar facilmente novos testes à medida que a aplicação cresce, garantindo uma cobertura de testes abrangente e eficiente.

