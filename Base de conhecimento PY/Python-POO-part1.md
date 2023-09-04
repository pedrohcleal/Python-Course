# Introdução a POO

A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia na ideia de estruturar o código em torno de objetos, que são instâncias de classes. No Python, a POO é uma parte fundamental da linguagem e oferece uma maneira eficaz de organizar, reutilizar e modularizar o código. Nesta introdução, vamos explorar os conceitos básicos da POO em Python.

Em POO, uma classe é um modelo ou plano para criar objetos. Um objeto é uma instância de uma classe e contém características (atributos) e comportamentos (métodos). A POO se concentra em encapsular o estado e o comportamento relacionados em um único pacote chamado objeto.

Vamos começar com um exemplo simples para ilustrar os conceitos:

```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        self.velocidade -= quantidade
        if self.velocidade < 0:
            self.velocidade = 0

    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}, Velocidade: {self.velocidade} km/h")

# Criando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Ford", "Mustang")

# Usando os métodos para interagir com os objetos
carro1.acelerar(30)
carro2.acelerar(50)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
```

Neste exemplo, criamos uma classe `Carro` com atributos como `marca`, `modelo` e `velocidade`. Os métodos `acelerar`, `frear` e `exibir_informacoes` permitem interagir com os objetos criados a partir dessa classe.

A função `__init__` é um construtor especial que é chamado quando um objeto é criado a partir da classe. O parâmetro `self` refere-se ao próprio objeto e é usado para acessar seus atributos e métodos.

Através da POO, o código se torna mais organizado, modular e reutilizável. As classes permitem abstrair os detalhes complexos do programa, tornando-o mais compreensível e manutenível.

Em resumo, a POO em Python envolve a criação de classes que definem atributos e métodos, e a criação de objetos a partir dessas classes para interagir com o código. Isso promove a estruturação lógica e a eficiência na programação.

## Atributos de classe

Em Python, os atributos de classe são variáveis que pertencem a uma classe em vez de a uma instância específica dessa classe. Eles são compartilhados por todas as instâncias da classe e são definidos dentro da classe, mas fora de qualquer método. Os atributos de classe são usados para armazenar informações que são relevantes para a classe como um todo, em vez de para instâncias individuais da classe. Aqui estão alguns pontos-chave sobre os atributos de classe em Python:

1. Definição de Atributos de Classe:
   Os atributos de classe são definidos dentro da classe, fora de qualquer método. Eles são declarados diretamente na classe usando a notação `nome_atributo = valor`.

2. Compartilhamento de Dados:
   Todos os objetos (instâncias) de uma classe têm acesso ao mesmo valor do atributo de classe. Isso significa que as alterações feitas em um atributo de classe em uma instância serão refletidas em todas as outras instâncias da mesma classe.

3. Acesso a Atributos de Classe:
   Para acessar um atributo de classe, você pode usar a sintaxe `NomeDaClasse.nome_do_atributo` ou `nome_instancia.nome_do_atributo`, embora seja mais comum acessá-lo usando o nome da classe.

4. Modificação de Atributos de Classe:
   Os atributos de classe podem ser modificados usando o nome da classe, mas isso afetará todas as instâncias da classe. Por exemplo:
   
   ```python
   class MinhaClasse:
       atributo_de_classe = 0

   obj1 = MinhaClasse()
   obj2 = MinhaClasse()

   MinhaClasse.atributo_de_classe = 42  # Altera o valor para todas as instâncias
   print(obj1.atributo_de_classe)  # Saída: 42
   print(obj2.atributo_de_classe)  # Saída: 42
   ```

5. Uso Comum:
   Os atributos de classe são frequentemente usados para armazenar configurações, constantes compartilhadas ou informações globais relevantes para a classe em si.

Aqui está um exemplo simples de uma classe com um atributo de classe:

```python
class Pessoa:
    populacao = 0  # Atributo de classe para rastrear o número total de pessoas

    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    def __del__(self):
        Pessoa.populacao -= 1

pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob")

print(Pessoa.populacao)  # Saída: 2 (o número total de pessoas é mantido no atributo de classe)
```

Neste exemplo, o atributo de classe `populacao` é usado para rastrear o número total de instâncias da classe `Pessoa`, e ele é incrementado no construtor e decrementado no destrutor das instâncias.

