# Bibliotecas no python

## if __name__ == _main__:

Em Python, o bloco de código dentro de um programa frequentemente é organizado em funções e classes para facilitar a organização e a reutilização do código. No entanto, é importante que você possa controlar quando certos blocos de código devem ser executados apenas quando o arquivo Python é executado diretamente e não quando ele é importado como um módulo em outro programa.

Para esse fim, utiliza-se a construção `if __name__ == "__main__":` em Python. Ela permite que você especifique um bloco de código que será executado apenas quando o arquivo Python é executado diretamente como um programa principal e não quando é importado como um módulo em outro programa. Isso é útil para evitar a execução de código indesejado ao importar módulos.

Aqui está um exemplo simples:

```python
def funcao1():
    print("Função 1")

def funcao2():
    print("Função 2")

if __name__ == "__main__":
    print("Este código será executado apenas se o arquivo for executado diretamente.")
    funcao1()
    funcao2()
```

Neste exemplo, se você executar este arquivo diretamente como um programa Python, verá a saída das funções `funcao1` e `funcao2`, bem como a mensagem dentro do bloco `if __name__ == "__main__":`. No entanto, se você importar este arquivo como um módulo em outro programa, o bloco `if __name__ == "__main__":` não será executado automaticamente, permitindo que você utilize as funções definidas no módulo sem que o código dentro do bloco seja executado.

Isso é particularmente útil quando você deseja criar módulos reutilizáveis em Python. O código dentro do bloco `if __name__ == "__main__":` serve como um ponto de entrada quando o arquivo é executado diretamente, mas não interfere quando o arquivo é importado como um módulo em outros programas.

## Biblioteca datetime

A biblioteca `datetime` em Python é uma biblioteca padrão poderosa e amplamente utilizada para trabalhar com datas e horários. Ela fornece classes e funções que permitem criar, manipular e formatar datas e horários de maneira flexível e eficiente. A biblioteca `datetime` faz parte do módulo `datetime` e inclui várias classes importantes, como `datetime`, `date`, `time`, `timedelta`, `tzinfo`, entre outras.

Aqui estão algumas das principais classes e funcionalidades oferecidas pela biblioteca `datetime`:

1. **`datetime.datetime`**: Esta classe representa um ponto específico no tempo, incluindo informações de data e hora. Você pode criar objetos `datetime` para representar datas e horas específicas e realizar operações aritméticas com eles.

2. **`datetime.date`**: Esta classe representa apenas a parte da data, sem informações de hora. Ela é útil para trabalhar com datas, como datas de nascimento, datas de eventos, etc.

3. **`datetime.time`**: Esta classe representa apenas a parte do horário, sem informações de data. É útil quando você precisa lidar com horários específicos, como o horário de início e término de um evento.

4. **`datetime.timedelta`**: Esta classe permite representar uma diferença entre duas datas ou horas. Você pode realizar operações de adição e subtração com objetos `timedelta` para calcular intervalos de tempo.

5. **`datetime.datetime.now()`**: Função que retorna o objeto `datetime` representando a data e hora atuais.

6. **Formatação e análise de datas e horas**: A biblioteca `datetime` oferece métodos para formatar objetos `datetime` em strings legíveis e para analisar strings de datas e horas em objetos `datetime`.

7. **Fuso horário (timezone)**: Você pode trabalhar com fusos horários usando o módulo `datetime.timezone`. Isso permite que você lide com datas e horas em diferentes fusos horários e faça conversões de fuso horário quando necessário.

8. **Operações de aritmética de datas e horas**: A biblioteca `datetime` permite realizar operações matemáticas com datas e horas, como adição, subtração e comparação.

Aqui está um exemplo simples de como usar a biblioteca `datetime` para criar um objeto `datetime` representando a data e hora atuais:

```python
import datetime

# Obter a data e hora atuais
agora = datetime.datetime.now()

print("Data e hora atuais:", agora)
```

A biblioteca `datetime` é extremamente útil para tarefas que envolvem manipulação de datas e horas em Python, como trabalhar com registros de data e hora, agendamento de tarefas, cálculo de intervalos de tempo, e muito mais. Ela oferece uma ampla gama de recursos para atender às necessidades de desenvolvedores que trabalham com datas e horas em seus projetos Python.

### Como formatar datas e horas:
A formatação de datas e horas em Python, utilizando a biblioteca `datetime`, permite que você exiba datas e horas de maneira legível para os usuários ou para armazenamento em diferentes formatos. Você pode formatar objetos `datetime`, `date` e `time` em strings seguindo padrões específicos. Isso é útil ao exibir datas e horas em interfaces de usuário, relatórios, bancos de dados e outros contextos onde a formatação é importante.

Para formatar datas e horas, você pode usar o método `strftime()` (string format time) que está disponível em objetos `datetime`, `date` e `time`. O método `strftime()` aceita um argumento de formato, que é uma string que define como a data e a hora devem ser apresentadas. Aqui estão alguns dos códigos de formatação mais comuns que você pode usar:

