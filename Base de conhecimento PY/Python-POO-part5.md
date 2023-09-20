# POO Part5

## Classe Enum

Em Python, a classe `Enum` faz parte do módulo `enum`, que foi introduzido na versão 3.4 da linguagem. Enums são utilizados para criar conjuntos de constantes nomeadas, o que torna o código mais legível e evita erros relacionados a valores mágicos (números ou strings diretamente incorporados no código).

Aqui está uma descrição básica de como usar a classe `Enum` em Python:

1. Importar o módulo `enum`:

   Para começar a usar Enums, você deve importar o módulo `enum`:

   ```python
   from enum import Enum
   ```

2. Definir uma classe Enum:

   Você pode criar uma classe Enum estendendo a classe base `Enum`. Cada membro da enumeração é definido como uma instância dessa classe. Aqui está um exemplo simples:

   ```python
   from enum import Enum

   class DiaDaSemana(Enum):
       SEGUNDA = 1
       TERCA = 2
       QUARTA = 3
       QUINTA = 4
       SEXTA = 5
       SABADO = 6
       DOMINGO = 7
   ```

   Neste exemplo, criamos uma enumeração chamada `DiaDaSemana` com sete membros, cada um representando um dia da semana.

3. Acesso aos membros da enumeração:

   Agora você pode acessar os membros da enumeração como atributos da classe `DiaDaSemana`. Por exemplo:

   ```python
   >>> print(DiaDaSemana.SEGUNDA)
   DiaDaSemana.SEGUNDA
   >>> print(DiaDaSemana.SEGUNDA.value)
   1
   ```

   O atributo `.value` fornece o valor associado a cada membro da enumeração.

4. Comparação de membros da enumeração:

   Você pode comparar membros da enumeração usando operadores de igualdade. Por exemplo:

   ```python
   >>> hoje = DiaDaSemana.SEGUNDA
   >>> amanha = DiaDaSemana.TERCA
   >>> print(hoje == amanha)
   False
   ```

5. Iteração sobre membros da enumeração:

   É possível iterar sobre todos os membros de uma enumeração usando um loop `for`:

   ```python
   for dia in DiaDaSemana:
       print(dia)
   ```

   Isso irá imprimir todos os membros da enumeração na ordem em que foram definidos.

Enums são úteis para tornar o código mais legível e evitar erros de digitação, já que os membros da enumeração são constantes nomeadas e não podem ser reatribuídos acidentalmente. Além disso, eles fornecem uma maneira eficaz de representar valores discretos e bem definidos em seu código Python.
