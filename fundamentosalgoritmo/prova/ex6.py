from random import randint

p = input()

m = []

for i in range(12):
    linha = []
    for i in range(12):
        linha.append(randint(0,10))
    m.append(linha)


print("Matriz criada:")
for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    print('%3d' % m[linha][coluna], end=' ')
  print()

if p == "S":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) and (0<coluna<11):
                soma += m[linha][coluna]
            elif (linha == 1) and (1<coluna<10):
                soma += m[linha][coluna]
            elif (linha == 2) and (2<coluna<9):
                soma += m[linha][coluna]
            elif (linha == 3) and (3<coluna<8):
                soma += m[linha][coluna]
            elif (linha == 4) and (4<coluna<7):
                soma += m[linha][coluna]
            else:
                pass

    print(f"Resultado da conta: {soma}")

elif p== "M":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) and (0<coluna<11):
                soma += m[linha][coluna]
            elif (linha == 1) and (1<coluna<10):
                soma += m[linha][coluna]
            elif (linha == 2) and (2<coluna<9):
                soma += m[linha][coluna]
            elif (linha == 3) and (3<coluna<8):
                soma += m[linha][coluna]
            elif (linha == 4) and (4<coluna<7):
                soma += m[linha][coluna]
            else:
                pass
    
    media = soma/30
    media = round(media)
    print(f"Resultado da conta: {media}")