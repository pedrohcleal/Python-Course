# se a soma dos dígitos na metade esquerda de seu número 
# fosse igual à soma dos dígitos na metade direita
import math

def luck_check(st):
    if st == '' or st.isdecimal() == False:
        raise("Invalid type value should throw error.")
    list_st = list(st)
    soma1 = 0
    soma2 = 0
    
    if len(st)%2 != 0:
        del list_st[math.floor(len(st)/2)]
        
    for x in range(len(list_st)):
        if x < int(len(list_st)/2):
            soma1 += int(list_st[x])
        else:
            soma2 += int(list_st[x])

    if soma1 == soma2:
        return True
    else:
        return False

print(luck_check('55555')) # true
print(luck_check('003111')) #true
print(luck_check('543970707')) #false
