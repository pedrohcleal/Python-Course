def move_zeros(lst):
    for x in lst:
        if x == 0:
            lst.append(0)
            lst.remove(0)    
    
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) 
# returns [1, 1, 2, 1, 3, 0, 0]
