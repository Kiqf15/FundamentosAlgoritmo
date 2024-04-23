n = int(input())
a=1
b=1
lista = [0, 1, 1]
if n==1:
    print('0')
elif n==2:
    print('0','1')
else:
    for i in range(n-3):
        total = a + b
        b = a
        a = total
        lista.append(total)
print(*lista)