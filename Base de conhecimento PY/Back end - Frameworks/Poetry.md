# Poetry

O Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para projetos Python. Ele oferece uma abordagem moderna para a gestão de bibliotecas e aplicativos Python, visando simplificar o processo de configuração, instalação de dependências e distribuição de pacotes. A seguir, estão descritas algumas das principais características e benefícios do Poetry:

### Características do Poetry

1. **Gerenciamento de Dependências**:
   - **Automático**: O Poetry gerencia automaticamente as dependências do projeto. Ele resolve e instala as bibliotecas necessárias com base nas especificações fornecidas no arquivo `pyproject.toml`.
   - **Arquivo de Bloqueio (`poetry.lock`)**: Similar ao `Pipfile.lock` do Pipenv ou `package-lock.json` do npm, o `poetry.lock` assegura que todas as dependências sejam instaladas em versões específicas, garantindo reprodutibilidade no ambiente de desenvolvimento.

2. **Empacotamento**:
   - O Poetry facilita a criação e publicação de pacotes Python. Ele usa o arquivo `pyproject.toml` para definir metadados do projeto, tais como nome, versão, descrição, autores, e outros detalhes relevantes para a distribuição.

3. **Configuração Simples**:
   - **Arquivo `pyproject.toml`**: O arquivo de configuração central do Poetry, que substitui o `setup.py` e `requirements.txt` tradicionalmente usados no desenvolvimento Python. Esse arquivo é fácil de ler e editar, permitindo a definição clara de dependências e metadados do projeto.

4. **Ambientes Virtuais**:
   - O Poetry pode criar e gerenciar ambientes virtuais automaticamente, garantindo que as dependências do projeto não entrem em conflito com outras instalações Python no sistema.

5. **Publicação de Pacotes**:
   - A ferramenta oferece comandos integrados para publicar pacotes no PyPI ou em repositórios privados, simplificando o processo de distribuição de bibliotecas e aplicativos Python.

### Benefícios do Uso do Poetry

- **Reprodutibilidade**: Com o uso do arquivo `poetry.lock`, os ambientes de desenvolvimento e produção podem ser facilmente replicados, garantindo que as mesmas versões de dependências sejam usadas em diferentes sistemas.
- **Simplicidade**: A configuração centralizada no `pyproject.toml` facilita a manutenção e leitura das dependências e metadados do projeto.
- **Integração com Ambientes Virtuais**: O Poetry lida automaticamente com a criação e ativação de ambientes virtuais, simplificando a configuração do ambiente de desenvolvimento.
- **Gestão de Dependências Melhorada**: A resolução automática de dependências e a criação de arquivos de bloqueio ajudam a evitar conflitos de versão e problemas de compatibilidade.
- **Empacotamento e Distribuição**: O Poetry facilita o empacotamento e publicação de pacotes, integrando-se perfeitamente com o PyPI e outros repositórios.

### Exemplo de Uso do Poetry

#### Instalação
Para instalar o Poetry, você pode usar o seguinte comando:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Inicialização de um Projeto
Para iniciar um novo projeto com o Poetry, você pode usar:

```bash
poetry new meu_projeto
cd meu_projeto
```

#### Adição de Dependências
Para adicionar uma dependência ao seu projeto, use:

```bash
poetry add requests
```

#### Instalação de Dependências
Para instalar todas as dependências listadas no arquivo `pyproject.toml`:

```bash
poetry install
```

#### Publicação de um Pacote
Para publicar seu pacote no PyPI, configure suas credenciais e use:

```bash
poetry publish --build
```

### Conclusão

O Poetry é uma ferramenta poderosa que simplifica o desenvolvimento, gerenciamento de dependências e distribuição de pacotes em projetos Python. Sua abordagem moderna e integrada ajuda desenvolvedores a manter ambientes limpos, reprodutíveis e bem configurados, facilitando o ciclo de vida de desenvolvimento e publicação de software.

## Comandos

