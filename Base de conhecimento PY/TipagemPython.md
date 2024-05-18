# Tipagem em Python

## Lib `typing`
A biblioteca `typing` do Python foi introduzida na versão 3.5 para fornecer suporte a anotações de tipo, permitindo que os desenvolvedores especificassem de maneira mais clara e precisa quais tipos de dados são esperados e retornados pelas funções, classes e variáveis. Isso melhora a legibilidade do código e pode ajudar ferramentas de análise estática, como mypy, a identificar possíveis erros antes mesmo da execução do código.

Aqui estão alguns dos principais componentes e recursos da biblioteca `typing`:

### 1. **Tipos Primitivos e Genéricos**
- **Any**: Um tipo especial que pode ser qualquer coisa.
- **Union**: Indica que uma variável pode ser de mais de um tipo. Por exemplo, `Union[int, str]` significa que a variável pode ser um inteiro ou uma string.
- **Optional**: Um tipo especial que é uma abreviação para `Union[SomeType, None]`. Por exemplo, `Optional[int]` é equivalente a `Union[int, None]`.

### 2. **Coleções Genéricas**
- **List[Type]**: Representa uma lista onde todos os elementos são do tipo especificado. Exemplo: `List[int]` é uma lista de inteiros.
- **Dict[KeyType, ValueType]**: Representa um dicionário com chaves e valores de tipos específicos. Exemplo: `Dict[str, int]` é um dicionário onde as chaves são strings e os valores são inteiros.
- **Tuple[Type1, Type2, ...]**: Representa uma tupla com um número fixo de elementos, cada um de um tipo específico. Exemplo: `Tuple[int, str]` é uma tupla onde o primeiro elemento é um inteiro e o segundo é uma string.

### 3. **Funções e Callables**
- **Callable[[Arg1Type, Arg2Type], ReturnType]**: Representa um objeto chamável (como funções ou métodos) com uma assinatura específica. Exemplo: `Callable[[int, str], bool]` é uma função que aceita um inteiro e uma string como argumentos e retorna um booleano.

### 4. **Tipos Parametrizáveis e Genéricos**
- **TypeVar**: Usado para definir tipos genéricos. Por exemplo, ao criar uma função que pode aceitar e retornar valores de qualquer tipo, você pode usar `TypeVar`.
  ```python
  from typing import TypeVar
  
  T = TypeVar('T')
  
  def identidade(item: T) -> T:
      return item
  ```

### 5. **Classes Abstratas Genéricas**
- **Iterable, Iterator**: Usados para anotar iteráveis e iteradores. Por exemplo, `Iterable[int]` é um objeto que pode ser iterado para produzir inteiros.
- **Sequence**: Representa uma sequência (como listas e tuplas) com tipos homogêneos. Exemplo: `Sequence[str]` é uma sequência de strings.
- **Mapping**: Representa mapeamentos (como dicionários) de tipos homogêneos para chaves e valores. Exemplo: `Mapping[str, int]`.

### 6. **Protocolos e Duck Typing**
- **Protocol**: Introduzido no Python 3.8, permite a definição de protocolos, que são semelhantes a interfaces em outras linguagens de programação. Eles permitem especificar um conjunto de métodos que uma classe deve implementar, sem a necessidade de herança explícita.
  ```python
  from typing import Protocol
  
  class ExemploProtocolo(Protocol):
      def metodo(self) -> str:
          ...
  
  class Implementacao:
      def metodo(self) -> str:
          return "Implementado"
  
  def funcao_que_aceita_protocolo(obj: ExemploProtocolo) -> None:
      print(obj.metodo())
  
  funcao_que_aceita_protocolo(Implementacao())
  ```

### Vantagens do uso da biblioteca `typing`:
1. **Legibilidade**: Facilita a compreensão do código, pois outros desenvolvedores podem ver imediatamente quais tipos de dados são esperados.
2. **Verificação Estática**: Ferramentas de análise estática podem detectar erros de tipo antes da execução do código, ajudando a prevenir bugs.
3. **Documentação**: As anotações de tipo podem servir como uma forma de documentação integrada ao código.

