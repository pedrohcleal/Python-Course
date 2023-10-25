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

## Biblioteca openpyxl

O `openpyxl` é uma biblioteca de código aberto em Python que permite a leitura e gravação de arquivos no formato Excel (.xlsx). Ela é uma ferramenta muito útil para lidar com planilhas e automação de tarefas que envolvem a manipulação de dados em planilhas do Microsoft Excel. Aqui estão alguns aspectos importantes sobre o `openpyxl`:

1. **Leitura e Escrita de Planilhas**: Com o `openpyxl`, você pode abrir arquivos Excel existentes, ler seus conteúdos e até mesmo criar novos arquivos Excel do zero. Isso é útil para automatizar tarefas que envolvem a geração de relatórios, análise de dados e muito mais.

2. **Suporte ao Formato .xlsx**: O `openpyxl` é projetado especificamente para lidar com arquivos no formato .xlsx, que é o formato de arquivo Excel mais recente e amplamente utilizado. Isso significa que você pode trabalhar com arquivos Excel modernos sem problemas de compatibilidade.

3. **Manipulação de Planilhas e Células**: A biblioteca permite a criação, exclusão e edição de planilhas em um arquivo Excel. Você pode também ler e escrever dados em células individuais, definir estilos, cores de células, bordas e muito mais.

4. **Gráficos e Imagens**: O `openpyxl` suporta a inclusão de gráficos e imagens em planilhas, permitindo criar relatórios e apresentações visualmente atraentes.

5. **Fórmulas**: Você pode definir fórmulas em células, permitindo a automação de cálculos complexos e a atualização automática dos resultados conforme os dados são modificados.

6. **Estilos e Formatação**: A biblioteca oferece recursos para aplicar estilos e formatação às células, como fonte, alinhamento, cores de preenchimento, etc.

7. **Manipulação de Gráficos**: O `openpyxl` permite a manipulação de gráficos existentes em uma planilha, a criação de novos gráficos e a configuração de suas propriedades.

8. **Compatibilidade com Pandas**: O `openpyxl` é frequentemente usado em conjunto com a biblioteca Pandas para converter dados entre DataFrames do Pandas e planilhas do Excel.

9. **Documentação e Comunidade Ativa**: O `openpyxl` possui uma documentação detalhada e uma comunidade ativa de desenvolvedores, o que torna mais fácil aprender e resolver problemas relacionados a planilhas em Python.

Para começar a usar o `openpyxl`, você precisará instalá-lo (se ainda não estiver instalado) e importá-lo em seu código Python. Em seguida, você pode abrir um arquivo Excel, manipular seus dados e salvar as alterações. Aqui está um exemplo simples de como você pode abrir um arquivo Excel e ler dados de uma planilha:

```python
import openpyxl

# Abrir um arquivo Excel
workbook = openpyxl.load_workbook('exemplo.xlsx')

# Selecionar uma planilha
sheet = workbook['Planilha1']

# Ler dados de uma célula
data = sheet['A1'].value

# Imprimir o valor da célula
print(data)

# Fechar o arquivo
workbook.close()
```

O `openpyxl` é uma ferramenta poderosa para a manipulação de planilhas em Python e é amplamente utilizado em tarefas de automação de escritório e análise de dados.

### Métodos na lib

O `openpyxl` oferece uma ampla variedade de métodos para lidar com planilhas do Excel. Abaixo estão alguns dos principais métodos e funcionalidades que você pode usar com essa biblioteca:

1. **Carregando um Arquivo Excel**:
   - `openpyxl.load_workbook(nome_do_arquivo)`: Este método é usado para abrir um arquivo Excel (.xlsx) existente e carregar seu conteúdo para ser manipulado.

2. **Acessando Planilhas**:
   - `workbook.sheetnames`: Retorna uma lista com os nomes de todas as planilhas no arquivo.
   - `workbook['nome_da_planilha']`: Permite selecionar uma planilha específica para trabalhar.

3. **Manipulando Células**:
   - `sheet['A1']`: Acessa uma célula específica pela referência da coluna e linha.
   - `cell.value`: Obtém ou define o valor de uma célula.
   - `cell.row`: Retorna o número da linha da célula.
   - `cell.column`: Retorna a letra da coluna da célula.
   - `sheet.cell(row=n, column=m)`: Acessa uma célula com base nos números da linha e da coluna.

