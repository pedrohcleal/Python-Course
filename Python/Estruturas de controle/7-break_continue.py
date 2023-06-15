for x in range(1,11):
    if x % 2 == 0:
        continue   ##interrompe aquela repetição e vai pra próxima(pulou os nº pares)
    print(x)

for x in range(1,11):
        if x == 5:  ##(termina até o 5 com o break)
            break
        print(x)

print('Fim!')