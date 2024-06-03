# FastAPI

FastAPI é um framework moderno e de alto desempenho para a construção de APIs em Python. Ele é especialmente projetado para a criação rápida de APIs web com dados baseados em JSON e é conhecido por sua facilidade de uso e velocidade. Aqui estão alguns pontos-chave sobre o FastAPI:

### Principais Características

1. **Alto Desempenho**:
   - FastAPI é um dos frameworks web mais rápidos disponíveis em Python, comparável em desempenho a frameworks como Node.js e Go. Isso se deve à sua base no ASGI (Asynchronous Server Gateway Interface) e ao uso intensivo de programação assíncrona.

2. **Validação Automática de Dados**:
   - Utiliza o Pydantic para validar os dados de entrada e saída automaticamente. Isso significa que você pode definir modelos de dados com tipagem explícita e o FastAPI garantirá que os dados recebidos na API estejam no formato correto.

3. **Documentação Automática**:
   - Uma das funcionalidades mais apreciadas do FastAPI é a geração automática de documentação interativa da API. Usando OpenAPI e JSON Schema, ele cria uma interface Swagger UI e Redoc que permite testar e visualizar facilmente as APIs.

4. **Tipagem Estática**:
   - Aproveita o suporte à tipagem estática do Python (a partir do Python 3.6), o que melhora a legibilidade do código e fornece melhores sugestões de código e detecção de erros em tempo de desenvolvimento.

5. **Facilidade de Uso**:
   - O FastAPI é fácil de aprender e usar. Ele é projetado para ser intuitivo, com uma curva de aprendizado suave para desenvolvedores que já conhecem Python.

6. **Suporte a OAuth2 e JWT**:
   - Inclui suporte embutido para autenticação e autorização, incluindo OAuth2 e JWT (JSON Web Tokens).

### Exemplo Básico de Uso

Aqui está um exemplo simples de como criar uma API usando FastAPI:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    return item
```

### Vantagens

- **Desempenho**: FastAPI é um dos frameworks mais rápidos, permitindo construir APIs de alto desempenho.
- **Simplicidade**: A simplicidade de uso e a documentação automática tornam o desenvolvimento mais rápido e eficiente.
- **Flexibilidade**: Pode ser usado para projetos pequenos e grandes, com facilidade para escalar.

### Desvantagens

- **Curva de Aprendizado**: Para desenvolvedores não familiarizados com tipagem estática ou programação assíncrona, pode haver uma curva de aprendizado.
- **Comunidade**: Embora esteja crescendo rapidamente, a comunidade ainda é menor comparada a frameworks mais antigos como Flask e Django.

Em resumo, o FastAPI é uma excelente escolha para desenvolvedores que buscam um framework moderno, rápido e eficiente para construir APIs robustas em Python.

## Casos de uso

O FastAPI é altamente versátil e pode ser utilizado em diversos casos de uso devido às suas características de alto desempenho, facilidade de uso e robustez. Aqui estão alguns exemplos de casos de uso comuns para o FastAPI:

### 1. **APIs de Microserviços**
   - **Descrição**: Microserviços são uma arquitetura de software onde um sistema é dividido em pequenos serviços independentes, cada um executando uma funcionalidade específica.
   - **Uso do FastAPI**: Devido ao seu desempenho e simplicidade, o FastAPI é ideal para criar microserviços rápidos e eficientes. Sua documentação automática facilita a integração e comunicação entre serviços.

### 2. **APIs de Aplicativos Web e Móveis**
   - **Descrição**: APIs que servem como backend para aplicativos web e móveis, fornecendo endpoints para operações como autenticação de usuários, operações CRUD (Create, Read, Update, Delete), etc.
   - **Uso do FastAPI**: A validação de dados automática e a tipagem estática garantem que os dados enviados e recebidos estejam no formato correto, reduzindo erros e acelerando o desenvolvimento.

### 3. **Aplicações em Tempo Real**
   - **Descrição**: Aplicações que requerem comunicação em tempo real, como chats, notificações em tempo real, etc.
   - **Uso do FastAPI**: Com suporte para WebSockets, o FastAPI pode gerenciar conexões em tempo real de maneira eficiente, facilitando a construção de aplicações que necessitam de comunicação bidirecional em tempo real.

### 4. **Automação e Integração de Sistemas**
   - **Descrição**: Ferramentas internas para automação de processos e integração entre diferentes sistemas corporativos.
   - **Uso do FastAPI**: A capacidade de criar APIs rapidamente e a facilidade de integração com outras ferramentas fazem do FastAPI uma escolha ideal para projetos de automação e integração.

### 5. **APIs de Machine Learning e Data Science**
   - **Descrição**: APIs que expõem modelos de machine learning e análises de dados, permitindo que outras aplicações consumam esses serviços.
   - **Uso do FastAPI**: Integra-se bem com bibliotecas de data science como TensorFlow, Scikit-learn, e PyTorch. A capacidade de manipular grandes volumes de dados de forma eficiente é crucial para esses casos.

### 6. **Plataformas de E-commerce**
   - **Descrição**: Backends que suportam plataformas de comércio eletrônico, gerenciando catálogos de produtos, carrinhos de compras, pedidos, pagamentos, etc.
   - **Uso do FastAPI**: A flexibilidade e o desempenho são críticos para aplicações de e-commerce, onde a rapidez no processamento de transações pode impactar diretamente a experiência do usuário e as vendas.

### 7. **APIs de Finanças e Bancárias**
   - **Descrição**: APIs que lidam com transações financeiras, verificação de saldos, processamento de pagamentos, etc.
   - **Uso do FastAPI**: A segurança é fundamental nessas aplicações, e o suporte do FastAPI para OAuth2 e JWT permite a implementação de mecanismos de autenticação e autorização robustos.

### 8. **Sistemas de Gerenciamento de Conteúdo (CMS)**
   - **Descrição**: Backends que gerenciam conteúdo digital para sites, blogs, etc.
   - **Uso do FastAPI**: Permite a criação de interfaces de administração e APIs para manipulação de conteúdo de forma eficiente, com suporte para operações complexas de forma rápida e segura.

### 9. **APIs para IoT (Internet das Coisas)**
   - **Descrição**: APIs que interagem com dispositivos IoT para coleta de dados, controle de dispositivos, etc.
   - **Uso do FastAPI**: O suporte a WebSockets e a capacidade de lidar com um grande número de conexões simultâneas tornam o FastAPI ideal para aplicações IoT.

### 10. **Plataformas Educacionais e LMS (Learning Management Systems)**
   - **Descrição**: Sistemas que gerenciam cursos, alunos, avaliações e outros recursos educacionais.
   - **Uso do FastAPI**: A documentação automática é útil para desenvolvedores de frontend e integradores, enquanto a validação de dados e o desempenho são cruciais para a experiência do usuário.

Em resumo, o FastAPI é uma ferramenta poderosa e versátil que pode ser utilizada em uma ampla gama de aplicações, desde pequenos serviços internos até grandes plataformas de alta demanda, sempre garantindo alto desempenho e facilidade de uso.

## Basic

FastAPI oferece diversas funções básicas que facilitam a criação, validação e documentação de APIs web de forma eficiente e intuitiva. Aqui estão algumas das principais funcionalidades:

### 1. **Criação de Roteamentos (Routes)**

#### **@app.get()**
Define um endpoint para requisições HTTP GET. Utilizado para obter dados do servidor.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

#### **@app.post()**
Define um endpoint para requisições HTTP POST. Utilizado para enviar dados ao servidor.

```python
@app.post("/items/")
def create_item(item: dict):
    return item
