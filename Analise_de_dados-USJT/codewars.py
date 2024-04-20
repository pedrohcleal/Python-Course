from decimal import Decimal


def sum_strings(x, y):
    results = ""
    contador = 0
    sumfinal = 0
    resto = 0

    maxi = max(x[::-1],y[::-1])
    mini = min(x[::-1],y[::-1])

    if x == "" and y == "":
        return "0"

    elif y == "":
        y = "0"

    elif x == "":
        x = "0"

    for i1 in maxi:
        print(contador)
        if contador >= len(mini):
            results = results + i1

        else:
            for i2 in range(contador,contador+1):
                soma = int(i1) + int(mini[i2]) + resto
                if soma > 9:
                    results = results + str(soma)[1]
                    resto += int(str(soma)[0])
                else:

                    results = results +str(soma)

                contador += 1

    return results


num1 = "129"
num2 = "43"
print(sum_strings(num1, num2))
