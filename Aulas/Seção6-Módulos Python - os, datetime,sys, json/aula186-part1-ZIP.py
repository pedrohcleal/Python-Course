# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)




criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
"""""
O código que você forneceu é um exemplo de como criar arquivos e direcioná-los para um diretório no sistema de arquivos. A função `criar_arquivos` cria arquivos de texto no diretório especificado e preenche esses arquivos com algum texto. Aqui está uma explicação passo a passo do código:

1. Importações:
   - O código começa importando os módulos necessários: `os`, `shutil`, `pathlib`, e `ZipFile`. Esses módulos são usados para trabalhar com caminhos de arquivos, gerenciamento de arquivos, compactação e descompactação.

2. Definição de Caminhos:
   - Ele define vários caminhos usando o módulo `pathlib`. Esses caminhos incluem o caminho do diretório raiz, o caminho para um diretório que será usado para armazenar arquivos temporários, o caminho para o arquivo compactado, e o caminho para o diretório onde os arquivos descompactados serão colocados.

3. Remoção de Arquivos e Diretórios Existente:
   - Antes de começar a trabalhar com os arquivos, o código remove qualquer diretório ou arquivo existente que possa entrar em conflito. Ele usa a função `shutil.rmtree` para excluir diretórios, `Path.unlink` para excluir um arquivo e `missing_ok=True` para ignorar erros se o arquivo não existir.

4. Criação do Diretório de Destino:
   - Ele cria um diretório chamado `aula_186_diretorio_zip` usando o método `mkdir` do objeto `Path` com o argumento `exist_ok=True`. Isso garante que o diretório seja criado se ainda não existir.

5. Função `criar_arquivos`:
   - A função `criar_arquivos` é definida para criar arquivos de texto no diretório especificado. Ela recebe dois argumentos: a quantidade de arquivos a serem criados (`qtd`) e o diretório de destino (`zip_dir`).
   - Dentro da função, um loop é usado para criar os arquivos de texto. Cada arquivo é aberto com `open` e preenchido com um texto único baseado no valor de `i`.

6. Chamada da Função `criar_arquivos`:
   - Finalmente, a função `criar_arquivos` é chamada com `qtd=10` e `CAMINHO_ZIP_DIR` como argumentos, o que cria 10 arquivos de texto no diretório `aula_186_diretorio_zip`.

Este código é uma preparação para criar arquivos que podem ser posteriormente compactados em um arquivo ZIP, mas não inclui a parte de compactação. Se você quiser ver o código completo para compactar esses arquivos em um arquivo ZIP, seria necessário adicionar a parte que utiliza o `ZipFile` para criar o arquivo compactado."""