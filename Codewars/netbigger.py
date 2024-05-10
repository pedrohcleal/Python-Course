def next_bigger(n):
    strn = list(str(n))
    print(n)
    for x in range(len(strn)-1,0, -1):
        strn[x] = str(n)[x-1] 
        strn[x-1] = str(n)[x]
        
        current = int(''.join(strn))
        print(current)
        if (current > n):
            if ()
            return current
    return -1

print(next_bigger(1234567890))
print('resultado deve ser =',1234567908)

