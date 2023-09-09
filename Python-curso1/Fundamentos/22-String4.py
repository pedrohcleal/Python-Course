# %%
a = '123'
b = ' de Oliveira 4'
a + b
a.__add__(b)
str.__add__(a, b)

len(a)
a.__len__()
'1' in a
a.__contains__('1')

dir(str)