### Limitações e Considerações:
- **Checagem em Tempo de Execução**: O Python é dinamicamente tipado e as anotações de tipo são ignoradas em tempo de execução. Elas são usadas apenas por ferramentas de verificação estática e não impactam a execução do programa.
- **Complexidade**: Em projetos muito grandes ou complexos, o uso extensivo de anotações de tipo pode tornar o código mais difícil de manter.

A adoção de tipos em Python é uma prática que pode trazer muitos benefícios, especialmente em grandes projetos ou em sistemas críticos, ajudando a melhorar a qualidade e a confiabilidade do código.

### Aplicações:

Vamos explorar exemplos de aplicação da biblioteca `typing` no Python usando tipos primitivos, genéricos e coleções genéricas. 

### Tipos Primitivos

#### Exemplo com `int` e `str`
```python
from typing import Any

def soma(a: int, b: int) -> int:
    return a + b

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

def imprime_valor(valor: Any) -> None:
    print(valor)

# Uso das funções
print(soma(3, 4))       # 7
print(saudacao("Mundo")) # Olá, Mundo!
imprime_valor(10)       # 10
imprime_valor("Texto")  # Texto
```

### Tipos Genéricos

#### Exemplo com `TypeVar`
```python
from typing import TypeVar, List

T = TypeVar('T')

def identidade(item: T) -> T:
    return item

# Uso da função genérica
print(identidade(42))         # 42
print(identidade("Texto"))    # Texto
print(identidade([1, 2, 3]))  # [1, 2, 3]
```

### Coleções Genéricas

#### Exemplo com `List` e `Dict`
```python
from typing import List, Dict, Tuple

def total_lista(numeros: List[int]) -> int:
    return sum(numeros)

def contar_palavras(texto: List[str]) -> Dict[str, int]:
    contagem = {}
    for palavra in texto:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

def coordenadas(ponto: Tuple[float, float]) -> str:
    return f"X: {ponto[0]}, Y: {ponto[1]}"

# Uso das funções
print(total_lista([1, 2, 3, 4, 5])) # 15

texto = ["olá", "mundo", "olá", "python"]
print(contar_palavras(texto)) # {'olá': 2, 'mundo': 1, 'python': 1}

print(coordenadas((10.5, 20.3))) # X: 10.5, Y: 20.3
```

### Coleções Genéricas Avançadas

#### Exemplo com `Union` e `Optional`
```python
from typing import Union, Optional

def processa_dado(dado: Union[int, str]) -> str:
    if isinstance(dado, int):
        return f"Você forneceu o número: {dado}"
    elif isinstance(dado, str):
        return f"Você forneceu o texto: '{dado}'"

def pode_ser_none(valor: Optional[str]) -> str:
    if valor is None:
        return "Você não forneceu um valor"
    else:
        return f"Você forneceu o valor: '{valor}'"

# Uso das funções
print(processa_dado(42))           # Você forneceu o número: 42
print(processa_dado("Python"))     # Você forneceu o texto: 'Python'

print(pode_ser_none("Texto"))      # Você forneceu o valor: 'Texto'
print(pode_ser_none(None))         # Você não forneceu um valor
```

### Funções e Callables

#### Exemplo com `Callable`
```python
from typing import Callable

def executa_funcao(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

def multiplicacao(a: int, b: int) -> int:
    return a * b

# Uso da função que aceita outra função como parâmetro
print(executa_funcao(multiplicacao, 6, 7)) # 42
```

### Protocolos e Duck Typing

#### Exemplo com `Protocol`
```python
from typing import Protocol

class Mostravel(Protocol):
    def mostrar(self) -> str:
        ...

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def mostrar(self) -> str:
        return f"Pessoa: {self.nome}"

class Produto:
    def __init__(self, descricao: str):
        self.descricao = descricao
    
    def mostrar(self) -> str:
        return f"Produto: {self.descricao}"

def exibir(obj: Mostravel) -> None:
    print(obj.mostrar())

# Uso da função que aceita objetos que seguem o protocolo
pessoa = Pessoa("Alice")
produto = Produto("Caneta")

exibir(pessoa)  # Pessoa: Alice
exibir(produto) # Produto: Caneta
```

