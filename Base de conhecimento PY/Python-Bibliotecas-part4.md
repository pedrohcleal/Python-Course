# Bibliotecas Py part 4

## SYS lib

A biblioteca `sys` em Python é um módulo padrão que fornece acesso a funcionalidades relacionadas ao sistema. Ela permite que você interaja com o ambiente em que seu programa Python está sendo executado, fornecendo informações e funcionalidades relacionadas ao sistema operacional, ao interpretador Python e ao ambiente de execução. Aqui estão algumas das principais funcionalidades da biblioteca `sys`:

1. **Acesso a argumentos de linha de comando:** O módulo `sys` permite que você acesse os argumentos passados ​​para um programa Python a partir da linha de comando. Você pode usar `sys.argv` para obter uma lista dos argumentos, onde `sys.argv[0]` é o nome do script Python em execução e os argumentos subsequentes são os argumentos fornecidos.

2. **Manipulação de caminhos de arquivo:** A biblioteca `sys` fornece funcionalidades para trabalhar com caminhos de arquivo. O `sys.path` é uma lista de diretórios onde o interpretador Python procura módulos para importar. Você pode adicionar diretórios a esta lista se desejar importar módulos de locais personalizados.

3. **Funções relacionadas à saída padrão e erro:** `sys.stdout` e `sys.stderr` são objetos que representam a saída padrão e a saída de erro, respectivamente. Você pode redirecionar essas saídas para outros locais, como arquivos, se necessário.

4. **Variáveis e configurações do interpretador:** O módulo `sys` oferece informações sobre o interpretador Python em execução. Você pode acessar informações como a versão do Python (`sys.version`), a versão do interpretador (`sys.hexversion`), e outros detalhes relacionados ao sistema.

5. **Finalização de programa:** A função `sys.exit()` é usada para encerrar o programa. Seu argumento opcional pode ser um código de status que indica o motivo do encerramento.

6. **Gestão de exceções:** A função `sys.exc_info()` retorna informações sobre a exceção atual sendo tratada, se houver. Isso pode ser útil para lidar com erros de forma programática.

7. **Interação com o interpretador Python:** O módulo `sys` também permite interagir com o interpretador Python em execução. Por exemplo, você pode usar `sys.stdin` e `sys.stdout` para interagir com a entrada e saída do interpretador, ou `sys.exec_prefix` para obter o diretório onde o interpretador Python está instalado.

A biblioteca `sys` é uma parte essencial da linguagem Python e é amplamente utilizada em várias aplicações, desde processamento de linha de comando até manipulação de caminhos de arquivo e gerenciamento de exceções. Ela fornece acesso a informações importantes sobre o ambiente de execução do seu programa e é útil em uma variedade de cenários.

### sys.argv

`sys.argv` é uma lista em Python que contém os argumentos passados para um programa Python a partir da linha de comando quando o programa é iniciado. Ela é uma parte fundamental do módulo `sys` e é comumente usada para interagir com argumentos de linha de comando.

A lista `sys.argv` é composta pelos seguintes elementos:

1. `sys.argv[0]`: O primeiro elemento da lista `sys.argv` é sempre o nome do script Python em execução. Esse valor é fornecido automaticamente pelo interpretador Python.

2. `sys.argv[1]`, `sys.argv[2]`, e assim por diante: Os elementos subsequentes na lista `sys.argv` são os argumentos que foram passados para o programa na linha de comando. Por exemplo, se você executar um script Python da seguinte maneira:

   ```bash
   python meu_script.py arg1 arg2 arg3
   ```

   Então, `sys.argv[1]` conterá a string "arg1", `sys.argv[2]` conterá "arg2" e `sys.argv[3]` conterá "arg3".

Você pode usar `sys.argv` para criar programas que sejam sensíveis aos argumentos de linha de comando. Isso é especialmente útil quando você deseja que seu programa realize ações diferentes com base nos argumentos fornecidos pelos usuários. Você pode usar bibliotecas como `argparse` para analisar e gerenciar os argumentos de forma mais sofisticada.

Aqui está um exemplo simples de como você pode usar `sys.argv` em um script Python:

```python
import sys

# Verificando se pelo menos um argumento foi passado
if len(sys.argv) > 1:
    # O primeiro argumento é o nome do script, então começamos a partir de sys.argv[1]
    for i in range(1, len(sys.argv)):
        print(f"Argumento {i}: {sys.argv[i]}")
else:
    print("Nenhum argumento foi passado.")
```

Este script verifica se foram passados argumentos na linha de comando e os imprime. Caso contrário, exibe uma mensagem informando que nenhum argumento foi passado.
