""" A = [ [1,2,3],
      [4,5,6],
      [7,8,9] ]


for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        print(A[linha][coluna], end=' ')
    print()
 """
# -------------------------------------------------
""" 
M = []

for ind_linha in range(10):
    linha = []
    for ind_coluna in range(15):
        linha.append(ind_coluna + ind_linha)
    M.append(linha)

for linha in range(10):
    for coluna in range(15):
        print('%4d' % M[linha][coluna], end='')
    print() """
# ---------------------------------------------
""" 
from random import randint

M = []

for ind_linhas in range(10):
    linha = []
    for ind_col in range (15):
        linha.append(randint(0,100))
    M.append(linha)

for linha in range(10):
    for coluna in range(15):
        print('{0:4d}'. format(M[linha][coluna]), end='')
    print()

print()
for coluna in range(1):
    print(M[1][coluna], end='')
 """

# ------------------------------------------------

""" M = []
impar = []


for ind_linha in range(4):
    linha = []
    for ind_col in range(4):
        linha.append(int(input('Digite um número: ')))
    M.append(linha)

for linha in range(len(M)):
    soma = 0
    for coluna in range(len(M[linha])):
        print('{0:3d}'.format(M[linha][coluna]), end ='')
        if M[linha][coluna] % 2 != 0:
            soma += M[linha][coluna]
    impar.append(soma)
    print()
print()
print(impar) """

# ------------------------------------

""" M = []

for ind_linha in range(3):
    linha = []
    for ind_col in range(3):
        linha.append(int(input('Digite um valor: ')))
    M.append(linha)

soma = 0

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print('%3d' % M[linha][coluna], end='')
        
        if linha == coluna:
            soma += M[linha][coluna]
    print()

print(soma) """