O Poetry é uma ferramenta robusta para gerenciamento de dependências e empacotamento em projetos Python. Ele fornece uma série de comandos que facilitam a criação, gestão e publicação de projetos Python. Abaixo estão os comandos mais comuns do Poetry, organizados por categorias com uma breve descrição de cada um.

### Comandos Básicos

#### `poetry new`
Cria um novo projeto Python com a estrutura padrão.

```bash
poetry new my_project
```

#### `poetry init`
Inicializa um novo projeto no diretório atual, guiando você através de uma série de perguntas para configurar o `pyproject.toml`.

```bash
poetry init
```

### Gerenciamento de Dependências

#### `poetry add`
Adiciona uma nova dependência ao projeto e a instala.

```bash
poetry add requests
```

#### `poetry remove`
Remove uma dependência do projeto.

```bash
poetry remove requests
```

#### `poetry install`
Instala todas as dependências listadas no `pyproject.toml` e `poetry.lock`.

```bash
poetry install
```

#### `poetry update`
Atualiza todas as dependências do projeto para suas versões mais recentes permitidas pelas restrições do `pyproject.toml`.

```bash
poetry update
```

### Gerenciamento do Ambiente Virtual

#### `poetry shell`
Abre um novo shell dentro do ambiente virtual gerenciado pelo Poetry.

```bash
poetry shell
```

#### `poetry run`
Executa um comando dentro do ambiente virtual sem precisar ativá-lo explicitamente.

```bash
poetry run python script.py
```

### Informações sobre o Projeto

#### `poetry show`
Exibe informações sobre as dependências do projeto.

- Para listar todas as dependências:
  ```bash
  poetry show
  ```

- Para listar uma dependência específica:
  ```bash
  poetry show requests
  ```

- Para incluir dependências transitivas:
  ```bash
  poetry show --tree
  ```

### Empacotamento e Publicação

#### `poetry build`
Constrói os pacotes fonte e Wheel do projeto.

```bash
poetry build
```

#### `poetry publish`
Publica o pacote no PyPI ou em um repositório configurado.

- Para publicar no PyPI:
  ```bash
  poetry publish --build
  ```

- Para usar um repositório personalizado:
  ```bash
  poetry publish --repository my-repo
  ```

### Configuração

#### `poetry config`
Gera ou modifica configurações do Poetry. As configurações podem ser definidas localmente (por projeto) ou globalmente.

- Para definir um token de API global para o PyPI:
  ```bash
  poetry config pypi-token.pypi <seu-token-pypi>
  ```

- Para definir uma configuração específica do projeto:
  ```bash
  poetry config --local virtualenvs.in-project true
  ```

### Outras Ferramentas Úteis

#### `poetry check`
Verifica se o `pyproject.toml` e o `poetry.lock` estão consistentes e se as dependências são resolvíveis.

```bash
poetry check
```

#### `poetry cache`
Gerencia o cache de pacotes do Poetry.

- Para listar o cache:
  ```bash
  poetry cache list
  ```

- Para limpar o cache:
  ```bash
  poetry cache clear --all
  ```

### Comandos de Depuração e Desenvolvimento

#### `poetry lock`
Gera o arquivo `poetry.lock` sem instalar nada.

```bash
poetry lock
```

#### `poetry export`
Exporta as dependências para um formato `requirements.txt`.

```bash
poetry export -f requirements.txt --output requirements.txt
```

### Exemplos de Fluxos de Trabalho Comuns

#### Criar um Novo Projeto
```bash
poetry new my_project
cd my_project
poetry install
```

#### Adicionar uma Dependência
```bash
poetry add flask
```

#### Atualizar Todas as Dependências
```bash
poetry update
```

#### Publicar um Pacote
```bash
poetry build
poetry publish
```

Com esses comandos, o Poetry oferece uma maneira eficiente e estruturada de gerenciar projetos Python, facilitando a configuração, o desenvolvimento e a distribuição de pacotes.

