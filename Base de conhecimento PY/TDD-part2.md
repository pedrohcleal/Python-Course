# TDD part2


## unittest

O módulo `unittest` em Python fornece um framework de teste unitário que permite a criação e execução de testes para garantir a qualidade do código. O `unittest` segue o padrão xUnit e oferece uma série de recursos para a criação de testes, a organização de testes em classes e a execução de testes de forma automatizada. Aqui estão os principais conceitos e recursos do `unittest`:

1. **Testes Unitários e Métodos de Teste:**
   - Um teste unitário é uma unidade básica de teste que verifica uma única funcionalidade do código.
   - Métodos de teste são funções dentro de classes de teste que executam verificações específicas.

2. **Classe TestCase:**
   - Os testes são organizados em classes que herdam de `unittest.TestCase`.
   - Cada método de teste dentro da classe deve começar com o nome "test".

3. **Assert Statements:**
   - As asserções (`assert`) são usadas para verificar se uma condição é verdadeira.
   - Métodos como `assertEqual`, `assertTrue`, `assertFalse`, etc., são usados para realizar verificações específicas.

4. **Configuração e Limpeza:**
   - Métodos `setUp` e `tearDown` são usados para configuração e limpeza antes e depois dos testes.
   - `setUpClass` e `tearDownClass` executam configuração e limpeza de classe uma vez para todos os testes na classe.

5. **Descoberta e Execução de Testes:**
   - O comando `unittest.main()` pode ser usado para descobrir e executar testes em um arquivo.
   - A descoberta de testes pode ser feita usando a linha de comando com `python -m unittest discover`.

6. **Test Suites:**
   - Um conjunto de testes pode ser agrupado em uma "test suite" usando a classe `TestSuite`.
   - Isso permite a execução de conjuntos específicos de testes.

7. **Mocking e Patching:**
   - O módulo `unittest.mock` fornece recursos para criar objetos simulados (mocks) para isolar partes do código durante os testes.
   - `patch` é usado para substituir objetos por mocks temporariamente.

8. **Testes Parametrizados:**
   - A decoração `@unittest.parametrize` permite a execução de um método de teste com diferentes conjuntos de parâmetros.
   - Isso ajuda a evitar a duplicação de código de teste.

Exemplo básico de teste usando `unittest`:

```python
import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        resultado = soma(3, 4)
        self.assertEqual(resultado, 7, "A soma de 3 e 4 deve ser 7")

    def test_soma_negativos(self):
        resultado = soma(-2, -5)
        self.assertEqual(resultado, -7, "A soma de -2 e -5 deve ser -7")

if __name__ == '__main__':
    unittest.main()
```

Ao executar este script, `unittest` descobrirá automaticamente as classes e métodos de teste e executará os testes, exibindo a saída no console.

O `unittest` é uma ferramenta poderosa para criar e executar testes unitários em Python, ajudando a garantir a qualidade e confiabilidade do código.

## `assert`

As asserções desempenham um papel crucial nos testes unitários usando o módulo `unittest` em Python. As asserções são afirmações que verificam se determinadas condições são verdadeiras e, se não forem, geram falhas nos testes. O módulo `unittest` fornece vários métodos de asserção para verificar diferentes condições. Aqui estão alguns dos métodos de asserção mais comuns:

1. **`assertEqual(a, b, msg=None)`:**
   - Verifica se `a` é igual a `b`.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertEqual(soma(2, 3), 5, "A soma de 2 e 3 deve ser 5")
   ```

2. **`assertNotEqual(a, b, msg=None)`:**
   - Verifica se `a` não é igual a `b`.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertNotEqual(soma(2, 3), 6, "A soma de 2 e 3 não deve ser 6")
   ```

3. **`assertTrue(expr, msg=None)`:**
   - Verifica se a expressão `expr` é verdadeira.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertTrue(len([1, 2, 3]) == 3, "A lista deve ter 3 elementos")
   ```

4. **`assertFalse(expr, msg=None)`:**
   - Verifica se a expressão `expr` é falsa.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertFalse(2 + 2 == 5, "A soma de 2 e 2 não deve ser 5")
   ```