Esses exemplos demonstram como a biblioteca `typing` pode ser usada para especificar claramente os tipos de dados em funções e classes, melhorando a legibilidade e a segurança do código.

## Pydantic

A biblioteca `pydantic` é uma poderosa ferramenta em Python para validação de dados e gerenciamento de tipos. Ela facilita a criação de modelos de dados que são validados automaticamente, garantindo que os dados de entrada sejam corretos e estejam no formato esperado. A `pydantic` é amplamente utilizada em contextos como a definição de esquemas para APIs, configuração de aplicativos e transformação de dados.

### Principais Características

1. **Validação Automática**: `pydantic` valida os dados automaticamente ao criar instâncias de seus modelos. Se os dados não correspondem aos tipos especificados, uma exceção é lançada.

2. **Suporte a Tipos Complexos**: Além de suportar os tipos básicos do Python (como `int`, `str`, `float`), `pydantic` também suporta tipos complexos como listas, dicionários, tuples, e até mesmo tipos personalizados.

3. **Conversão Automática de Tipos**: Se possível, `pydantic` tenta converter automaticamente os dados de entrada para o tipo especificado.

4. **Facilidade de Uso com JSON**: `pydantic` trabalha muito bem com JSON, tornando-o ideal para trabalhar com dados de APIs.

5. **Integração com IDEs e Ferramentas de Análise Estática**: As anotações de tipo de `pydantic` são reconhecidas por IDEs e ferramentas como mypy, oferecendo sugestões de código e detecção de erros mais precisas.

### Exemplo Básico

#### Instalação
Para começar a usar `pydantic`, você precisa instalá-lo. Isso pode ser feito usando pip:
```bash
pip install pydantic
```

#### Definição de um Modelo
A criação de um modelo `pydantic` é simples e se assemelha à definição de classes em Python. Aqui está um exemplo básico:

```python
from pydantic import BaseModel, ValidationError

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

# Criando uma instância do modelo com dados válidos
usuario = Usuario(id=1, nome="João", idade=30, email="joao@example.com")
print(usuario)

# Tentando criar uma instância com dados inválidos
try:
    usuario_invalido = Usuario(id="um", nome="João", idade="trinta", email="joao@example.com")
except ValidationError as e:
    print(e)
```

### Recursos Avançados

#### Validação Customizada
Você pode adicionar validações personalizadas a um modelo usando decoradores:

```python
from pydantic import BaseModel, validator

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str
    
    @validator('idade')
    def idade_deve_ser_positiva(cls, v):
        if v <= 0:
            raise ValueError('A idade deve ser um valor positivo')
        return v

# Criando uma instância do modelo com uma idade válida
usuario = Usuario(id=1, nome="João", idade=30, email="joao@example.com")
print(usuario)

# Tentando criar uma instância com uma idade inválida
try:
    usuario_invalido = Usuario(id=1, nome="João", idade=-1, email="joao@example.com")
except ValidationError as e:
    print(e)
```

#### Modelos Aninhados
`pydantic` suporta modelos aninhados, permitindo a criação de estruturas de dados complexas:

```python
from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str
    cidade: str
    estado: str

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    email: str
    endereco: Endereco

endereco = Endereco(rua="Rua A", cidade="Cidade B", estado="Estado C")
usuario = Usuario(id=1, nome="João", idade=30, email="joao@example.com", endereco=endereco)
print(usuario)
```

### Integração com FastAPI

Uma das aplicações mais populares de `pydantic` é com o framework web FastAPI. `pydantic` é usado para definir os modelos de dados das requisições e respostas da API:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float
    em_estoque: bool

@app.post("/itens/")
async def criar_item(item: Item):
    return item

