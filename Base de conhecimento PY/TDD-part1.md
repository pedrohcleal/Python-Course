# TDD

**Desenvolvimento Orientado a Testes (TDD) em Python: Uma Visão Geral**

O Desenvolvimento Orientado a Testes (TDD) é uma abordagem de desenvolvimento de software que coloca a criação de testes automatizados como parte fundamental do ciclo de vida do desenvolvimento. No contexto do Python, o TDD é uma prática comum e eficaz para garantir a qualidade do código e facilitar a manutenção do software.

**Passos Básicos do TDD:**

1. **Escrever um Teste (Red):** Antes de começar a implementar uma funcionalidade, escreva um teste que falhe. Isso garante que o teste realmente avalia a funcionalidade desejada e que o código não atende a esse requisito ainda.

   Exemplo (usando o módulo `unittest`):
   ```python
   import unittest

   class TestMinhaClasse(unittest.TestCase):
       def test_soma(self):
           # Teste que falha, pois a funcionalidade ainda não foi implementada
           self.assertEqual(soma(2, 3), 5)
   ```

2. **Implementar o Código Mínimo Necessário (Green):** Implemente o código mínimo necessário para fazer o teste passar. Isso significa que, neste ponto, o código pode não ser a solução final ou otimizada, mas deve satisfazer os requisitos do teste.

   Exemplo:
   ```python
   def soma(a, b):
       return a + b
   ```

3. **Refatorar o Código (Refactor):** Após o teste passar, é possível refatorar o código para melhorá-lo, sem alterar seu comportamento. Os testes garantirão que as alterações não quebram a funcionalidade existente.

   Exemplo:
   ```python
   def soma(a, b):
       # Agora, a função é mais robusta e lida com tipos diferentes
       return int(a) + int(b)
   ```

**Ferramentas e Bibliotecas Comuns para TDD em Python:**

1. **unittest:** Módulo de teste integrado ao Python, que fornece uma estrutura para a criação e execução de testes.

2. **pytest:** Uma biblioteca de teste mais concisa e poderosa em comparação com o `unittest`. Ela suporta TDD eficientemente e oferece recursos adicionais.

3. **nose2:** Outra alternativa ao `unittest`, que simplifica a descoberta e execução de testes.

**Benefícios do TDD em Python:**

1. **Garantia de Qualidade:** O TDD ajuda a garantir que o código seja funcionalmente correto e que as alterações futuras não quebrem as funcionalidades existentes.

2. **Documentação Automática:** Os testes servem como documentação viva do código, fornecendo exemplos práticos de como usar as diferentes partes do sistema.

3. **Facilidade de Manutenção:** Testes automatizados tornam a manutenção do código mais fácil, especialmente em projetos de longo prazo.

Em resumo, o TDD é uma prática valiosa no desenvolvimento de software em Python, proporcionando confiança na qualidade do código e facilitando o processo de desenvolvimento e manutenção.

## Assertion

As asserções, em Python, são declarações usadas para verificar se uma determinada condição é verdadeira e, caso contrário, gerar uma exceção. Elas são frequentemente utilizadas para garantir que o código esteja funcionando conforme o esperado, especialmente em situações de teste. As asserções são implementadas com a palavra-chave `assert`.

A estrutura básica de uma asserção em Python é a seguinte:

```python
assert expressao, mensagem_de_erro
```

- `expressao`: A condição que deve ser verdadeira. Se for falsa, uma exceção `AssertionError` será levantada.
- `mensagem_de_erro`: Uma mensagem opcional que será exibida junto com a exceção em caso de falha.

**Exemplo Simples:**

```python
x = 10

assert x == 10, "O valor de x deve ser 10"
```

Neste exemplo, a asserção verifica se a variável `x` é igual a 10. Se a condição for falsa, a mensagem "O valor de x deve ser 10" será exibida junto com a exceção `AssertionError`.

**Utilização em Testes:**

As asserções são frequentemente utilizadas em testes unitários para verificar se o comportamento do código está de acordo com o esperado. Considere o seguinte exemplo usando o módulo `unittest`:

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

Neste exemplo, as asserções são usadas para verificar se as somas produzem os resultados esperados. Se uma asserção falhar durante a execução dos testes, o `unittest` registrará essa falha.

**Avisos ao Usar Assertions:**

