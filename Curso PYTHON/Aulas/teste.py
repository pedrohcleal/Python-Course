import string
def alphabet_position(text):
    abc = list(string.ascii_lowercase)
    um_24 = [x for x in range (1,25)]
    dict_numb = {}
    for x in abc:
        for y in um_24:
            dict_numb[(x)] = y
            y += 1
        continue
    print(dict_numb)



print(alphabet_position('abc'))