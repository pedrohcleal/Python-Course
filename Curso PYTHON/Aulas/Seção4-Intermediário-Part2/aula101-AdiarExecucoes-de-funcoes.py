# Definindo a função 'soma' que retorna a soma de dois valores x e y
def soma(x, y):
    return x + y

# Definindo a função 'multiplica' que retorna o produto de dois valores x e y
def multiplica(x, y):
    return x * y

# Definindo a função 'criar_funcao' que recebe uma função e um valor x como argumentos
def criar_funcao(funcao, x):
    # Definindo uma função interna chamada 'interna' que recebe um valor y como argumento
    def interna(y):
        # A função interna retorna o resultado da chamada da função passada como argumento (funcao) com os valores x e y
        return funcao(x, y)
    # Retornando a função interna criada
    return interna

# Criando uma nova função 'soma_com_cinco' usando a função 'criar_funcao' e a função 'soma', com x igual a 5
soma_com_cinco = criar_funcao(soma, 5)

# Criando uma nova função 'multiplica_por_dez' usando a função 'criar_funcao' e a função 'multiplica', com x igual a 10
multiplica_por_dez = criar_funcao(multiplica, 10)

# Chamando a função 'soma_com_cinco' com o argumento 10, que internamente chamará a função 'soma(5, 10)' e retornará o resultado
print(soma_com_cinco(10))

# Chamando a função 'multiplica_por_dez' com o argumento 10, que internamente chamará a função 'multiplica(10, 10)' e retornará o resultado
print(multiplica_por_dez(10))

"""
O código basicamente demonstra como criar funções adicionais a partir de funções existentes usando o conceito de fechamento (closure). 
A função criar_funcao cria e retorna uma função interna (interna) que "lembrará" o valor de x passado para ela ao ser chamada mais tarde.
Isso permite criar funções especializadas que utilizam um valor fixo x ao chamar funções mais genéricas, como soma e multiplica, com argumentos variáveis y.

Portanto, o resultado das chamadas soma_com_cinco(10) e multiplica_por_dez(10) será:

soma_com_cinco(10) resulta em soma(5, 10), que é igual a 15.
multiplica_por_dez(10) resulta em multiplica(10, 10), que é igual a 100.

Então, o output do código será:

15
100 

""""