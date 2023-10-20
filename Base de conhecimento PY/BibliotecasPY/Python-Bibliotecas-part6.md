# Bibliotecas Py part6

## Subprocess lib

A biblioteca `subprocess` em Python é uma poderosa ferramenta que permite executar processos externos a partir de um programa Python. Isso é útil quando você deseja interagir com programas ou comandos do sistema operacional a partir do seu código Python. A biblioteca `subprocess` oferece uma variedade de métodos e classes para lidar com processos, permitindo que você inicie, controle e interaja com eles de várias maneiras.

Aqui estão algumas funcionalidades comuns da biblioteca `subprocess`:

1. **Execução de Comandos Simples**:
   Você pode usar a função `subprocess.run()` para executar comandos simples. Por exemplo:

   ```python
   import subprocess

   result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
   print(result.stdout)
   ```

   Isso executará o comando "ls -l" e capturará a saída.

2. **Pipes**:
   A biblioteca `subprocess` permite a criação de pipes (tubos) para redirecionar a entrada e a saída de processos. Você pode usar `subprocess.PIPE` para criar pipes para a entrada ou saída do processo.

3. **Controle de Processo**:
   Você pode iniciar um processo e aguardar a conclusão dele com `subprocess.run()`, ou você pode iniciar um processo em segundo plano e continuar a execução do seu programa. O módulo também oferece métodos para esperar pelo término do processo ou obter seu código de saída.

4. **Variáveis de Ambiente**:
   É possível definir variáveis de ambiente específicas para o processo que está sendo executado usando o argumento `env` em `subprocess.run()`.

5. **Comunicação Interativa**:
   Você pode abrir um processo e interagir com ele, lendo e escrevendo em seu stdin e stdout. Isso é útil para automatizar tarefas interativas, como usar um shell.

6. **Manipulação de Erros**:
   A biblioteca lida com exceções e erros associados à execução de processos, tornando mais fácil identificar problemas, como comandos não encontrados ou erros de execução.

7. **Redirecionamento de E/S**:
   É possível redirecionar a saída padrão (stdout) e a saída de erro (stderr) para arquivos ou pipes para capturar ou redirecionar essas informações.

8. **Personalização de Argumentos**:
   Você pode personalizar vários aspectos da execução do processo, como diretório de trabalho, shell a ser usado, codificação de caracteres e muito mais.

A biblioteca `subprocess` é uma maneira versátil de interagir com comandos do sistema operacional a partir do Python. No entanto, é importante usá-la com cuidado, principalmente ao executar comandos que incluem entradas do usuário ou que podem ser vulneráveis a injeção de código. Certifique-se de validar e sanitizar todas as entradas para evitar vulnerabilidades de segurança.

### Principais funções de subprocess.run()

A função `subprocess.run()` é usada para executar comandos e controlar processos externos a partir de um programa Python. Ela aceita vários argumentos que permitem personalizar a execução do processo. Abaixo estão os argumentos principais da função `subprocess.run()`:

1. **`args` (obrigatório)**: Uma lista que contém o comando a ser executado e seus argumentos. Cada elemento da lista é uma string que representa um componente do comando. Por exemplo, `["ls", "-l"]` representa o comando "ls -l".

2. **`stdin`**: Especifica a entrada padrão para o processo. Pode ser configurado para `subprocess.PIPE` (padrão), que permite interagir com a entrada padrão do processo ou para um objeto de arquivo que contém os dados de entrada.

3. **`stdout`**: Especifica a saída padrão para o processo. Pode ser configurado para `subprocess.PIPE` (padrão) para capturar a saída do processo ou para um objeto de arquivo para redirecionar a saída para um arquivo.

4. **`stderr`**: Especifica a saída de erro padrão para o processo. Pode ser configurado para `subprocess.PIPE` (padrão) para capturar a saída de erro do processo ou para um objeto de arquivo para redirecionar a saída de erro para um arquivo.