5. **`assertIsNone(expr, msg=None)`:**
   - Verifica se a expressão `expr` é `None`.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertIsNone(funcao_retorna_none(), "A função deve retornar None")
   ```

6. **`assertIsNotNone(expr, msg=None)`:**
   - Verifica se a expressão `expr` não é `None`.
   - Se a condição não for verdadeira, a mensagem opcional `msg` será exibida.

   Exemplo:
   ```python
   self.assertIsNotNone(funcao_retorna_alguma_coisa(), "A função não deve retornar None")
   ```

Estes são apenas alguns dos métodos de asserção disponíveis no módulo `unittest`. Eles permitem que você construa testes claros e precisos para verificar o comportamento esperado do seu código. Ao usar as asserções apropriadas, você pode tornar seus testes mais robustos e informativos, facilitando a identificação e correção de problemas no código.

## TDD + Unittest

O Test-Driven Development (TDD) é uma metodologia de desenvolvimento de software que enfatiza a criação de testes antes da implementação do código. O objetivo é garantir que o código seja funcional e atenda aos requisitos definidos pelos testes desde o início do processo de desenvolvimento. O módulo `unittest` em Python é frequentemente utilizado no contexto do TDD para criar e executar testes de unidade.

A abordagem básica do TDD pode ser resumida em três etapas: "Red-Green-Refactor".

1. **Red (Vermelho):** Escrever um teste que falhe, indicando que a funcionalidade ainda não foi implementada ou está incorreta.

   Exemplo (usando `unittest`):
   ```python
   import unittest

   class TestSoma(unittest.TestCase):
       def test_soma_positivos(self):
           self.assertEqual(soma(2, 3), 5)
   ```

   Neste ponto, a função `soma` ainda não está implementada, então o teste falhará.

2. **Green (Verde):** Implementar o código mínimo necessário para fazer o teste passar.

   Exemplo:
   ```python
   def soma(a, b):
       return a + b
   ```

   Agora, ao executar o teste, ele deve passar porque a funcionalidade mínima foi implementada.

3. **Refactor (Refatorar):** Melhorar o código, mantendo os testes verdes.

   Exemplo:
   ```python
   def soma(a, b):
       # Adicionada uma verificação de tipos
       if isinstance(a, (int, float)) and isinstance(b, (int, float)):
           return a + b
       else:
           raise ValueError("Ambos os argumentos devem ser números.")
   ```

   Ao refatorar, é possível melhorar a qualidade do código sem alterar seu comportamento. Os testes garantem que as alterações não quebrem a funcionalidade existente.

**Vantagens do TDD com unittest:**

1. **Garantia de Qualidade:** O TDD garante que o código seja testado continuamente à medida que é desenvolvido, reduzindo a probabilidade de erros.

2. **Design Incremental:** O desenvolvimento é feito em pequenos incrementos, com testes validando cada passo. Isso leva a um design mais modular e coeso.

3. **Documentação Viva:** Os testes servem como documentação atualizada e pronta para uso, demonstrando como o código deve ser usado.

4. **Refatoração Segura:** A presença de testes facilita a refatoração do código, pois os testes fornecem feedback imediato sobre a integridade do código após as alterações.

**Exemplo Completo:**

```python
import unittest

def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos os argumentos devem ser números.")

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -5), -7)

    def test_soma_invalida(self):
        with self.assertRaises(ValueError):
            soma("abc", 5)

if __name__ == '__main__':
    unittest.main()
```

Este é um exemplo simples de TDD usando `unittest`. Cada teste é escrito antes da implementação correspondente, garantindo que o código seja validado em relação aos requisitos específicos definidos pelos testes.

## `subTest`

O método `subTest()` é uma funcionalidade útil no módulo `unittest` em Python, que permite a execução de subtestes dentro de um método de teste. Ele é particularmente útil quando você deseja executar várias verificações dentro de um único método de teste e obter informações específicas sobre falhas, em vez de abortar o teste na primeira falha.

A estrutura básica do `subTest()` é a seguinte:

```python
import unittest

class MeuTeste(unittest.TestCase):
    def test_subteste(self):
        with self.subTest():
            # Código do subteste 1
            self.assertEqual(1 + 1, 2)

        with self.subTest():
            # Código do subteste 2
            self.assertEqual(2 * 3, 6)

        with self.subTest():
            # Código do subteste 3
            self.assertEqual(8 / 2, 4)
