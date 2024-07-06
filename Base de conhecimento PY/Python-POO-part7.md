# POO part7

## Repository

No design de software, o padrão de repositório (Repository) é uma abordagem para encapsular o acesso aos dados, promovendo uma abstração entre a lógica de negócios e a camada de persistência de dados. Ele fornece uma interface para a recuperação e armazenamento de objetos de domínio, mantendo a separação entre a lógica de negócios e a infraestrutura.

### Características Principais do Repository

1. **Abstração do Acesso a Dados:** O repositório esconde os detalhes da implementação do acesso a dados, permitindo que a lógica de negócios interaja com dados sem se preocupar com como eles são armazenados ou recuperados.
2. **Encapsulamento da Lógica de Persistência:** Repositórios gerenciam as operações de CRUD (Create, Read, Update, Delete) e outras consultas, centralizando a lógica de persistência.
3. **Interface Limpa e Coesa:** Oferece uma interface coesa para a interação com o armazenamento de dados, facilitando a manutenção e evolução do sistema.

### Padrões e Práticas de Implementação

#### 1. **Interface do Repositório**

A interface define os métodos que o repositório deve implementar, sem especificar como esses métodos são realizados. 

```python
from abc import ABC, abstractmethod
from typing import List

class UserRepository(ABC):
    
    @abstractmethod
    def add(self, user: 'User'):
        pass

    @abstractmethod
    def get(self, user_id: int) -> 'User':
        pass

    @abstractmethod
    def update(self, user: 'User'):
        pass
    
    @abstractmethod
    def delete(self, user_id: int):
        pass
    
    @abstractmethod
    def list(self) -> List['User']:
        pass
```

#### 2. **Implementação do Repositório**

A implementação concreta define como os dados são efetivamente armazenados e recuperados.

```python
class InMemoryUserRepository(UserRepository):
    
    def __init__(self):
        self.users = {}
    
    def add(self, user: 'User'):
        self.users[user.user_id] = user
    
    def get(self, user_id: int) -> 'User':
        return self.users.get(user_id)
    
    def update(self, user: 'User'):
        if user.user_id in self.users:
            self.users[user.user_id] = user
    
    def delete(self, user_id: int):
        if user_id in self.users:
            del self.users[user_id]
    
    def list(self) -> List['User']:
        return list(self.users.values())
```

#### 3. **Uso do Repositório na Lógica de Negócio**

O repositório é utilizado pelos serviços ou pela lógica de negócios para realizar operações sobre os dados.

```python
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def register_user(self, user_id: int, name: str, email: str):
        user = User(user_id=user_id, name=name, email=email)
        self.user_repository.add(user)
    
    def get_user(self, user_id: int) -> 'User':
        return self.user_repository.get(user_id)
    
    def update_user_email(self, user_id: int, new_email: str):
        user = self.user_repository.get(user_id)
        if user:
            user.email = new_email
            self.user_repository.update(user)
```

### Benefícios do Padrão Repository

1. **Separação de Preocupações:** Mantém a lógica de negócios separada da lógica de acesso a dados, promovendo um design mais limpo e modular.
2. **Facilidade de Testes:** Permite o uso de mocks e stubs para testar a lógica de negócios sem depender da persistência real de dados.
3. **Flexibilidade na Persistência:** Facilita a mudança da tecnologia de armazenamento sem impactar a lógica de negócios, pois a interface do repositório pode permanecer a mesma.
4. **Centralização da Lógica de Acesso a Dados:** Reúne todas as operações de persistência em um só lugar, simplificando a manutenção e a evolução do acesso a dados.

### Casos de Uso

- **CRUD Operations:** Para operações básicas de criação, leitura, atualização e exclusão de entidades.
- **Consultas Complexas:** Para gerenciar consultas complexas e operações que envolvem múltiplas entidades ou condições.
- **Camada de Persistência:** Para centralizar o acesso a dados, independentemente do tipo de armazenamento utilizado (banco de dados relacional, NoSQL, etc.).

### Comparação com Outros Padrões

