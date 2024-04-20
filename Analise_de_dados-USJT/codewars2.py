def dir_reduc(arr):

    contador = 3

    listr = arr
    print(arr)

    for dir in range(0,len(arr)-1):
        print(dir)
        if dir == len(arr)-1:
            break
        print("__________")
        print(arr[dir])
        print(arr)
        if arr[dir] == "NORTH" and "SOUTH" in arr:
            arr.remove("NORTH")
            arr.remove("SOUTH")
            dir -= 1

        elif arr[dir] == "SOUTH" and "NORTH" in arr:
            arr.remove("NORTH")
            arr.remove("SOUTH")


        elif arr[dir] == "EAST" and "WEST" in arr:
            arr.remove("EAST")
            arr.remove("WEST")

        elif arr[dir] == "WEST" and "EAST" in arr:
            arr.remove("EAST")
            arr.remove("WEST")
        print(arr)

    return listr


l1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dir_reduc(l1))
print(['WEST'])