1. **Desativar Assertions em Tempo de Produção:** Por padrão, as asserções são desativadas em ambientes de produção para evitar que o programa pare de funcionar devido a uma condição não atendida. Isso ocorre porque o interpretador Python é executado com a opção `-O` (otimização) por padrão, o que desativa as asserções. No entanto, é uma boa prática garantir que o código funcione corretamente durante o desenvolvimento e os testes.

2. **Não Utilizar para Controle de Fluxo:** As asserções não devem ser usadas como uma forma de controle de fluxo normal do programa, pois podem ser desativadas e não são destinadas a substituir estruturas condicionais regulares.

Em resumo, as asserções são ferramentas valiosas para garantir a corretude do código e facilitar a detecção de erros durante o desenvolvimento e os testes.

## doctest

`doctest` é um módulo em Python que permite incorporar testes diretamente na documentação do código, utilizando os exemplos de uso presentes nos docstrings. Os testes são escritos no formato de sessões interativas do interpretador Python, e o `doctest` executa esses exemplos e verifica se os resultados coincidem com a saída esperada.

A principal vantagem do `doctest` é que ele mantém a documentação e os testes próximos ao código, facilitando a manutenção e garantindo que os exemplos na documentação estejam sempre atualizados.

Aqui está um exemplo simples de uso do `doctest`:

```python
def soma(a, b):
    """
    Esta função retorna a soma de dois números.

    Exemplos:
    
    >>> soma(2, 3)
    5

    >>> soma(-1, 1)
    0
    """
    return a + b
```

Os exemplos interativos dentro do docstring fornecem casos de teste. Para executar esses testes, você pode utilizar o módulo `doctest` da seguinte maneira:

```python
import doctest

doctest.testmod()
```

Ao executar este código, o `doctest` importará o módulo em que está presente, analisará os docstrings, executará os exemplos interativos e verificará se os resultados coincidem com as saídas esperadas.

Caso não haja saída, significa que os testes foram bem-sucedidos. Caso contrário, o `doctest` irá gerar uma mensagem de erro indicando qual parte da documentação não está de acordo com a execução real.

Principais pontos a considerar sobre `doctest`:

1. **Integração com o Teste Unitário:** O `doctest` pode ser integrado a estruturas de teste unitário, como `unittest`. Isso permite que você use o `doctest` para testar partes específicas de seu código e, ao mesmo tempo, mantenha a flexibilidade de outros métodos de teste.

2. **Controle de Saída:** Às vezes, a saída pode ter pequenas diferenças, como espaços em branco ou mudanças de linha. O `doctest` permite a utilização de expressões regulares para ignorar essas diferenças.

3. **Segurança:** Tome cuidado ao usar `doctest` em código que aceita entrada do usuário, pois a execução de código no contexto do `doctest` pode ser uma vulnerabilidade de segurança.

O `doctest` é uma ferramenta poderosa para manter a documentação e os testes sempre alinhados, tornando o desenvolvimento mais eficiente e reduzindo a possibilidade de desatualizações na documentação.

### verbose=true  (doctests)

A opção `verbose` no módulo `doctest` é usada para especificar se a saída do teste deve incluir informações detalhadas sobre os testes executados. Quando `verbose` é definido como `True`, o `doctest` imprime informações adicionais durante a execução dos testes, como exemplos testados, falhas encontradas e estatísticas.

Aqui está um exemplo de como usar a opção `verbose` com o método `testmod()`:

```python
import doctest

def soma(a, b):
    """
    Esta função retorna a soma de dois números.

    Exemplos:
    
    >>> soma(2, 3)
    5

    >>> soma(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod(verbose=True)
```

Neste exemplo, `verbose=True` é passado para `testmod()`, o que significa que informações detalhadas sobre a execução dos testes serão impressas no console. Isso pode ser útil para depurar problemas em casos de teste ou entender melhor como o `doctest` está processando os exemplos interativos no código.

Sem a opção `verbose`, o `doctest` ainda executará os testes, mas a saída será mais concisa, indicando apenas se os testes foram bem-sucedidos ou se houve falhas.

A saída do teste pode incluir informações sobre exemplos testados, falhas e estatísticas de execução, proporcionando uma visão geral mais detalhada do processo de teste quando `verbose` é configurado como `True`.

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
