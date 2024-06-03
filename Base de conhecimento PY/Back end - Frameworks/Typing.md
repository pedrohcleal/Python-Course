Typing em Python refere-se à anotação de tipos, uma funcionalidade introduzida para ajudar os desenvolvedores a especificar os tipos de variáveis, parâmetros de funções e valores de retorno. Essa funcionalidade melhora a legibilidade do código, auxilia na detecção precoce de erros e melhora o suporte de ferramentas como linters e IDEs. A tipagem em Python, no entanto, é opcional e o interpretador do Python não a utiliza para impor restrições durante a execução do programa (Python é uma linguagem dinamicamente tipada).

### Anotações de Tipo Básicas

1. **Variáveis**:
   ```python
   age: int = 25
   name: str = "Alice"
   ```
   
2. **Funções**:
   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}"
   ```
   
### Tipos Comuns

- **Tipos Primitivos**: `int`, `float`, `str`, `bool`
- **Coleções**: `List`, `Tuple`, `Set`, `Dict`
  ```python
  from typing import List, Tuple, Set, Dict

  names: List[str] = ["Alice", "Bob"]
  coordinates: Tuple[int, int] = (10, 20)
  unique_numbers: Set[int] = {1, 2, 3}
  person_info: Dict[str, int] = {"Alice": 30, "Bob": 25}
  ```

### Tipagem Avançada

1. **Union**: Para variáveis que podem ter múltiplos tipos.
   ```python
   from typing import Union

   def get_data(data: Union[int, str]) -> str:
       return str(data)
   ```

2. **Optional**: Para variáveis que podem ser de um determinado tipo ou `None`.
   ```python
   from typing import Optional

   def get_name(name: Optional[str] = None) -> str:
       if name is None:
           return "Anonymous"
       return name
   ```

3. **Any**: Para variáveis que podem ser de qualquer tipo.
   ```python
   from typing import Any

   def process_data(data: Any) -> None:
       print(data)
   ```

4. **Callable**: Para funções ou objetos que podem ser chamados.
   ```python
   from typing import Callable

   def execute(func: Callable[[int, int], int], x: int, y: int) -> int:
       return func(x, y)
   ```

### Generics

Os generics permitem criar funções e classes que podem trabalhar com qualquer tipo de dado.
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content

box = Box 
print(box.get_content())  # Saída: 123
```

### Benefícios do Typing

- **Melhoria da Documentação**: O código se torna mais autodocumentado.
- **Detecção Precoce de Erros**: Ferramentas como mypy podem ser usadas para verificar tipos estaticamente.
- **Autocompletar em IDEs**: Melhora a experiência de desenvolvimento ao fornecer sugestões mais precisas.

### Ferramentas

- **mypy**: Um verificador de tipos estáticos para Python.
  ```bash
  mypy script.py
  ```

- **pyright**: Um verificador de tipos estáticos da Microsoft, também utilizado no VS Code.

### Considerações Finais

O typing em Python é uma adição poderosa que, embora opcional, pode trazer grandes benefícios para o desenvolvimento de software, especialmente em projetos grandes e colaborativos. Ao utilizar anotação de tipos, os desenvolvedores podem escrever código mais robusto, legível e menos propenso a erros.
