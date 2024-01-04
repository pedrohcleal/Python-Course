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