- **Repository vs. DAO (Data Access Object):** O DAO é um padrão mais genérico que também encapsula o acesso a dados, mas o Repository é mais focado na interação com o domínio e a lógica de negócios.
- **Repository vs. Service:** O Service encapsula a lógica de negócios, enquanto o Repository se concentra no acesso a dados. Ambos podem interagir, com o Service chamando o Repository para realizar operações de dados.

### Exemplo Completo com Entidade e Repositório

```python
# Entidade
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

# Interface do Repositório
class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update(self, user: User):
        pass
    
    @abstractmethod
    def delete(self, user_id: int):
        pass
    
    @abstractmethod
    def list(self) -> List[User]:
        pass

# Implementação do Repositório
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}
    
    def add(self, user: User):
        self.users[user.user_id] = user
    
    def get(self, user_id: int) -> User:
        return self.users.get(user_id)
    
    def update(self, user: User):
        if user.user_id in self.users:
            self.users[user.user_id] = user
    
    def delete(self, user_id: int):
        if user_id in self.users:
            del self.users[user_id]
    
    def list(self) -> List[User]:
        return list(self.users.values())

# Serviço que usa o Repositório
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def register_user(self, user_id: int, name: str, email: str):
        user = User(user_id=user_id, name=name, email=email)
        self.user_repository.add(user)
    
    def get_user(self, user_id: int) -> User:
        return self.user_repository.get(user_id)
    
    def update_user_email(self, user_id: int, new_email: str):
        user = self.user_repository.get(user_id)
        if user:
            user.email = new_email
            self.user_repository.update(user)
```

### Conclusão

O padrão Repository é uma ferramenta fundamental no design de sistemas de software, proporcionando uma forma estruturada e eficiente para acessar e gerenciar dados. Ele promove a separação de preocupações, facilita o teste e a manutenção do código, e ajuda a criar um sistema mais flexível e adaptável a mudanças na tecnologia de armazenamento.

### Referências Adicionais

