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