```

Aqui estão alguns pontos importantes sobre o uso do `subTest()`:

1. **Falhas Isoladas:** Se um subteste falhar, o restante do teste continuará sendo executado. Isso é útil para identificar todas as falhas no teste de uma vez, em vez de interromper na primeira falha.

2. **Identificação Detalhada:** Quando um subteste falha, a mensagem de erro inclui informações detalhadas sobre qual subteste específico falhou. Isso facilita a localização e correção de problemas.

3. **Uso em Estruturas de Dados Iteráveis:** O `subTest()` é frequentemente usado em loops, especialmente ao testar várias entradas ou casos de borda. Isso ajuda a garantir que todas as iterações sejam executadas, mesmo que uma delas falhe.

Aqui está um exemplo mais prático usando `subTest()` em um loop:

```python
import unittest

def verifica_paridade(numero):
    return numero % 2 == 0

class TestVerificaParidade(unittest.TestCase):
    def test_verifica_paridade(self):
        entradas = [2, 3, 8, 5, 10]

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                self.assertTrue(verifica_paridade(entrada), f"{entrada} deveria ser par.")

if __name__ == '__main__':
    unittest.main()
```

Neste exemplo, o teste verifica se uma função `verifica_paridade` está correta para uma lista de entradas. Se algum caso falhar, o `subTest()` fornece detalhes específicos sobre qual entrada causou a falha.

O uso de `subTest()` é uma prática recomendada quando você deseja manter a execução de testes e identificar todas as falhas, mesmo quando ocorrem em diferentes partes de um método de teste. Isso ajuda a tornar os testes mais robustos e informativos.

##  Métodos de configuração e limpeza - `unittest`

No módulo `unittest` em Python, a configuração e limpeza de testes são realizadas por métodos especiais que podem ser definidos em uma classe de teste. Esses métodos são chamados automaticamente antes e depois da execução de cada teste, proporcionando um ambiente controlado e consistente para a execução dos testes. Os principais métodos são `setUp()`, `tearDown()`, `setUpClass()`, e `tearDownClass()`.

### `setUp()` e `tearDown()`:

- **`setUp(self)`:**
  - Método chamado antes da execução de cada teste.
  - Utilizado para configurar condições prévias necessárias para a execução do teste.

- **`tearDown(self)`:**
  - Método chamado após a execução de cada teste.
  - Utilizado para realizar limpeza ou restaurar o ambiente após a execução do teste.

Exemplo:

```python
import unittest

class TestExemplo(unittest.TestCase):
    def setUp(self):
        # Configuração prévia para todos os testes
        self.lista = [1, 2, 3]

    def tearDown(self):
        # Limpeza após cada teste
        self.lista = []

    def test_soma_elementos(self):
        # Teste que usa a lista configurada em setUp
        resultado = sum(self.lista)
        self.assertEqual(resultado, 6)

    def test_tamanho_lista(self):
        # Outro teste que usa a lista configurada em setUp
        tamanho = len(self.lista)
        self.assertEqual(tamanho, 3)

if __name__ == '__main__':
    unittest.main()
```

### `setUpClass()` e `tearDownClass()`:

- **`setUpClass(cls)`:**
  - Método chamado uma vez antes da execução de todos os testes na classe.
  - Utilizado para configurações que afetam todos os testes na classe.

- **`tearDownClass(cls)`:**
  - Método chamado uma vez após a execução de todos os testes na classe.
  - Utilizado para limpeza ou restauração após todos os testes.

Exemplo:

```python
import unittest

class TestExemplo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuração prévia para todos os testes na classe
        print("Configurando a classe de teste")

    @classmethod
    def tearDownClass(cls):
        # Limpeza após todos os testes na classe
        print("Limpando a classe de teste")

    def test_um(self):
        # Teste 1
        self.assertTrue(True)

    def test_dois(self):
        # Teste 2
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
```

Esses métodos de configuração e limpeza fornecem uma maneira de criar um ambiente controlado e previsível para a execução dos testes, garantindo que condições prévias necessárias sejam estabelecidas e que a limpeza seja realizada após a execução dos testes. Isso é fundamental para garantir a reprodutibilidade e a confiabilidade dos testes.
