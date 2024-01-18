def solution(args):

    for x in args:
        print(x)
    # your code here


print(solution([-3,-2,-1,2,10,15,16,18,19,20])) #'-3--1,2,10,15,16,18-20'



"""DESAFIO:
Dada uma lista de números inteiros em ordem crescente, o objetivo é criar uma função que retorne uma string formatada conforme as seguintes regras:

- Os números individuais devem ser separados por vírgulas.
- Os intervalos de números devem ser representados pelo primeiro e último número do intervalo, separados por um traço (-).
- Um intervalo é considerado válido apenas se abranger pelo menos 3 números.

Exemplo:

```python
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# retorna "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```

Para resolver o desafio, é necessário implementar a função "solution" que recebe a lista de inteiros em ordem crescente e retorna a string formatada conforme as regras mencionadas."""