```

#### **@app.put()**
Define um endpoint para requisições HTTP PUT. Utilizado para atualizar dados existentes no servidor.

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}
```

#### **@app.delete()**
Define um endpoint para requisições HTTP DELETE. Utilizado para deletar dados no servidor.

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted"}
```

### 2. **Modelagem de Dados com Pydantic**

#### **Definição de Modelos**
Utiliza Pydantic para definir esquemas de dados com validação automática.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
```

#### **Validação Automática**
Os dados enviados são automaticamente validados contra o modelo definido.

```python
@app.post("/items/")
def create_item(item: Item):
    return item
```

### 3. **Parâmetros de Consulta e Caminho**

#### **Parâmetros de Caminho**
Definem variáveis que fazem parte da URL.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

#### **Parâmetros de Consulta**
Capturam parâmetros que são passados na URL após o símbolo `?`.

```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### 4. **Documentação Automática**

#### **Swagger UI**
Gera automaticamente uma interface interativa para testar a API.

- Acessível em `/docs`.

#### **Redoc**
Outra interface de documentação gerada automaticamente.

- Acessível em `/redoc`.

### 5. **Autenticação e Autorização**

#### **OAuth2 e JWT**
Suporte embutido para autenticação e autorização usando OAuth2 e JWT.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

### 6. **Tratamento de Erros**

#### **Customização de Respostas de Erro**
Permite definir respostas personalizadas para diferentes tipos de erro.

```python
from fastapi.exceptions import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### 7. **Middleware**

#### **Adicionar Middleware**
Permite adicionar funções que são executadas antes ou depois das requisições.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 8. **WebSockets**

#### **Comunicação em Tempo Real**
Suporte para comunicação bidirecional em tempo real com WebSockets.

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

### 9. **Background Tasks**

#### **Tarefas em Segundo Plano**
Permite executar tarefas de longa duração em segundo plano.

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(message)

@app.post("/send-notification/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent"}
```

### 10. **Dependencies Injection**

#### **Gerenciamento de Dependências**
Permite a injeção de dependências de maneira declarativa.

```python
from fastapi import Depends

def common_parameters(q: str = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

Essas funções básicas tornam o FastAPI uma ferramenta poderosa e flexível para o desenvolvimento de APIs web modernas e eficientes.
