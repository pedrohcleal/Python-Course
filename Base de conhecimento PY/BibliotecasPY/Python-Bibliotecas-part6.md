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
