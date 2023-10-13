# Bibliotecas Py part 5

## Selenium

O Selenium é uma ferramenta de automação de testes amplamente usada para testar aplicativos da web por meio de scripts. Com o Selenium, você pode automatizar a interação de um navegador da web com um site ou aplicativo da web, executando ações como clicar em botões, preencher formulários, navegar por páginas e extrair informações.

O Selenium suporta várias linguagens de programação, incluindo Python, o que o torna uma escolha popular para desenvolvedores que desejam automatizar tarefas de teste em seus aplicativos da web. Para usar o Selenium com Python, você precisa do módulo Python chamado "selenium", que pode ser instalado usando um gerenciador de pacotes como o pip.

Aqui estão os passos básicos para começar a usar o Selenium com Python:

1. Instale o Selenium: Você pode instalar o Selenium para Python executando o seguinte comando no seu terminal ou prompt de comando:

```bash
pip install selenium
```

2. Baixe um driver de navegador: O Selenium requer um driver específico para o navegador que você deseja automatizar. Os drivers são essenciais para permitir que o Selenium interaja com o navegador. Alguns dos drivers populares incluem o ChromeDriver, o GeckoDriver (para o Firefox) e o WebDriver para o Safari. Certifique-se de baixar o driver correto para o seu navegador.

3. Escreva seu script de automação: Agora você pode escrever um script em Python para automatizar as ações que deseja executar no navegador. Aqui está um exemplo simples que abre o Google Chrome, acessa o site do Google e faz uma pesquisa:

```python
from selenium import webdriver

# Inicialize o driver do Chrome (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

# Abra uma página da web
driver.get("https://www.google.com")

# Encontre o campo de pesquisa e digite algo nele
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium with Python")

# Clique no botão de pesquisa
search_box.submit()

# Feche o navegador
driver.quit()
```

4. Execute o script: Salve o script em um arquivo Python (.py) e execute-o. O Selenium abrirá o navegador, executará as ações especificadas e, em seguida, fechará o navegador.

O Selenium com Python oferece muitos recursos avançados, como a capacidade de esperar por elementos, manipular cookies, alternar entre janelas e frames, tirar screenshots e muito mais. É uma ferramenta poderosa para automação de tarefas relacionadas à web, testes de software e scraping de dados da web.

## Selecionando elementos com Selenium

O Selenium oferece recursos poderosos para interagir com elementos da página da web de maneira dinâmica, como aguardar a presença de elementos, clicar em botões, preencher formulários e muito mais. Para fazer isso, você pode usar as classes `By`, `ExpectedConditions` e `WebDriverWait`. Vou explicar como cada uma delas funciona e como você pode usá-las:

1. `By`:

A classe `By` é usada para localizar elementos na página da web. Ela fornece vários métodos estáticos para criar localizadores baseados em diferentes critérios, como ID, nome, classe, tag, seletor CSS, seletor XPath e outros. Aqui está um exemplo de como você pode usar a classe `By` para localizar um elemento por ID:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Localiza um elemento pelo ID
element = driver.find_element(By.ID, "elemento_id")
```

2. `ExpectedConditions`:

A classe `ExpectedConditions` é usada em conjunto com o `WebDriverWait` para criar condições que o Selenium aguardará antes de interagir com um elemento. Ela inclui várias condições úteis, como esperar até que um elemento esteja visível, clicável, presente, ausente e muito mais. Aqui está um exemplo de como usar o `ExpectedConditions` com o `WebDriverWait` para esperar até que um elemento esteja visível:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "elemento_id"))
)
```

Neste exemplo, o `WebDriverWait` aguardará até 10 segundos para que o elemento com o ID "elemento_id" seja visível na página da web.

3. `WebDriverWait`:

O `WebDriverWait` é usado para esperar por uma condição específica em um período de tempo definido. Você deve especificar o driver (instância do navegador) e o tempo máximo de espera. Você pode combinar o `WebDriverWait` com o `ExpectedConditions` para criar uma espera condicional. Se a condição não for satisfeita dentro do tempo especificado, uma exceção será gerada. Caso contrário, o programa continuará a execução.

