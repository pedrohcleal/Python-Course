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
