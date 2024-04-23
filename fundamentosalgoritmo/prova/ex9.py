A = 0
B = 0

for contador in range(2,7):
    if(A==2):
        A+=4
    else:
        A+=1
    
for contador in range(3,9):
    if(B==3):
        B+=3
    else:
        B+=2
while(A<4):
    if(B==4):
        B+=2
    else:
        B+=1
while(B<4):
    if(A==4):
        A+=2
    else:
        A+=1
print(A)
print(B)