# Bibliotecas Py Part2
## Módulo OS

O módulo `os` em Python é uma biblioteca padrão que fornece uma interface para interagir com funcionalidades específicas do sistema operacional. Ele permite que você acesse e manipule informações sobre o ambiente do sistema operacional, como diretórios, arquivos, processos e variáveis de ambiente. O módulo `os` é extremamente útil para escrever código que seja portátil e compatível com diferentes sistemas operacionais, uma vez que ele abstrai muitas das diferenças específicas do sistema.

Aqui estão algumas das funcionalidades mais comuns que você pode realizar com o módulo `os`:

1. **Gerenciamento de diretórios e arquivos:**
   - `os.getcwd()`: Retorna o diretório de trabalho atual.
   - `os.chdir(path)`: Altera o diretório de trabalho atual para o caminho especificado.
   - `os.listdir(path)`: Retorna uma lista de arquivos e diretórios no caminho especificado.
   - `os.mkdir(path)`: Cria um novo diretório.
   - `os.remove(path)`: Remove um arquivo.
   - `os.rmdir(path)`: Remove um diretório vazio.
   - `os.rename(src, dst)`: Renomeia um arquivo ou diretório.

2. **Operações de caminho (path operations):**
   - `os.path.join()`: Combina vários componentes de caminho em um único caminho.
   - `os.path.abspath()`: Retorna o caminho absoluto de um arquivo ou diretório.
   - `os.path.exists()`: Verifica se um caminho existe.
   - `os.path.isfile()`: Verifica se um caminho é um arquivo.
   - `os.path.isdir()`: Verifica se um caminho é um diretório.

3. **Variáveis de ambiente:**
   - `os.environ`: Um dicionário que contém as variáveis de ambiente do sistema.
   - `os.environ.get(key)`: Obtém o valor de uma variável de ambiente específica.

4. **Execução de comandos do sistema:**
   - `os.system(command)`: Executa um comando do sistema.
   - `os.popen(command)`: Abre uma conexão para a saída do comando.

5. **Manipulação de processos:**
   - `os.fork()`: Cria um novo processo (em sistemas Unix-like).
   - `os.kill(pid, signal)`: Envia um sinal a um processo (em sistemas Unix-like).

6. **Manipulação de permissões:**
   - `os.chmod(path, mode)`: Altera as permissões de um arquivo ou diretório.

O módulo `os` é uma parte essencial da linguagem Python e é amplamente utilizado em aplicativos que precisam interagir com o sistema operacional em um nível mais baixo. No entanto, vale ressaltar que, em sistemas operacionais diferentes, algumas funcionalidades do `os` podem se comportar de maneira diferente devido às diferenças nos sistemas. Portanto, ao escrever código que depende do módulo `os`, é importante considerar a portabilidade e testar em diferentes sistemas operacionais, se necessário.

### ```os.patch```

As operações de caminho, também conhecidas como operações de gerenciamento de caminhos de arquivo, são operações que permitem manipular caminhos de arquivo de forma eficaz e portátil em Python. Essas operações são frequentemente usadas para construir, manipular e verificar caminhos de arquivo e diretório de maneira que seja compatível com diferentes sistemas operacionais, como Windows, Linux e macOS. As operações de caminho são realizadas principalmente usando o módulo `os.path` da biblioteca padrão do Python.

Aqui estão algumas das operações de caminho mais comuns:

1. **`os.path.join()`**: Este método é usado para combinar vários componentes de caminho em um único caminho. Ele lida automaticamente com a formatação do caminho, adicionando barras diagonais ou barras invertidas conforme necessário, dependendo do sistema operacional. Por exemplo:

   ```python
   import os

   path = os.path.join('diretorio', 'subdiretorio', 'arquivo.txt')
   # Resultado será 'diretorio/subdiretorio/arquivo.txt' no Unix
   # ou 'diretorio\\subdiretorio\\arquivo.txt' no Windows
   ```