Aqui está um exemplo de como você pode usar o `WebDriverWait` para esperar até que um elemento esteja clicável:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Inicializa o WebDriverWait
wait = WebDriverWait(driver, 10)

# Espera até que o elemento seja clicável
element = wait.until(
    EC.element_to_be_clickable((By.ID, "elemento_id"))
)

# Agora você pode clicar no elemento
element.click()
```

Esses três componentes, `By`, `ExpectedConditions` e `WebDriverWait`, permitem que você escreva scripts de automação Selenium mais robustos e confiáveis, aguardando condições específicas antes de interagir com os elementos da página da web. Isso é particularmente útil para lidar com páginas da web dinâmicas ou lentas, onde os elementos podem não estar imediatamente disponíveis para interação.

## Enviando teclas com a classe "keys"

Para enviar teclas com a classe `Keys` do Selenium em Python, você pode usar essa classe para gerar eventos de teclado, como pressionar e soltar teclas. A classe `Keys` é usada principalmente em combinação com ações do Selenium, como `ActionChains`, para realizar interações complexas de teclado.

Aqui está um exemplo de como enviar teclas usando a classe `Keys`:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Simule a pressão de teclas
search_box = driver.find_element(By.ID, "elemento_id")
search_box.send_keys("Texto de exemplo")

# Pressionar a tecla Enter após preencher o campo de pesquisa
search_box.send_keys(Keys.ENTER)

# Simular combinação de teclas (por exemplo, Ctrl+A para selecionar tudo)
search_box.send_keys(Keys.CONTROL + 'a')
```

Neste exemplo, usamos `Keys.ENTER` para simular a pressão da tecla Enter após preencher um campo de pesquisa. Também usamos `Keys.CONTROL + 'a'` para simular a combinação de teclas "Ctrl + A", que seleciona todo o texto em um campo de entrada.

Você pode combinar várias teclas e sequências de teclas para realizar ações mais complexas, como Ctrl+Shift+T, Ctrl+C, Ctrl+V, etc. A classe `Keys` oferece uma variedade de constantes para representar as teclas, e você pode usar o operador `+` para combinar teclas.

Lembre-se de que você deve ter cuidado ao usar a automação de teclado em sites, pois isso pode violar os termos de uso de alguns sites ou aplicativos da web. Certifique-se de estar ciente das políticas de uso e leis locais ao automatizar interações na web.

## Sobre  find_element e find_elements by no Selenium

No Selenium, os métodos `find_element` e `find_elements` são usados para localizar elementos na página da web com base em diferentes critérios de busca. Ambos os métodos retornam elementos que correspondem aos critérios especificados, mas eles têm algumas diferenças fundamentais:

1. `find_element`:

- `find_element` é usado para localizar o primeiro elemento que corresponde aos critérios de busca especificados. Ele retorna uma única instância do elemento encontrado, que é a primeira correspondência na página. Se não houver correspondências, ele lançará uma exceção `NoSuchElementException`.

Exemplo de uso de `find_element`:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Localiza um único elemento pelo ID
element = driver.find_element(By.ID, "elemento_id")
```

2. `find_elements`:

- `find_elements`, por outro lado, é usado para localizar todos os elementos que correspondem aos critérios de busca especificados. Ele retorna uma lista de elementos, mesmo que haja apenas um único elemento correspondente. Se não houver correspondências, ele retorna uma lista vazia.

Exemplo de uso de `find_elements`:

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Localiza todos os elementos com a tag "a"
links = driver.find_elements(By.TAG_NAME, "a")
```

Ambos os métodos aceitam dois argumentos: o primeiro é o critério de busca, especificado usando a classe `By`, que pode ser `By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.XPATH`, `By.CSS_SELECTOR`, entre outros; o segundo argumento é o valor que corresponde ao critério de busca.

Em resumo, `find_element` é usado quando você deseja localizar um único elemento correspondente aos critérios de busca, enquanto `find_elements` é usado quando você deseja localizar todos os elementos correspondentes. Esses métodos são fundamentais para interagir com elementos da página da web ao automatizar tarefas usando o Selenium.
