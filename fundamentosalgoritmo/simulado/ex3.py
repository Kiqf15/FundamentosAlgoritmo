lista = [0, -5, 10, 7, -8, 6, 14, 8, -2, 0, -1, 14]

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = -2 * lista[i]
    else:
        lista[i] += 1
print(lista)