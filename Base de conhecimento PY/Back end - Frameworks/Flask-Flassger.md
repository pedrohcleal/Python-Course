# Flassger

Flasgger é uma biblioteca para o framework Flask que permite a documentação automática das APIs usando o padrão OpenAPI (anteriormente conhecido como Swagger). Ele ajuda a gerar uma interface interativa para testar endpoints da API, simplificando a visualização e o uso das APIs. Aqui está uma visão geral do uso de Flasgger no Flask:

### Instalação

Para instalar o Flasgger, você pode usar o pip:

```bash
pip install flasgger
```

### Configuração Básica

1. **Importações e Configuração Inicial**

   Primeiro, importe o Flasgger e configure-o no seu aplicativo Flask:

   ```python
   from flask import Flask
   from flasgger import Swagger

   app = Flask(__name__)
   swagger = Swagger(app)
   ```

2. **Definindo Documentação da API**

   Você pode usar docstrings nos endpoints para definir a documentação da API em um formato YAML ou JSON. Aqui está um exemplo básico:

   ```python
   @app.route('/api/hello', methods=['GET'])
   def hello():
       """
       Um exemplo simples de endpoint.
       ---
       responses:
         200:
           description: Retorna uma mensagem de boas-vindas.
           examples:
             application/json: {"message": "Hello, World!"}
       """
       return {"message": "Hello, World!"}
   ```

3. **Executando o Aplicativo**

   Execute o seu aplicativo Flask normalmente:

   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Documentação Personalizada

Você pode personalizar o Swagger UI fornecendo um arquivo de configuração YAML:

1. **Arquivo de Configuração**

   Crie um arquivo `swagger.yaml`:

   ```yaml
   swagger: "2.0"
   info:
     title: "Minha API"
     description: "API de exemplo usando Flasgger"
     version: "1.0.0"
   host: "localhost:5000"
   schemes:
     - "http"
   paths:
     /api/hello:
       get:
         summary: "Endpoint de boas-vindas"
         responses:
           200:
             description: "Mensagem de boas-vindas"
             examples:
               application/json: {"message": "Hello, World!"}
   ```

2. **Carregando a Configuração**

   Carregue a configuração no Flasgger:

   ```python
   from flask import Flask
   from flasgger import Swagger

   app = Flask(__name__)
   swagger = Swagger(app, template_file='swagger.yaml')

   @app.route('/api/hello', methods=['GET'])
   def hello():
       return {"message": "Hello, World!"}

   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Usando Blueprints

Se o seu aplicativo usar Blueprints, você pode integrar Flasgger da seguinte maneira:

1. **Definindo o Blueprint**

   ```python
   from flask import Blueprint, jsonify
   from flasgger import swag_from

   hello_blueprint = Blueprint('hello', __name__)

   @hello_blueprint.route('/api/hello', methods=['GET'])
   @swag_from({
       'responses': {
           200: {
               'description': 'Retorna uma mensagem de boas-vindas.',
               'examples': {
                   'application/json': {'message': 'Hello, World!'}
               }
           }
       }
   })
   def hello():
       return jsonify(message="Hello, World!")
   ```

2. **Registrando o Blueprint no Aplicativo Principal**

   ```python
   from flask import Flask
   from flasgger import Swagger

   app = Flask(__name__)
   swagger = Swagger(app)

   from hello_blueprint import hello_blueprint
   app.register_blueprint(hello_blueprint)

   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Conclusão

Flasgger simplifica a criação de documentação interativa para APIs desenvolvidas com Flask, facilitando o entendimento e teste dos endpoints. Ele suporta especificações OpenAPI/Swagger, permitindo uma documentação rica e detalhada. Com Flasgger, a manutenção e o uso de APIs Flask se tornam mais eficientes e intuitivos.
