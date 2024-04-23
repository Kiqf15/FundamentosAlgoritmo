x = int(input("Digite o código do produto: \n"))

y = int(input("Digite a quantidade do produto: \n"))

total = 0

if x == 1:
    total = 6*y
elif x == 2:
    total = 6.50*y
elif x == 3:
    total = 5*y
elif x == 4:
    total = 3*y
elif x == 5:
    total = 2*y

print ("Total: R$ {0:.2f}".format(total))