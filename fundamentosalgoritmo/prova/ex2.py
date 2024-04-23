A1=9
B1=8
C1=1

if (A1==B1) or (A1%2==0):
    C1=0
elif (A1<B1) and (C1>0):
    C1 = 1
elif (A1>B1) or (A1%2==0):
    C1=2
elif (A1<B1) and (A1%2==0):
    C1=3
elif (A1<B1) and (B1%2==0):
    C1=4
elif (A1<B1):
    C1=5
elif (A1>B1):
    C1=6
else:
    C1=7

print(C1)