# Para iniciar o servidor, use o comando `uvicorn`:
# uvicorn nome_do_arquivo:app --reload
```

### Vantagens do Pydantic

1. **Facilidade de Uso**: A sintaxe de `pydantic` é intuitiva e fácil de usar, especialmente para aqueles já familiarizados com classes e dataclasses do Python.
2. **Desempenho**: `pydantic` é rápido e eficiente na validação e manipulação de dados.
3. **Flexibilidade**: Suporte a validações complexas e tipos de dados avançados torna `pydantic` uma escolha versátil para muitos casos de uso.
4. **Integração**: Boa integração com frameworks populares como FastAPI torna `pydantic` uma ferramenta essencial para o desenvolvimento de APIs modernas.

### Conclusão

`pydantic` é uma biblioteca poderosa e versátil para validação de dados e gerenciamento de tipos em Python. Ela melhora a segurança e a robustez do código, facilitando a criação de aplicações confiáveis e fáceis de manter. Seja para validação de entrada de dados, configuração de aplicativos ou definição de esquemas de API, `pydantic` é uma ferramenta valiosa para desenvolvedores Python.

## Datetime

`datetime` é um módulo fundamental da biblioteca padrão do Python que fornece classes para manipulação de datas e horários. Ele oferece uma ampla gama de funcionalidades para criar, manipular e formatar objetos de data e hora, além de calcular diferenças entre datas e realizar operações relacionadas ao tempo.

### Principais Classes do Módulo `datetime`

1. **`datetime`**: A classe principal para representar datas e horários. Ela combina os conceitos de data e hora em um único objeto.
   
   Exemplo de criação de um objeto `datetime`:
   ```python
   from datetime import datetime
   
   # Criando um objeto datetime para a data e hora atual
   agora = datetime.now()
   print(agora)  # Saída: 2024-05-18 15:30:00.123456
   ```

2. **`date`**: Utilizada para representar datas sem informações sobre o horário.

   Exemplo de criação de um objeto `date`:
   ```python
   from datetime import date
   
   # Criando um objeto date para representar o dia de hoje
   hoje = date.today()
   print(hoje)  # Saída: 2024-05-18
   ```

3. **`time`**: Utilizada para representar horários sem informações sobre a data.

   Exemplo de criação de um objeto `time`:
   ```python
   from datetime import time
   
   # Criando um objeto time para representar o horário 15:30:00
   hora = time(hour=15, minute=30, second=0)
   print(hora)  # Saída: 15:30:00
   ```

### Funcionalidades Principais

- **Operações Aritméticas**: `datetime` permite realizar operações aritméticas entre datas e horários, como adição e subtração.
  
  Exemplo:
  ```python
  from datetime import datetime, timedelta
  
  hoje = datetime.today()
  amanha = hoje + timedelta(days=1)
  print(amanha)  # Saída: Data e hora de amanhã
  ```

- **Formatação e Parsing**: É possível formatar objetos `datetime` em strings com um formato específico e também analisar strings em objetos `datetime`.

  Exemplo de formatação:
  ```python
  agora = datetime.now()
  print(agora.strftime("%Y-%m-%d %H:%M:%S"))  # Saída: 2024-05-18 15:30:00
  ```

  Exemplo de parsing:
  ```python
  data_texto = "2024-05-18"
  data = datetime.strptime(data_texto, "%Y-%m-%d")
  print(data)  # Saída: 2024-05-18 00:00:00
  ```

- **Diferenças de Tempo**: `datetime` permite calcular a diferença entre duas datas ou horários.

  Exemplo:
  ```python
  from datetime import datetime, timedelta
  
  inicio = datetime(2024, 5, 18, 10, 0, 0)
  fim = datetime(2024, 5, 18, 15, 30, 0)
  diferenca = fim - inicio
  print(diferenca)  # Saída: 5:30:00
  ```

### Utilização Avançada

Além das funcionalidades básicas mencionadas acima, o módulo `datetime` oferece uma variedade de recursos avançados, incluindo:

- Suporte a Fusos Horários com o módulo `timezone`.
- Manipulação de deltas de tempo com o módulo `timedelta`.
- Conversão entre diferentes formatos de data e hora usando o módulo `calendar`.
- Trabalho com datas julianas e calouros julianos.
- E muito mais.

### Conclusão

O módulo `datetime` é uma ferramenta poderosa para lidar com manipulação de datas e horários em Python. Com suas classes e métodos, você pode facilmente criar, manipular e formatar objetos de data e hora, além de realizar uma variedade de operações relacionadas ao tempo. Seja para desenvolver aplicações que lidam com agendamento de tarefas, geração de relatórios ou qualquer outra necessidade relacionada a datas e horários, o módulo `datetime` é uma escolha essencial para desenvolvedores Python.



