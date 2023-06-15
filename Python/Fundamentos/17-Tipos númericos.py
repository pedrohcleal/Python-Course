# %%
print(dir(int))
print(dir(float))

a = 5
b = 2.5
a / b
a + b
a * b

print(type(a))
print(type(b))
print(type(a - b))

print(b.is_integer())
print(5.0.is_integer())

print(dir(int))
print(int.__add__(2, 3))
print(2 + 3)

print((-2).__abs__())
print(abs(-2))

print((-3.6).__abs__())
print(dir(float))
print(abs(-3.6))