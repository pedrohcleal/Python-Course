# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))


    """"O código Python fornecido demonstra o uso da 
    biblioteca `string.Template` para substituir variáveis 
    em textos. Aqui está um resumo teórico da aplicação:

1. `string.Template`:
   - A biblioteca `string.Template` permite criar modelos de 
   texto com espaços reservados que podem ser preenchidos com 
   valores específicos em tempo de execução. Os espaços reservados 
   são marcados com chaves (por padrão, por exemplo, `$nome`) no
     texto do modelo.

2. Métodos de Substituição:
   - `substitute(d)`: Este método substitui os espaços reservados 
   no modelo pelos valores fornecidos no dicionário `d`. No entanto, 
   ele gera um erro se alguma das chaves do dicionário não for encontrada no modelo.
   - `safe_substitute(d)`: Este método também substitui os espaços 
   reservados no modelo pelos valores do dicionário `d`, mas não gera erros se alguma 
   chave não for encontrada no modelo. As chaves não substituídas permanecem no texto final.

3. O Exemplo Apresentado:
   - O exemplo carrega um arquivo de texto chamado `aula183.txt` e lê seu conteúdo.
   - Define um dicionário chamado `dados` que contém informações como nome, valor, data,
     empresa e telefone.
   - Cria uma subclasse personalizada chamada `MyTemplate` da classe `string.Template` 
   e define um novo delimitador de espaço reservado como `%`.
   - O conteúdo do arquivo de texto é processado pelo `MyTemplate` e as chaves do modelo 
   no arquivo de texto (marcadas com `%`) são substituídas pelos valores correspondentes no dicionário `dados`.
   - O resultado é impresso no console.

Em resumo, o código usa a biblioteca `string.Template` para criar um modelo de texto
 flexível que pode ser preenchido com valores dinâmicos a partir de um dicionário.
   Essa técnica é útil ao gerar documentos ou saídas de texto personalizadas, 
   permitindo uma fácil formatação e personalização dos dados."""