- `%Y`: Ano com 4 dígitos (por exemplo, 2023).
- `%y`: Ano com 2 dígitos (por exemplo, 23 para 2023).
- `%m`: Mês como número (01 a 12).
- `%d`: Dia do mês como número (01 a 31).
- `%H`: Hora em formato de 24 horas (00 a 23).
- `%M`: Minuto (00 a 59).
- `%S`: Segundo (00 a 59).
- `%A`: Nome completo do dia da semana (por exemplo, "segunda-feira").
- `%a`: Abreviação do dia da semana (por exemplo, "Seg").
- `%B`: Nome completo do mês (por exemplo, "setembro").
- `%b` ou `%h`: Abreviação do mês (por exemplo, "Set").
- `%Z`: Nome do fuso horário (por exemplo, "UTC" ou "America/New_York").

Aqui está um exemplo de como formatar um objeto `datetime` em uma string legível:

```python
import datetime

data_hora = datetime.datetime(2023, 9, 22, 15, 30, 0)

# Formatar a data e hora em um formato personalizado
formato_personalizado = "%Y-%m-%d %H:%M:%S"
data_formatada = data_hora.strftime(formato_personalizado)

print("Data e hora formatadas:", data_formatada)
```

Isso produzirá a saída: "2023-09-22 15:30:00", seguindo o formato personalizado especificado.

Você pode ajustar o formato de saída de acordo com as necessidades do seu projeto. Além disso, o método `strftime()` permite que você insira caracteres não alfanuméricos no formato para incluir caracteres especiais, como hifens, barras e espaços.

Lembre-se de que, ao analisar datas e horas de strings, você pode usar o método `strptime()` para converter strings formatadas em objetos `datetime`. É importante garantir que o formato da string corresponda ao formato especificado no argumento da função `strptime()`.

### Time zones com PYTZ

O módulo `pytz` em Python é uma biblioteca muito útil para lidar com fusos horários (time zones) em aplicações que envolvem datas e horas. O `pytz` estende a funcionalidade da biblioteca padrão `datetime` em Python para fornecer suporte a fusos horários mais abrangentes e precisos. Ele utiliza o banco de dados IANA (IANA Time Zone Database) para armazenar informações detalhadas sobre fusos horários de todo o mundo.

Aqui estão algumas das funcionalidades e conceitos-chave relacionados ao uso do `pytz`:

1. **Fusos Horários**: O `pytz` fornece acesso a uma lista extensa de fusos horários de todo o mundo. Você pode criar objetos de fusos horários específicos usando o `pytz.timezone()` e, em seguida, usá-los em conjunto com objetos `datetime` para realizar conversões de fuso horário.

```python
import pytz
from datetime import datetime

# Criar um objeto de fuso horário para Nova Iorque
nova_york = pytz.timezone('America/New_York')

# Obter a data e hora atual em Nova Iorque
data_hora_ny = datetime.now(nova_york)
```

2. **Conversão de Fuso Horário**: O `pytz` permite converter objetos `datetime` de um fuso horário para outro de forma fácil e precisa. Isso é especialmente útil quando você está trabalhando com datas e horas em diferentes partes do mundo.

```python
import pytz
from datetime import datetime

# Criar objetos de fusos horários
nova_york = pytz.timezone('America/New_York')
londres = pytz.timezone('Europe/London')

# Obter a data e hora atual em Nova Iorque
data_hora_ny = datetime.now(nova_york)

# Converter a data e hora de Nova Iorque para Londres
data_hora_londres = data_hora_ny.astimezone(londres)
```

3. **Lidar com Horário de Verão**: O `pytz` é capaz de lidar automaticamente com mudanças no horário de verão, ajustando as conversões de fuso horário conforme necessário.

4. **Nomes de Fusos Horários**: O `pytz` usa nomes de fusos horários baseados no banco de dados IANA, que são mais descritivos e precisos do que simples deslocamentos de UTC.

5. **Exceções de Fuso Horário**: O `pytz` também lida com exceções de fusos horários, como fusos horários que têm deslocamentos diferentes em diferentes partes do ano.

6. **Representação de UTC**: O `pytz` permite representar explicitamente a hora UTC (Tempo Universal Coordenado) usando o objeto `pytz.UTC`. Isso pode ser útil para operações em que você deseja garantir que a hora seja tratada como UTC.

```python
import pytz
from datetime import datetime

# Representar a hora atual como UTC
data_hora_utc = datetime.now(pytz.UTC)
```

O uso do módulo `pytz` é altamente recomendado sempre que você precisar trabalhar com fusos horários em Python, pois ele oferece um suporte completo e preciso para questões relacionadas a datas e horas em todo o mundo. Certifique-se de instalar a biblioteca `pytz` antes de usá-la em seu projeto, o que pode ser feito usando uma ferramenta de gerenciamento de pacotes, como o `pip`.