5. **`shell`**: Um valor booleano que determina se o comando deve ser executado em um shell. O valor padrão é `False`. Quando definido como `True`, você pode usar comandos shell, incluindo pipes e redirecionamentos.

6. **`cwd`**: O diretório de trabalho no qual o processo será executado. Se não for especificado, o diretório de trabalho padrão será o diretório atual do script Python.

7. **`env`**: Um dicionário que contém variáveis de ambiente que serão definidas para o processo. Se não for especificado, o processo herdará as variáveis de ambiente do processo Python pai.

8. **`text`**: Um valor booleano que determina se a saída do processo deve ser tratada como texto. Quando definido como `True`, a saída é retornada como strings. Quando definido como `False` (o padrão), a saída é retornada como bytes.

9. **`encoding`**: A codificação de caracteres a ser usada para a saída do processo, se `text` for `True`. O valor padrão é `None`, o que significa que a codificação padrão do sistema será usada.

10. **`errors`**: Especifica como lidar com erros de codificação ao decodificar a saída. O valor padrão é `'strict'`.

11. **`timeout`**: Um valor numérico que define o tempo máximo de execução do processo em segundos. Se o processo não terminar dentro desse tempo, uma exceção `TimeoutExpired` será levantada.

12. **`check`**: Um valor booleano que determina se um código de saída diferente de zero deve levantar uma exceção. Se definido como `True`, uma exceção `CalledProcessError` será levantada se o processo terminar com um código de saída diferente de zero.

Esses são os principais argumentos da função `subprocess.run()`. Eles permitem controlar diversos aspectos da execução do processo, desde a entrada e saída até o comportamento em relação a erros e exceções.

### Exemplo de aplicação

Exemplo simples de aplicação do `subprocess.run()` para executar um comando externo. Neste exemplo, usaremos o comando `ls` para listar o conteúdo de um diretório e capturaremos a saída.

```python
import subprocess

# Comando a ser executado (listar arquivos e diretórios no diretório atual)
comando = ["ls", "-l"]

# Executa o comando e captura a saída
resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)

# Verifica se a execução do comando foi bem-sucedida (código de saída zero)
if resultado.returncode == 0:
    print("Saída do comando:")
    print(resultado.stdout)
else:
    print("O comando falhou. Código de saída:", resultado.returncode)
```

Neste exemplo:

1. Definimos o comando a ser executado como uma lista de strings, onde `"ls"` é o comando e `"-l"` é um argumento para listar os arquivos e diretórios de forma detalhada.

2. Usamos `subprocess.run()` para executar o comando e capturamos a saída padrão (`stdout`) definindo `stdout=subprocess.PIPE`. Também usamos `text=True` para indicar que queremos a saída como texto.

3. Verificamos se o código de saída (`returncode`) do comando foi zero (o que indica que a execução foi bem-sucedida) e, em seguida, imprimimos a saída capturada. Caso contrário, informamos que o comando falhou e exibimos o código de saída.

Lembre-se de que este é apenas um exemplo simples. A biblioteca `subprocess` é extremamente flexível e pode ser usada para executar uma ampla variedade de comandos e realizar tarefas mais complexas, como interagir com a entrada e saída do processo, redirecionar para arquivos, definir variáveis de ambiente e muito mais.

## Threads

Em Python, as threads são usadas para realizar a programação concorrente, permitindo que você execute várias tarefas em paralelo. As threads são uma parte importante da biblioteca padrão do Python e são implementadas por meio do módulo `threading`. Aqui estão alguns conceitos e informações importantes relacionados às threads em Python:

1. **Thread**: Uma thread é uma unidade básica de execução em um programa concorrente. No Python, você pode criar threads usando a classe `Thread` do módulo `threading`.

2. **Criando Threads**: Para criar uma thread, você normalmente estende a classe `Thread` e substitui o método `run()` com o código que deseja executar na thread. Por exemplo:

