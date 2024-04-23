n = int(input("Digite o valor de N:"))
menor = 100
pos = 0

lista = []
for i in range(1,n+1):
    a = int(input("Digite o %i valor de X:" %(i)))
    lista.append(a)

for i in range(len(lista)):
  if lista[i] < menor:
    menor = lista[i]
    pos = i
print('Menor valor:', menor)
print('Posicao:', pos)