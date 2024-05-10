import string

example0 = 'hellowordling'
#example2= 'codewars'
key = 'passwordpassword'

dictalpha = {key: value for key, value in zip(string.ascii_lowercase,range(0,26))}
dictkeys = {}

for let in key:
    dictkeys[let] = dictalpha.get(let)
    finalstr = ''

for i in range(len(example0)):
    dictkeys[example0[i]]

print(dictkeys)