```python
import threading

class MinhaThread(threading.Thread):
    def run(self):
        # Código a ser executado na thread
        pass

# Cria uma instância da thread
thread = MinhaThread()
# Inicia a thread
thread.start()
```

3. **Threads vs. Processos**: O Python também suporta processos (por meio do módulo `multiprocessing`), que são semelhantes às threads, mas têm espaço de endereço separado e são mais apropriados para tarefas intensivas em CPU. Threads são ideais para tarefas de I/O-bound, como E/S de arquivo, rede, e operações de banco de dados.

4. **GIL (Global Interpreter Lock)**: O GIL é uma característica do interpretador CPython (a implementação padrão do Python) que permite apenas uma thread por vez executar código Python. Isso pode limitar o desempenho das threads em programas multi-threading em sistemas com múltos núcleos de CPU. No entanto, o GIL não é um problema para tarefas de I/O-bound, uma vez que a maior parte do tempo de CPU é gasta aguardando E/S.

5. **Módulo threading**: O módulo `threading` fornece várias funcionalidades para trabalhar com threads, incluindo semáforos, bloqueios, condições e muito mais. Esses recursos são úteis para coordenar a execução de várias threads e evitar problemas de concorrência.

6. **Comunicação entre Threads**: As threads podem compartilhar informações através de variáveis compartilhadas, mas isso pode levar a problemas de concorrência. Para evitar isso, é importante usar mecanismos de sincronização, como semáforos, bloqueios ou filas.

7. **ThreadPool**: O módulo `concurrent.futures` oferece uma abstração de thread e pool de processos para simplificar a execução de tarefas em paralelo. Você pode usar `ThreadPoolExecutor` para criar um pool de threads e delegar tarefas a ele.

```python
from concurrent.futures import ThreadPoolExecutor

def minha_funcao(x):
    return x * 2

# Cria um pool de threads
with ThreadPoolExecutor(max_workers=4) as executor:
    # Delega tarefas para as threads no pool
    resultado = executor.submit(minha_funcao, 42)
    print(resultado.result())
```

Lembre-se de que ao trabalhar com threads, é importante lidar com questões de concorrência e garantir que seus programas sejam seguros para threads. O uso adequado de semáforos, bloqueios e outros mecanismos de sincronização é essencial para evitar problemas como condições de corrida e deadlocks.

### Métodos na lib de Threads
A biblioteca `threading` em Python fornece vários métodos e funções para criar, gerenciar e interagir com threads. Aqui estão alguns dos métodos mais comuns e importantes que você pode usar ao trabalhar com threads:

1. **`threading.Thread(target, args)`**: Este é o construtor da classe `Thread`. Ele cria uma nova instância de thread com o código a ser executado especificado no argumento `target`. O argumento `args` pode ser uma tupla de argumentos a serem passados para a função alvo.

```python
import threading

def minha_funcao(arg1, arg2):
    # Código da função
    pass

thread = threading.Thread(target=minha_funcao, args=(arg1, arg2))
```

2. **`start()`**: Este método é usado para iniciar a execução da thread. Após chamar `start()`, a thread começa a executar a função alvo.

```python
thread.start()
```

3. **`join(timeout)`**: O método `join` é usado para esperar até que a thread termine sua execução. O argumento `timeout` especifica o tempo máximo a ser aguardado. Se omitido, o programa espera indefinidamente até que a thread termine.

```python
thread.join()
```

4. **`is_alive()`**: Este método verifica se a thread está em execução. Ele retorna `True` se a thread estiver ativa e `False` caso contrário.

```python
if thread.is_alive():
    print("A thread está em execução.")
```

5. **`getName()` e `setName(name)`**: `getName()` retorna o nome da thread e `setName(name)` permite definir o nome da thread.

```python
thread.setName("MinhaThread")
print(thread.getName())
```

6. **`ident`**: Atributo que retorna um identificador único para a thread.