2. **`os.path.abspath()`**: Retorna o caminho absoluto de um arquivo ou diretório. Isso significa que ele expandirá qualquer caminho relativo para um caminho absoluto completo. Por exemplo:

   ```python
   import os

   path = os.path.abspath('arquivo.txt')
   # Resultado será '/caminho/absoluto/completo/arquivo.txt' no Unix
   # ou 'C:\\caminho\\absoluto\\completo\\arquivo.txt' no Windows
   ```

3. **`os.path.exists()`**: Verifica se um caminho existe no sistema de arquivos. Retorna `True` se o caminho existir e `False` caso contrário.

   ```python
   import os

   existe = os.path.exists('arquivo.txt')
   ```

4. **`os.path.isfile()`**: Verifica se um caminho se refere a um arquivo existente. Retorna `True` se for um arquivo e `False` se for um diretório ou se o caminho não existir.

   ```python
   import os

   é_arquivo = os.path.isfile('arquivo.txt')
   ```

5. **`os.path.isdir()`**: Verifica se um caminho se refere a um diretório existente. Retorna `True` se for um diretório e `False` se for um arquivo ou se o caminho não existir.

   ```python
   import os

   é_diretorio = os.path.isdir('diretorio')
   ```

6. **`os.path.splitext()`**: Divide um caminho em duas partes: o nome do arquivo e a extensão do arquivo. Isso é útil para extrair informações sobre o nome e a extensão de um arquivo.

   ```python
   import os

   nome, extensao = os.path.splitext('arquivo.txt')
   # nome conterá 'arquivo' e extensao conterá '.txt'
   ```

Essas operações de caminho são essenciais ao lidar com arquivos e diretórios em Python, pois garantem que seu código seja portátil e funcione corretamente em diferentes sistemas operacionais. Elas ajudam a evitar erros relacionados à formatação de caminhos de arquivo e tornam seu código mais robusto.

###  ```os.listdir()```

A função `os.listdir()` é uma função do módulo `os` na biblioteca padrão do Python que é usada para listar os arquivos e diretórios em um determinado diretório especificado. Ela retorna uma lista de strings, onde cada elemento da lista representa um item (arquivo ou diretório) no diretório fornecido. Esta função é útil quando você precisa recuperar informações sobre os itens contidos em um diretório específico em seu sistema de arquivos.

Aqui está a sintaxe básica da função `os.listdir()`:

```python
import os

lista_de_itens = os.listdir(caminho_do_diretorio)
```

Onde:
- `caminho_do_diretorio` é o caminho absoluto ou relativo do diretório que você deseja listar.

Exemplo de uso:

```python
import os

# Listando os itens (arquivos e diretórios) em um diretório
diretorio = "/caminho/para/seu/diretorio"
itens = os.listdir(diretorio)

# Exibindo os itens listados
for item in itens:
    print(item)
```

Lembre-se de que os nomes dos itens listados são apenas strings e não incluem automaticamente o caminho completo. Se você precisar do caminho completo para cada item, você pode combiná-los usando `os.path.join()`:

```python
import os

diretorio = "/caminho/para/seu/diretorio"
itens = os.listdir(diretorio)

# Exibindo os itens listados com caminho completo
for item in itens:
    caminho_completo = os.path.join(diretorio, item)
    print(caminho_completo)
```

Tenha em mente que a função `os.listdir()` não classifica os itens listados em ordem alfabética por padrão. Se você precisar de uma lista ordenada, pode usar a função `sorted()` para classificar a lista de itens retornados:

```python
import os

diretorio = "/caminho/para/seu/diretorio"
itens = os.listdir(diretorio)

# Ordenando os itens listados em ordem alfabética
itens_ordenados = sorted(itens)

# Exibindo os itens listados ordenados
for item in itens_ordenados:
    print(item)
```

Em resumo, `os.listdir()` é uma função útil para listar e acessar os itens (arquivos e diretórios) em um diretório específico no sistema de arquivos. Ela é amplamente utilizada em tarefas de manipulação de arquivos e diretórios em Python.

### `os.stat`& `os.path.getsize`

