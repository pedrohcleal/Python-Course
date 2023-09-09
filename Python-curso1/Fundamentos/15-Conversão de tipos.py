print(2 + 3)
print('2' + '3')  #concatenção = 23 e não 2 + 3(=5)
#print(2 + '3') erro em console
a = 2
b = '3'
c = 'abc'
print(type(a))
print(type(b))
print(type(c))

print('a + b =', a + int(b))  #a string tem q estar previavemente estabelecida
print(type(b))

print(a + int(c)) #nao tem como converter abc em inteiro, erro mostrado em console