```python
thread_id = thread.ident
```

7. **`daemon`**: Atributo que determina se a thread é um daemon. Threads daemon não impedem o programa de sair quando o programa principal termina. Por padrão, as threads não são daemon.

```python
thread.daemon = True
```

8. **`enumerate()`**: Esta função retorna uma lista de todas as threads ativas no momento.

```python
threads_ativas = threading.enumerate()
```

9. **`current_thread()`**: Retorna a instância da thread que está sendo executada no momento.

```python
thread_atual = threading.current_thread()
```

10. **`active_count()`**: Retorna o número de threads ativas no momento.

```python
numero_de_threads_ativas = threading.active_count()
```

Estes são alguns dos métodos e funções comuns que você pode utilizar ao trabalhar com threads em Python. Lembre-se de que ao usar threads, é importante garantir a sincronização adequada para evitar problemas de concorrência e garantir a segurança das threads em seu programa.

### Locks na lib Threads

O `Lock` é um mecanismo de sincronização usado em programação concorrente para garantir que apenas uma thread por vez tenha acesso a recursos compartilhados, evitando condições de corrida e problemas de concorrência. Em Python, você pode usar o objeto `Lock` fornecido pelo módulo `threading` para implementar exclusão mútua entre threads. O `Lock` é um dos tipos mais comuns de semáforos usado para controlar o acesso a recursos compartilhados.

Aqui estão os principais métodos e conceitos relacionados ao uso de `Lock` em Python:

1. **Criando um Lock**:
   Você pode criar um objeto `Lock` simplesmente instanciando a classe `threading.Lock()`:

   ```python
   import threading

   my_lock = threading.Lock()
   ```

2. **Adquirindo e Liberando o Lock**:
   - Para adquirir o Lock e entrar na seção crítica (a parte do código que precisa de proteção), você utiliza o método `acquire()`:

     ```python
     my_lock.acquire()
     # Seção crítica
     my_lock.release()
     ```

   - Para liberar o Lock, use o método `release()`. A seção crítica deve ser protegida entre `acquire()` e `release()` para garantir que somente uma thread de cada vez acesse o recurso compartilhado.

3. **Exemplo de Uso**:
   Um exemplo comum de uso do Lock é proteger uma variável compartilhada por múltiplas threads:

   ```python
   import threading

   contador_compartilhado = 0
   lock = threading.Lock()

   def incrementa_contador():
       global contador_compartilhado
       with lock:
           contador_compartilhado += 1

   # Crie várias threads que chamam a função incrementa_contador()
   threads = [threading.Thread(target=incrementa_contador) for _ in range(5)]
   for thread in threads:
       thread.start()
   for thread in threads:
       thread.join()

   print("Contador compartilhado:", contador_compartilhado)
   ```

   O uso do Lock (`with lock`) garante que a operação de incremento seja realizada de maneira exclusiva por uma thread de cada vez.

4. **Múltiplos Locks**:
   Às vezes, você pode precisar de múltiplos Locks para proteger diferentes partes de seu programa. Certifique-se de ser consistente com os Locks usados em todo o código para evitar deadlocks.

5. **Garantir a Liberação do Lock**:
   É uma prática recomendada garantir que o Lock seja liberado (usando `release()`) em todas as situações, incluindo quando ocorrem exceções. Para isso, use a cláusula `finally` em um bloco `try-except-finally`.

   ```python
   my_lock.acquire()
   try:
       # Seção crítica
   finally:
       my_lock.release()
   ```

Os Locks são uma ferramenta poderosa para controlar o acesso a recursos compartilhados em ambientes de programação concorrente em Python. Eles ajudam a evitar condições de corrida, garantindo que apenas uma thread por vez acesse partes críticas do código. No entanto, ao usá-los, é importante ter cuidado para evitar deadlocks e garantir que os Locks sejam liberados de forma apropriada.
