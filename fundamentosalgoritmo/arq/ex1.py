pares = open("pares.txt", "w")

for i in range(1001):
    if i % 2 == 0:
        pares.write("%d\n" % i)
pares.close()

pares = open("pares.txt", "r")
num = pares.readlines()
print(num)
inverte = open("inverte.txt", "w")
for i in range(len(num) -1, -1, -1):
    inverte.write('%s' % num[i])
pares.close()