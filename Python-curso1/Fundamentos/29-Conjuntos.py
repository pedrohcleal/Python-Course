#conjuntos
a = {1,2,3}
print(type(a))
a = set('coder') #*set* conjuntos de caracteres em ordem aleatória "'c','r','o','e',d'"
print(a)

print('3' in  a, 4 not in a) #
print({1,2,3} == {3,2,1,3})

c1 = {1,2}
c2 = {2,3}
print(c1.union(c2))  #uniao
print(c1.intersection(c2)) #intersecção

c1.update(c2) #adicionou o c2 ao c1
print(c1)

print(c2 <= c1) #c2 é subconjunto de c1 ?
print(c1 >= c2) #c1 é superconjunto de c2?
print({1,2,3} - {2})
c1 -= {3} #remove e atualiza c1
print(c1)


