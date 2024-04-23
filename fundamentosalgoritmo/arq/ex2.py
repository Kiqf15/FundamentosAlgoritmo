def somatoria(lista):
    soma = 0
    for elemento in lista:
        soma += int(elemento)
    return soma

a = open('numeros2.txt', 'r')
lista = a.readlines()
a.close()
numeros_separados = lista[0].split()
print(somatoria(numeros_separados))
