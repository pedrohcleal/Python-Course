# POO Part4

## Context Manager with Class

Em Python, um contexto (context manager) é uma abstração que permite que você defina um bloco de código que deve ser executado antes e depois de um contexto específico. Isso é particularmente útil quando você precisa configurar recursos, como abrir e fechar arquivos, conexões de banco de dados ou sockets de rede, de maneira segura e garantir que os recursos sejam liberados corretamente, mesmo em caso de exceções.

Existem duas maneiras principais de implementar um contexto manager em Python: usando classes ou usando a sintaxe `with`. Vou explicar ambas:

**Usando uma classe:**

A maneira mais comum de criar um contexto manager é criando uma classe que implementa dois métodos especiais: `__enter__` e `__exit__`.

- O método `__enter__` é chamado quando o bloco `with` é iniciado e é usado para configurar o contexto e retornar um valor opcional que será associado à variável após o `as` no bloco `with`.
- O método `__exit__` é chamado quando o bloco `with` é concluído, seja normalmente ou devido a uma exceção. Ele é responsável por liberar os recursos e manipular exceções, se necessário.

Aqui está um exemplo de um contexto manager simples que lida com a abertura e o fechamento de arquivos:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Usando o contexto manager para abrir um arquivo
with FileManager('arquivo.txt', 'w') as file:
    file.write('Olá, contexto manager!')
# O arquivo é automaticamente fechado quando saímos do bloco "with"
```

**Usando a sintaxe `with` diretamente:**

Além de criar uma classe para um contexto manager, você também pode usar a função `contextlib.contextmanager` para criar um contexto manager de forma mais concisa usando geradores. Isso é útil quando você deseja criar um contexto manager mais simples.

Aqui está um exemplo usando a função `contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Usando o contexto manager para abrir um arquivo
with file_manager('arquivo.txt', 'w') as file:
    file.write('Olá, contexto manager!')
# O arquivo é automaticamente fechado quando saímos do bloco "with"
```

Ambos os exemplos acima ilustram como criar e usar context managers em Python para gerenciar recursos e garantir que eles sejam liberados adequadamente, o que é uma prática recomendada para escrever código mais seguro e eficiente.
