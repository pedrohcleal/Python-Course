# FastAPI - part2

Padrões de projeto são soluções reutilizáveis para problemas comuns de design de software. Em Python, especialmente com frameworks como o FastAPI, você pode aplicar diversos padrões de projeto para criar uma arquitetura robusta e manutenível. Vamos explorar alguns padrões de projeto importantes e como eles podem ser aplicados em classes com FastAPI.

### 1. **Singleton**

**Propósito:** Garantir que uma classe tenha apenas uma instância e fornecer um ponto global de acesso a ela.

**Como Aplicar com FastAPI:**
Você pode usar o padrão Singleton para garantir que uma única instância de uma classe seja compartilhada, como uma configuração de banco de dados ou um cliente HTTP.

```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            # Inicialize a conexão com o banco de dados aqui
        return cls._instance

# Exemplo de uso
db = Database()
```

### 2. **Factory Method**

**Propósito:** Definir uma interface para criar um objeto, mas permitir que subclasses decidam qual classe instanciar.

**Como Aplicar com FastAPI:**
Você pode usar o Factory Method para criar instâncias de serviços ou repositórios.

```python
class ServiceFactory:
    @staticmethod
    def get_service(service_type: str):
        if service_type == "email":
            return EmailService()
        elif service_type == "sms":
            return SMSService()
        else:
            raise ValueError("Invalid service type")

# Exemplo de uso
service = ServiceFactory.get_service("email")
```

### 3. **Decorator**

**Propósito:** Adicionar funcionalidades a um objeto dinamicamente.

**Como Aplicar com FastAPI:**
Você pode usar decoradores para adicionar funcionalidades a rotas, como autenticação ou logging.

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def auth_required(func):
    def wrapper(*args, **kwargs):
        # Verifique a autenticação aqui
        return func(*args, **kwargs)
    return wrapper

@app.get("/secure-data")
@auth_required
def get_secure_data():
    return {"data": "This is secured"}
```

### 4. **Observer**

**Propósito:** Definir uma dependência um-para-muitos entre objetos, para que quando um objeto muda de estado, todos os seus dependentes sejam notificados e atualizados automaticamente.

**Como Aplicar com FastAPI:**
Você pode usar o Observer para notificar sobre eventos ou mudanças de estado.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    def update(self, event):
        pass

# Exemplo de uso
subject = Subject()
observer = Observer()
subject.add_observer(observer)
subject.notify_observers("Event")
```

### 5. **Repository**

**Propósito:** Encapsular a lógica de acesso a dados, separando a lógica de negócios da persistência.

**Como Aplicar com FastAPI:**
Você pode usar o padrão Repository para encapsular operações com o banco de dados.

```python
class UserRepository:
    def get_user_by_id(self, user_id: int):
        # Lógica para buscar usuário no banco de dados
        pass

    def save_user(self, user):
        # Lógica para salvar usuário no banco de dados
        pass

# Exemplo de uso
user_repo = UserRepository()
user_repo.save_user(user)
```

### 6. **Strategy**

**Propósito:** Definir uma família de algoritmos, encapsular cada um e torná-los intercambiáveis.

**Como Aplicar com FastAPI:**
Você pode usar o padrão Strategy para escolher diferentes algoritmos ou estratégias.

```python
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        # Lógica para pagamento com cartão de crédito
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        # Lógica para pagamento com PayPal
        pass

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)
```

### 7. **Command**

**Propósito:** Encapsular uma solicitação como um objeto, permitindo que você parametrize clientes com diferentes requisições.

**Como Aplicar com FastAPI:**
Você pode usar o padrão Command para encapsular operações em um serviço.

```python
class Command:
    def execute(self):
        pass

class CreateUserCommand(Command):
    def __init__(self, user_data):
        self.user_data = user_data

    def execute(self):
        # Lógica para criar um usuário
        pass

# Exemplo de uso
command = CreateUserCommand(user_data)
command.execute()
```

### 8. **Chain of Responsibility**

**Propósito:** Passar uma solicitação ao longo de uma cadeia de objetos até que um objeto a trate.

**Como Aplicar com FastAPI:**
Você pode usar o Chain of Responsibility para criar uma cadeia de middlewares.

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if self.can_handle(request):
            # Lógica para tratar o pedido
            pass
        else:
            super().handle(request)

# Exemplo de uso
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB(handler_a)
handler_b.handle(request)
```

### 9. **Builder**

**Propósito:** Separar a construção de um objeto complexo da sua representação para que o mesmo processo de construção possa criar diferentes representações.

**Como Aplicar com FastAPI:**
Você pode usar o Builder para construir configurações complexas.

```python
class ConfigBuilder:
    def __init__(self):
        self.config = {}

    def set_database_url(self, url):
        self.config['DATABASE_URL'] = url
        return self

    def set_debug(self, debug):
        self.config['DEBUG'] = debug
        return self

    def build(self):
        return self.config

# Exemplo de uso
builder = ConfigBuilder()
config = builder.set_database_url("sqlite:///example.db").set_debug(True).build()
```

### Considerações Finais

O uso desses padrões pode ajudar a criar um código mais modular, flexível e fácil de manter. A escolha do padrão certo depende do problema específico que você está tentando resolver e da arquitetura da sua aplicação FastAPI.

Se você estiver interessado em mais detalhes sobre qualquer um desses padrões ou em outros padrões, sinta-se à vontade para perguntar!