- [Pattern Repository - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)
- [Repository Pattern - Wikipedia](https://en.wikipedia.org/wiki/Repository_pattern)
- [Using the Repository Pattern in Python - Real Python](https://realpython.com/repository-pattern-python/)

## Factory

O padrão de design **Factory** (Fábrica) é um dos padrões de criação mais conhecidos e utilizados em desenvolvimento de software. Ele se concentra em encapsular a criação de objetos, promovendo uma maneira flexível de criar instâncias de uma classe sem especificar a classe exata do objeto que será criado.

### Características Principais do Padrão Factory

1. **Encapsulamento da Criação de Objetos:** O padrão Factory fornece uma interface para criar objetos, permitindo que subclasses ou instâncias específicas decidam a classe concreta a ser instanciada.
2. **Desacoplamento:** Permite desacoplar a criação de objetos de seu uso, facilitando a mudança dos detalhes da criação sem alterar o código que usa os objetos.
3. **Flexibilidade e Extensibilidade:** Facilita a adição de novos tipos de objetos sem modificar o código cliente que usa esses objetos.

### Tipos de Factory

Existem várias variantes do padrão Factory, cada uma com um propósito ligeiramente diferente:

1. **Factory Method (Método de Fábrica):** Define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar. É um método na classe base que deve ser implementado por subclasses para criar instâncias de objetos.
2. **Abstract Factory (Fábrica Abstrata):** Oferece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
3. **Simple Factory (Fábrica Simples):** Um padrão de criação que não faz parte do design pattern formal, mas é uma técnica para encapsular a criação de objetos em um método estático ou uma classe específica.

### Factory Method

#### Estrutura

- **Produto:** Interface ou classe abstrata que define um tipo de objeto.
- **ConcreteProduct:** Implementação concreta do produto.
- **Creator:** Classe abstrata ou base que declara o método de fábrica, mas não o implementa.
- **ConcreteCreator:** Implementação concreta do criador que define o método de fábrica para instanciar um `ConcreteProduct`.

#### Exemplo de Factory Method

```python
from abc import ABC, abstractmethod

# Produto
class Dog(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

# Produtos Concretos
class Beagle(Dog):
    def speak(self) -> str:
        return "Woof! Woof!"

class Bulldog(Dog):
    def speak(self) -> str:
        return "Woof!"

# Criador
class DogFactory(ABC):
    @abstractmethod
    def create_dog(self) -> Dog:
        pass

# Criadores Concretos
class BeagleFactory(DogFactory):
    def create_dog(self) -> Dog:
        return Beagle()

class BulldogFactory(DogFactory):
    def create_dog(self) -> Dog:
        return Bulldog()

# Cliente
def get_dog_sound(factory: DogFactory) -> str:
    dog = factory.create_dog()
    return dog.speak()

# Uso
beagle_factory = BeagleFactory()
print(get_dog_sound(beagle_factory))  # Output: Woof! Woof!

bulldog_factory = BulldogFactory()
print(get_dog_sound(bulldog_factory))  # Output: Woof!
```

### Abstract Factory

#### Estrutura

- **AbstractFactory:** Interface para criar métodos de fábrica para diferentes produtos.
- **ConcreteFactory:** Implementa os métodos de criação para diferentes produtos.
- **AbstractProduct:** Interface para produtos, pode ser um conjunto de produtos relacionados.
- **ConcreteProduct:** Implementações concretas de produtos.

#### Exemplo de Abstract Factory

```python
from abc import ABC, abstractmethod

# Produtos
class Dog(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Cat(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

# Produtos Concretos
class Beagle(Dog):
    def speak(self) -> str:
        return "Woof! Woof!"

class Bulldog(Dog):
    def speak(self) -> str:
        return "Woof!"

class Persian(Cat):
    def speak(self) -> str:
        return "Meow!"

class Siamese(Cat):
    def speak(self) -> str:
        return "Meow!"

# Fábrica Abstrata
class AnimalFactory(ABC):
    @abstractmethod
    def create_dog(self) -> Dog:
        pass
    
    @abstractmethod
    def create_cat(self) -> Cat:
        pass

# Fábricas Concretas
class ConcreteAnimalFactory1(AnimalFactory):
    def create_dog(self) -> Dog:
        return Beagle()
    
    def create_cat(self) -> Cat:
        return Persian()

class ConcreteAnimalFactory2(AnimalFactory):
    def create_dog(self) -> Dog:
        return Bulldog()
    
    def create_cat(self) -> Cat:
        return Siamese()

# Cliente
def get_animal_sounds(factory: AnimalFactory) -> str:
    dog = factory.create_dog()
    cat = factory.create_cat()
    return f"Dog says: {dog.speak()} | Cat says: {cat.speak()}"

# Uso
factory1 = ConcreteAnimalFactory1()
print(get_animal_sounds(factory1))  # Output: Dog says: Woof! Woof! | Cat says: Meow!

factory2 = ConcreteAnimalFactory2()
print(get_animal_sounds(factory2))  # Output: Dog says: Woof! | Cat says: Meow!
```

### Simple Factory

#### Estrutura

- **Factory:** Uma classe que contém um método para criar objetos sem expor a lógica de criação ao cliente.

#### Exemplo de Simple Factory

```python
class Dog:
    def __init__(self, breed: str):
        self.breed = breed

    def speak(self) -> str:
        if self.breed == "Beagle":
            return "Woof! Woof!"
        elif self.breed == "Bulldog":
            return "Woof!"
        return "Unknown breed"

class DogFactory:
    @staticmethod
    def create_dog(breed: str) -> Dog:
        return Dog(breed)

# Cliente
def get_dog_sound(breed: str) -> str:
    dog = DogFactory.create_dog(breed)
    return dog.speak()

# Uso
print(get_dog_sound("Beagle"))  # Output: Woof! Woof!
print(get_dog_sound("Bulldog")) # Output: Woof!
```

### Benefícios do Padrão Factory

1. **Desacoplamento:** Separa o código cliente da lógica de criação dos objetos, promovendo uma arquitetura mais limpa e modular.
2. **Flexibilidade:** Facilita a adição de novos tipos de objetos sem alterar o código cliente.
3. **Manutenção e Evolução:** Facilita a manutenção e a evolução da aplicação ao centralizar a lógica de criação dos objetos.
4. **Substituição de Implementações:** Permite a substituição de implementações concretas sem alterar o código que depende da interface ou da classe base.

### Casos de Uso

- **Criação de Objetos Complexos:** Quando a criação de um objeto envolve uma lógica complexa ou configuração.
- **Sistema de Plugins:** Para sistemas que devem carregar plugins ou extensões, onde novos tipos de plugins podem ser adicionados sem modificar o sistema principal.
- **Ambientes Dinâmicos:** Em situações onde o tipo exato do objeto a ser criado pode mudar durante a execução do programa.

### Comparação com Outros Padrões de Criação

- **Factory vs. Singleton:** O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global. O Factory, por outro lado, é usado para criar múltiplas instâncias de diferentes classes.
- **Factory vs. Builder:** O padrão Builder foca na criação de um objeto complexo passo a passo, enquanto o Factory fornece uma maneira de criar instâncias de uma classe sem expor a lógica de criação.

### Referências Adicionais

- [Design Patterns - Factory Method - Martin Fowler](https://martinfowler.com/eaaCatalog/factoryMethod.html)
- [Factory Pattern - Wikipedia](https://en.wikipedia.org/wiki/Factory_pattern)
- [Abstract Factory Pattern - Wikipedia](https://en.wikipedia.org/wiki/Abstract_factory_pattern)
- [Python Design Patterns - Factory Method](https://refactoring.guru/design-patterns/factory-method/python)

### Links Úteis

- [Refactoring Guru - Factory Method](https://refactoring.guru/design-patterns/factory-method)
- [Refactoring Guru - Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
- [Design Patterns Library - Factory Method](https://www.dofactory.com/net/factory-method-design-pattern)

### Conclusão

O padrão **Factory** é uma ferramenta poderosa para gerenciar a criação de objetos de maneira flexível e desacoplada. Ele ajuda a criar um sistema mais modular e adaptável a mudanças, promovendo boas práticas de design e arquitetura de software.

### Exemplos Adicionais

Para aprofundar seus conhecimentos, aqui estão alguns exemplos de diferentes variantes e implementações do padrão Factory:

- [Factory Method Pattern in Python - Tutorial](https://www.geeksforgeeks.org/factory-method-pattern-python/)
- [Abstract Factory Pattern with Python - Tutorial](https://www.geeksforgeeks.org/abstract-factory-pattern-python/)
- [Simple Factory Pattern with Python - Example](https://www.datacamp.com/community/tutorials/python-simple-factory-pattern)

Se tiver mais perguntas ou precisar de mais detalhes, fique à vontade para perguntar!

## Controller

O padrão **Controller** é uma parte fundamental do design de software em muitos frameworks de desenvolvimento, especialmente em arquiteturas de software baseadas em MVC (Model-View-Controller) e similares. Ele atua como um intermediário entre o modelo (Model) e a visão (View), gerenciando a interação entre eles e orquestrando a lógica da aplicação.

### Características Principais do Controller

1. **Intermediário:** O Controller age como um intermediário entre a camada de apresentação (View) e a lógica de negócios (Model). Ele processa a entrada do usuário, interage com o Model e decide qual View apresentar.
2. **Gerenciamento de Requisições:** Recebe e processa requisições do usuário, manipula dados através dos Models e retorna uma resposta adequada para o usuário através das Views.
3. **Orquestração da Lógica de Aplicação:** Coordena a execução das ações apropriadas com base nas requisições do usuário e nas regras de negócios.

### Componentes do Controller

1. **Ação (Action):** Métodos dentro do Controller que correspondem a requisições específicas dos usuários. Cada ação lida com uma tarefa específica, como exibir uma página ou processar um formulário.
2. **Roteamento (Routing):** Mapeia URLs ou eventos de entrada para as ações correspondentes nos Controllers. É geralmente configurado por um framework ou biblioteca.
3. **Interação com Model:** O Controller pode criar, atualizar, excluir ou recuperar dados de Model.
4. **Preparação de Dados para a View:** O Controller prepara dados e os passa para a View para que o usuário possa visualizá-los.

### Estrutura do Controller

A estrutura do Controller pode variar dependendo do framework, mas geralmente inclui a definição de rotas e ações. Aqui está um exemplo de um Controller em um framework web comum:

#### Exemplo de Controller em Flask

```python
from flask import Flask, request, render_template, redirect, url_for
from models import User, UserRepository

app = Flask(__name__)
user_repository = UserRepository()

@app.route('/users', methods=['GET'])
def list_users():
    users = user_repository.list()
    return render_template('user_list.html', users=users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_repository.get(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    user = User(name=name, email=email)
    user_repository.add(user)
    return redirect(url_for('list_users'))

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user(user_id):
    user = user_repository.get(user_id)
    return render_template('user_edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')
    user = user_repository.get(user_id)
    user.name = name
    user.email = email
    user_repository.update(user)
    return redirect(url_for('list_users'))

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user_repository.delete(user_id)
    return redirect(url_for('list_users'))

if __name__ == '__main__':
    app.run(debug=True)
```

#### Exemplo de Controller em Django

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def list_users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'user_confirm_delete.html', {'user': user})
```

### Benefícios do Padrão Controller

1. **Separação de Preocupações:** Divide a lógica de aplicação da lógica de apresentação, permitindo que cada parte do sistema tenha uma responsabilidade única e claramente definida.
2. **Organização do Código:** Melhora a organização do código ao centralizar o gerenciamento de requisições e respostas em um único componente.
3. **Facilidade de Teste:** Facilita o teste das funcionalidades da aplicação, uma vez que as ações podem ser testadas isoladamente.
4. **Escalabilidade:** Torna a aplicação mais escalável e modular, pois novas funcionalidades podem ser adicionadas ao Controller sem alterar o restante do sistema.

### Casos de Uso

- **Desenvolvimento Web:** Em frameworks web, Controllers são usados para processar requisições HTTP, interagir com o Model e renderizar Views.
- **Aplicações Desktop:** Em aplicativos de desktop, Controllers podem gerenciar a interação entre a interface do usuário e a lógica de negócios.
- **Sistemas Complexos:** Em sistemas com múltiplos componentes, Controllers podem coordenar a interação entre diferentes partes do sistema.

### Comparação com Outros Padrões de Design

- **Controller vs. Service:** Ambos podem conter lógica de aplicação, mas o Controller gerencia a interação com o usuário e a apresentação dos dados, enquanto o Service encapsula a lógica de negócios e regras de aplicação.
- **Controller vs. View:** A View é responsável por apresentar dados ao usuário, enquanto o Controller lida com a lógica e o processamento de requisições.
- **Controller vs. Presenter:** Em padrões MVP (Model-View-Presenter), o Presenter serve um papel similar ao Controller, mediando a interação entre o Model e a View.

### Exemplos de Implementações e Leitura Adicional

- [MVC Pattern in Flask](https://flask.palletsprojects.com/en/2.0.x/tutorial/views/)
- [Django MVC Pattern Explained](https://docs.djangoproject.com/en/stable/misc/design-philosophies/#the-mvc-pattern)
- [Controller Design Pattern - Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller#Controller)

### Links Úteis

- [Flask Documentation - Views](https://flask.palletsprojects.com/en/2.3.x/views/)
- [Django Documentation - Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
- [Design Patterns Library - Controller](https://www.dofactory.com/net/controller-pattern)

### Conclusão

O padrão **Controller** é um componente crucial no design de software que promove a separação de preocupações e organiza a lógica da aplicação de forma eficiente. Ele atua como um intermediário que gerencia a interação entre o Model e a View, processando requisições, aplicando regras de negócios e retornando respostas para o usuário. Usar o padrão Controller corretamente pode levar a um design mais modular, escalável e fácil de manter.

### Exemplos Adicionais

- [Flask Controller Example - Medium](https://medium.com/@pythonhero/flask-controller-pattern-6a1c3459d0b2)
- [Django Controller Example - Real Python](https://realpython.com/django-views/)
- [Controller Pattern in Python - Tutorial](https://www.geeksforgeeks.org/python-mvc-pattern/)

Se você tiver mais perguntas ou precisar de mais detalhes, não hesite em perguntar!
