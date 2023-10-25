# Bibliotecas- part7

## PyPDF 2 Lib

A biblioteca PyPDF2 é uma popular biblioteca de código aberto em Python que permite a manipulação de arquivos PDF. Com o PyPDF2, você pode realizar uma variedade de operações em arquivos PDF, como a extração de texto, a mesclagem de arquivos PDF, a divisão de PDFs em páginas individuais, a rotação de páginas e muito mais.

Aqui estão algumas das principais funcionalidades da biblioteca PyPDF2:

1. Leitura de PDFs: PyPDF2 permite abrir e ler arquivos PDF existentes. Você pode extrair texto, metadados e informações sobre as páginas do PDF.

2. Mesclagem de PDFs: PyPDF2 possibilita a combinação de vários arquivos PDF em um único documento. Isso é útil quando você precisa criar um PDF compilado a partir de várias fontes.

3. Divisão de PDFs: Você pode dividir um PDF em vários arquivos menores, seja por página ou por intervalos de páginas específicos.

4. Rotação de Páginas: PyPDF2 permite girar páginas em um documento PDF. Isso é útil quando você precisa ajustar a orientação das páginas.

5. Criptografia de PDF: A biblioteca permite adicionar ou remover senhas de proteção em documentos PDF. Isso pode ser útil para proteger o conteúdo sensível.

6. Marcação de Texto: PyPDF2 pode ser usado para destacar ou sublinhar texto em um PDF.

7. Inserção de Páginas em Branco: Você pode adicionar páginas em branco a um PDF existente.

8. Extração de Imagens: PyPDF2 suporta a extração de imagens de um PDF para salvá-las como arquivos de imagem.

É importante notar que o PyPDF2 é uma biblioteca de terceiros e não é mantida como parte da biblioteca padrão do Python. Para utilizá-lo, você precisa instalá-lo separadamente, o que pode ser feito através do gerenciador de pacotes pip. Aqui está um exemplo de como você pode usar o PyPDF2 para mesclar dois arquivos PDF:

```python
import PyPDF2

# Abre os arquivos PDF que você deseja mesclar
pdf1 = open('arquivo1.pdf', 'rb')
pdf2 = open('arquivo2.pdf', 'rb')

# Cria objetos PDF para manipulação
pdf_reader1 = PyPDF2.PdfFileReader(pdf1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf2)

# Cria um novo arquivo PDF para a saída
pdf_writer = PyPDF2.PdfFileWriter()

# Adiciona páginas dos PDFs de origem ao PDF de saída
for page_num in range(pdf_reader1.numPages):
    page = pdf_reader1.getPage(page_num)
    pdf_writer.addPage(page)

for page_num in range(pdf_reader2.numPages):
    page = pdf_reader2.getPage(page_num)
    pdf_writer.addPage(page)

# Cria o arquivo PDF mesclado
output_pdf = open('pdf_mesclado.pdf', 'wb')
pdf_writer.write(output_pdf)

# Fecha os arquivos
pdf1.close()
pdf2.close()
output_pdf.close()
```

Lembre-se de que, como o PyPDF2 é uma biblioteca de terceiros, é importante verificar a documentação atualizada e a compatibilidade com a versão do Python que você está usando, bem como considerar alternativas mais recentes, como o PyMuPDF ou pdfplumber, que podem oferecer funcionalidades adicionais e melhor desempenho.

### Métodos na lib

A biblioteca PyPDF2 oferece uma variedade de métodos para trabalhar com documentos PDF. Abaixo estão alguns dos métodos mais comuns disponíveis na biblioteca PyPDF2:

1. **`PdfFileReader()`**: Este método é usado para criar um objeto `PdfFileReader`, que permite a leitura de um arquivo PDF existente.

```python
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
```

2. **`getDocumentInfo()`**: Retorna informações gerais sobre o documento PDF, como título, autor, criador, produtor, etc.

```python
document_info = pdf_reader.getDocumentInfo()
```

3. **`getNumPages()`**: Retorna o número de páginas no documento PDF.

```python
num_pages = pdf_reader.getNumPages()
```

4. **`getPage(page_number)`**: Retorna um objeto de página específico com base no número da página.

```python
page = pdf_reader.getPage(page_number)
```