Em Python, os módulos `os` e `os.path` oferecem funcionalidades para trabalhar com informações sobre arquivos e diretórios no sistema de arquivos do seu sistema operacional. Duas funções úteis relacionadas a isso são `os.stat` e `os.path.getsize`. Vou descrever cada uma delas separadamente:

1. `os.stat`:
   - A função `os.stat` permite que você obtenha informações detalhadas sobre um arquivo ou diretório, como tamanho, permissões, data de criação e modificação, e muito mais.
   - Ela retorna um objeto `os.stat_result` que contém uma variedade de atributos, que podem ser acessados usando métodos ou atributos do objeto.
   - Aqui está um exemplo de uso básico:

     ```python
     import os

     # Obtém informações sobre um arquivo
     file_info = os.stat('exemplo.txt')

     # Acessa os atributos do objeto os.stat_result
     print(f'Tamanho do arquivo: {file_info.st_size} bytes')
     print(f'Permissões: {file_info.st_mode}')
     print(f'Data de modificação: {file_info.st_mtime}')
     ```

   - Neste exemplo, `file_info.st_size` retorna o tamanho do arquivo em bytes, `file_info.st_mode` retorna as permissões do arquivo e `file_info.st_mtime` retorna a data de modificação do arquivo em segundos desde a época (Unix timestamp).

2. `os.path.getsize`:
   - A função `os.path.getsize` é uma função mais simples que se concentra exclusivamente em obter o tamanho de um arquivo em bytes.
   - Ela recebe como argumento o caminho para um arquivo e retorna o tamanho desse arquivo em bytes.
   - Aqui está um exemplo de uso:

     ```python
     import os

     # Obtém o tamanho de um arquivo usando os.path.getsize
     file_size = os.path.getsize('exemplo.txt')

     print(f'Tamanho do arquivo: {file_size} bytes')
     ```

   - Diferentemente de `os.stat`, `os.path.getsize` retorna diretamente o tamanho do arquivo em bytes, o que é útil quando você precisa apenas dessa informação específica e não deseja lidar com todos os outros atributos retornados por `os.stat`.

Ambas as funções são úteis para trabalhar com informações de arquivo e diretório em Python, e a escolha entre elas depende das suas necessidades específicas. Se você precisar de informações detalhadas, `os.stat` é mais adequado, enquanto `os.path.getsize` é uma opção mais simples quando você só precisa do tamanho de um arquivo.

### ```SHUTIL````

O módulo `shutil` é uma biblioteca padrão do Python que oferece várias funções para lidar com operações de alto nível em arquivos e diretórios, como copiar, mover, renomear e excluir. Para utilizá-lo, você precisa importar o módulo `shutil` no seu código Python. Aqui estão alguns exemplos de como utilizar o `shutil`:

1. Copiar um arquivo:

```python
import shutil

origem = "arquivo_origem.txt"
destino = "arquivo_destino.txt"

shutil.copy(origem, destino)
```

2. Copiar um diretório inteiro:

```python
import shutil

origem = "/caminho/para/diretorio_origem"
destino = "/caminho/para/diretorio_destino"

shutil.copytree(origem, destino)
```

3. Mover um arquivo:

```python
import shutil

origem = "arquivo_origem.txt"
destino = "novo_caminho/arquivo_destino.txt"

shutil.move(origem, destino)
```

4. Renomear um arquivo ou diretório:

```python
import shutil

antigo_nome = "arquivo_antigo.txt"
novo_nome = "arquivo_novo.txt"

shutil.move(antigo_nome, novo_nome)
```

5. Excluir um arquivo ou diretório:

```python
import shutil

arquivo_para_excluir = "arquivo_para_excluir.txt"

# Para excluir um arquivo
shutil.remove(arquivo_para_excluir)

diretorio_para_excluir = "diretorio_para_excluir"

# Para excluir um diretório e todo o seu conteúdo
shutil.rmtree(diretorio_para_excluir)
```

Tenha cuidado ao usar o `shutil`, especialmente com funções de exclusão, pois elas podem apagar permanentemente arquivos e diretórios. Certifique-se de que você está usando essas funções com cuidado e fazendo cópias de segurança dos seus dados importantes, se necessário.
