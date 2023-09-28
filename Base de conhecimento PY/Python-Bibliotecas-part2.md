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