5. **`extractText()`**: Extrai o texto de uma página ou de todo o documento PDF, dependendo de como é usado.

```python
text = page.extractText()
```

6. **`PdfFileWriter()`**: Este método é usado para criar um objeto `PdfFileWriter`, que permite a criação de um novo documento PDF para escrita.

```python
pdf_writer = PyPDF2.PdfFileWriter()
```

7. **`addPage(page)`**: Adiciona uma página ao objeto `PdfFileWriter`, que pode ser usada para criar um novo documento PDF ou mesclar páginas de outros documentos.

```python
pdf_writer.addPage(page)
```

8. **`write(output_file)`**: Salva o conteúdo do objeto `PdfFileWriter` em um arquivo PDF de saída.

```python
pdf_writer.write(output_file)
```

9. **`mergePage(page)`**: Mescla o conteúdo da página especificada com a página atual no objeto `PdfFileWriter`. Isso é usado para mesclar páginas de diferentes documentos.

```python
pdf_writer.mergePage(page)
```

10. **`encrypt(user_pwd, owner_pwd)`**: Criptografa o documento PDF com senhas de usuário e proprietário.

```python
pdf_writer.encrypt(user_password, owner_password)
```

11. **`addBookmark(title, page_num, parent=None)`**: Adiciona um marcador (bookmark) a um documento PDF para facilitar a navegação.

```python
pdf_writer.addBookmark('Título do Marcador', page_number)
```

12. **`insertPage(page, page_number)`**: Insere uma página em uma posição específica no documento PDF.

```python
pdf_writer.insertPage(page, page_number)
```

Estes são apenas alguns dos métodos disponíveis na biblioteca PyPDF2. Você pode explorar mais funcionalidades e métodos na documentação oficial ou utilizando a função `help(PyPDF2)` no Python para obter uma lista completa dos métodos e classes disponíveis.

## Deque

A biblioteca `deque` em Python é parte da biblioteca padrão e fornece uma estrutura de dados chamada deque, que é uma abreviação de "double-ended queue" (fila de duas extremidades). Ela é uma coleção ordenada de elementos que suporta eficientemente a inserção e remoção de elementos tanto no início quanto no final da coleção. Isso a torna uma escolha útil quando você precisa implementar uma fila, pilha ou buffer com alta performance.

A principal característica do `deque` é a sua capacidade de operações de inserção e remoção em tempo constante (O(1)) tanto no início quanto no final da fila, o que a diferencia de uma lista comum, que tem complexidade O(n) para inserções no início. Isso faz com que os `deque` sejam especialmente úteis em situações onde a ordem dos elementos é importante e onde você precisa adicionar ou remover elementos rapidamente em ambas as extremidades.

Aqui estão alguns exemplos de operações comuns que você pode realizar com um `deque` em Python:

1. **Criação de um deque:**
   Você pode criar um `deque` vazio da seguinte maneira:
   ```python
   from collections import deque
   d = deque()
   ```

2. **Inserção de elementos:**
   Você pode inserir elementos no final do `deque` usando o método `append()` ou no início usando o método `appendleft()`.

   ```python
   d.append(1)        # Insere 1 no final
   d.appendleft(2)    # Insere 2 no início
   ```

3. **Remoção de elementos:**
   Você pode remover elementos do final do `deque` usando o método `pop()` ou do início usando o método `popleft()`.

   ```python
   x = d.pop()        # Remove e retorna o último elemento
   y = d.popleft()    # Remove e retorna o primeiro elemento
   ```

4. **Acessando elementos:**
   Você pode acessar elementos de um `deque` como se fosse uma lista.

   ```python
   primeiro_elemento = d[0]
   ```

5. **Tamanho do deque:**
   Você pode obter o tamanho do `deque` usando a função `len()`.

   ```python
   tamanho = len(d)
   ```

6. **Iteração:**
   Você pode iterar sobre os elementos de um `deque` da mesma forma que faria com uma lista.

   ```python
   for item in d:
       print(item)
   ```

Os `deque` são uma escolha poderosa quando você precisa de estruturas de dados flexíveis para manipulação de filas, pilhas ou buffers com alta eficiência. Eles são especialmente úteis em situações onde você está frequentemente adicionando ou removendo elementos nas extremidades da coleção.