4. **Escrita de Dados**:
   - `sheet['A1'] = valor`: Permite definir um valor em uma célula específica.

5. **Leitura de Dados**:
   - `valor = sheet['A1'].value`: Obtém o valor de uma célula específica.

6. **Estilos e Formatação**:
   - `cell.font = Font(name='Arial', bold=True)`: Define o estilo de fonte de uma célula.
   - `cell.alignment = Alignment(horizontal='center', vertical='center')`: Define a formatação de alinhamento da célula.
   - `cell.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')`: Define o preenchimento de fundo da célula.
   - `cell.border = Border(left=Side(border_style='thin', color='000000'))`: Define as bordas da célula.

7. **Fórmulas**:
   - `cell.formula = 'A2 + B2'`: Permite definir uma fórmula em uma célula.
   - `cell.calculate_value()`: Calcula o valor da fórmula em uma célula.

8. **Inserção e Exclusão de Linhas e Colunas**:
   - `sheet.insert_rows(n, amount)`: Insere n linhas na planilha.
   - `sheet.delete_rows(n, amount)`: Exclui n linhas da planilha.
   - `sheet.insert_cols(n, amount)`: Insere n colunas na planilha.
   - `sheet.delete_cols(n, amount)`: Exclui n colunas da planilha.

9. **Salvando Alterações**:
   - `workbook.save(nome_do_arquivo)`: Salva as alterações feitas no arquivo Excel.

10. **Gráficos**:
    - `openpyxl.chart`: O `openpyxl` permite criar e manipular gráficos em planilhas do Excel.

Esses são apenas alguns dos principais métodos e funcionalidades fornecidos pela biblioteca `openpyxl`. A documentação oficial do `openpyxl` oferece informações detalhadas sobre esses métodos, exemplos de uso e recursos adicionais que você pode explorar para atender às suas necessidades específicas ao trabalhar com planilhas no Python.

## Lib Pillow

A biblioteca Pillow, anteriormente conhecida como PIL (Python Imaging Library), é uma biblioteca de processamento de imagens em Python. Ela fornece uma ampla gama de funcionalidades para abrir, manipular e salvar imagens em vários formatos. O Pillow é uma escolha popular para tarefas relacionadas a processamento de imagens em Python devido à sua facilidade de uso e ampla compatibilidade com diversos formatos de imagem.

Aqui estão algumas das funcionalidades e recursos mais comuns da biblioteca Pillow:

1. **Abertura e Salvamento de Imagens:** O Pillow permite abrir imagens de vários formatos, como JPEG, PNG, BMP, GIF, TIFF, e muitos outros. Além disso, você pode salvar imagens em diferentes formatos após processá-las.

2. **Manipulação de Imagens:** O Pillow oferece uma variedade de funções para modificar imagens, como redimensionar, cortar, girar, inverter e aplicar filtros. Você pode combinar várias operações para criar efeitos mais complexos.

3. **Processamento de Pixels:** O Pillow permite acessar e modificar pixels individuais em uma imagem, o que é útil para realizar operações personalizadas.

4. **Adição de Texto e Elementos Gráficos:** Você pode adicionar texto, formas e outros elementos gráficos a imagens usando o Pillow.

5. **Conversão de Cores:** A biblioteca oferece funções para converter imagens entre diferentes modos de cores, como RGB, escala de cinza, entre outros.

6. **Filtros e Efeitos:** O Pillow inclui vários filtros e efeitos, como desfoque, nitidez, sepia, entre outros, que podem ser aplicados às imagens.

7. **Suporte a Transparência:** Você pode trabalhar com imagens que têm informações de transparência, como imagens PNG com fundo transparente.

Aqui está um exemplo simples de como usar o Pillow para abrir uma imagem e redimensioná-la:

```python
from PIL import Image

# Abrir uma imagem
imagem = Image.open("exemplo.jpg")

# Redimensionar a imagem para 300x300 pixels
imagem_redimensionada = imagem.resize((300, 300))

# Salvar a imagem redimensionada
imagem_redimensionada.save("exemplo_redimensionado.jpg")
```

O Pillow é uma ferramenta versátil para processamento de imagens em Python e é amplamente utilizado em diversas aplicações, como processamento de fotos, geração de gráficos, criação de miniaturas, edição de imagens, entre outras. Certifique-se de instalar o Pillow em seu ambiente Python antes de utilizá-lo, o que pode ser feito com o comando `pip install pillow`.
