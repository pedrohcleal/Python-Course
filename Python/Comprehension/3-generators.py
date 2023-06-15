generator = ( i ** 2 for i in range(10) if i % 2 ==0)

print(next(generator)) #saida0
print(next(generator)) #saida4
print(next(generator)) #saida 16
print(next(generator)) #saida 26
print(next(generator)) #saida 64
#print(next(generator)) #erro!

