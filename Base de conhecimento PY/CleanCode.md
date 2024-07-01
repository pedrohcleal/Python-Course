## PEP8

O PEP 8, que significa "Python Enhancement Proposal 8", é o guia de estilo oficial da linguagem Python. Foi criado para fornecer diretrizes de formatação e estilo de código consistentes, a fim de melhorar a legibilidade e a manutenção do código Python. O PEP 8 é amplamente aceito pela comunidade de desenvolvedores Python e é considerado uma referência padrão para escrever código Python de maneira clara e consistente.

Aqui estão alguns dos pontos-chave abordados pelo PEP 8:

1. **Indentação:** Use quatro espaços por nível de indentação, em vez de tabulações. Isso ajuda a manter a consistência em diferentes editores e ambientes.

2. **Comprimento de Linha:** Mantenha cada linha de código com até 79 caracteres. Caso uma linha precise ser quebrada, utilize parênteses, colchetes ou chaves para indicar a continuação da linha.

3. **Importações:** Importe cada módulo em uma linha separada. Coloque as importações de bibliotecas padrão antes das importações de terceiros e suas próprias importações. Evite usar `import *`.

4. **Espaços em Branco:** Use espaços em branco de forma consistente para aumentar a legibilidade. Adicione espaços após vírgulas, operadores e palavras-chave, mas evite espaços em excesso.

5. **Nomes de Variáveis e Funções:** Use nomes descritivos para variáveis, funções e classes. Prefira `snake_case` para nomes de funções e variáveis (todas as letras minúsculas com underscores para separar palavras) e `CamelCase` para nomes de classes.

6. **Comentários:** Inclua comentários para explicar partes do código que podem não ser óbvias. No entanto, evite comentários desnecessários que não agregam valor.

7. **Docstrings:** Utilize docstrings para documentar funções, métodos e classes. Isso ajuda outros desenvolvedores a entenderem o propósito e o comportamento dessas partes do código.

8. **Organização:** Organize seu código de maneira lógica e estruturada. Separe as funções e classes com linhas em branco para melhorar a legibilidade.

9. **Constantes:** Defina constantes usando letras maiúsculas e underscores.

10. **Tratamento de Exceções:** Evite capturar exceções em branco. Sempre especifique os tipos de exceção que você está tratando.

11. **Expressões Booleanas:** Use palavras-chave como `and`, `or` e `not` em vez de seus equivalentes simbólicos (`&&`, `||`, `!`).

12. **Imports Absolutos:** Use imports absolutos em vez de imports relativos para evitar ambiguidades.

O PEP 8 não é uma regra rígida, mas seguir essas diretrizes ajuda a tornar o código Python mais legível e coeso, facilitando a colaboração e a manutenção a longo prazo. Vale ressaltar que, em alguns projetos, pode ser necessário aderir a um guia de estilo específico, especialmente se você estiver trabalhando com outros desenvolvedores.

## Metodologia dos 12 fatores 

A metodologia dos 12 Fatores (The Twelve-Factor App) é um conjunto de boas práticas para o desenvolvimento de aplicativos modernos, especialmente aqueles que serão implantados na nuvem. Ela foi formulada por desenvolvedores da Heroku e visa criar aplicativos que sejam portáveis, resilientes e escaláveis. Vamos abordar cada um dos 12 fatores com exemplos práticos em Python.

### 1. **Código Base (Codebase)**
- **Manter uma única base de código**: Cada aplicativo deve ter uma única base de código rastreada em um sistema de controle de versão, como Git.
- **Múltiplos deploys**: A mesma base de código pode ser implantada em vários ambientes (desenvolvimento, produção).

Exemplo:
```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. **Dependências (Dependencies)**
- **Declarar todas as dependências explicitamente**: Utilize um gerenciador de pacotes como `pip` e um arquivo `requirements.txt` para listar todas as dependências do projeto.

Exemplo:
```bash
pip freeze > requirements.txt
```

### 3. **Configuração (Config)**
- **Armazenar configurações no ambiente**: Utilize variáveis de ambiente para gerenciar configurações que variam entre ambientes.

Exemplo:
```python
import os

DATABASE_URL = os.getenv('DATABASE_URL')
```

### 4. **Serviços de Apoio (Backing Services)**
- **Tratar serviços de apoio como recursos anexados**: Configure serviços como bancos de dados, filas e caches como recursos que podem ser facilmente substituídos.

Exemplo:
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
```

### 5. **Build, Release, Run**
- **Manter estritamente separados os estágios de build, release e run**: Utilize ferramentas de automação para gerenciar esses processos.

Exemplo:
```bash
# Build stage
docker build -t myapp .

# Release stage
docker tag myapp registry/myapp:release-1.0

# Run stage
docker run -d registry/myapp:release-1.0
```

### 6. **Processos (Processes)**
- **Executar o aplicativo como um ou mais processos sem estado**: Cada processo deve ser autônomo e não depender de nada armazenado localmente.

Exemplo:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
```

### 7. **Vinculação de Porta (Port Binding)**
- **Exportar serviços via vinculação de porta**: O aplicativo deve ser auto-suficiente e expor serviços via uma porta.

Exemplo:
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 8. **Concorrência (Concurrency)**
- **Escalar por meio do modelo de processos**: Utilize processos e threads para aumentar a concorrência.

Exemplo:
```bash
gunicorn -w 4 myapp:app
```

### 9. **Descarte (Disposability)**
- **Maximizar a robustez com inicialização e desligamento rápidos**: Desenvolva o aplicativo para iniciar e parar rapidamente.

Exemplo:
```python
@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
```

### 10. **Paridade de Desenvolvimento/Produção (Dev/Prod Parity)**
- **Manter desenvolvimento, staging e produção o mais semelhantes possível**: Utilize contêineres para garantir a paridade entre ambientes.

Exemplo:
```bash
docker-compose up
```

### 11. **Logs**
- **Tratar logs como fluxo de eventos**: Escreva logs para stdout e utilize ferramentas de agregação de logs.

Exemplo:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('This is an info log message')
```

### 12. **Processos Administrativos (Admin Processes)**
- **Executar tarefas administrativas como processos únicos**: Utilize scripts ou comandos que possam ser executados conforme necessário.

Exemplo:
```bash
python manage.py migrate
```

Adotar a metodologia dos 12 Fatores ajuda a garantir que os aplicativos sejam mais fáceis de desenvolver, implantar e escalar, proporcionando uma base sólida para a construção de software moderno.

