#exercicio

def soma_lista(list1,list2):
    intervalo = min(len(list1), len(list2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]


l1 = [1,2,3,4]
l2= [3,4,5,6,7]

print(soma_lista(l1,l2))