import math

a, b, c = 10,20.1,5.1
delta = ((b**2)-4*a*c)

if(delta < 0 or a == 0):
    print("Impossível de calcular!")
elif (delta == 0):
    r1 = (-b+delta ** (1/2))/(2*a)
    r2=r1
    print("R1= %.3f" %(r1))
    print("R2= %.3f" %(r2))
else:
    r1 = (-b + delta ** (1/2))/(2*a)
    r2 = (-b - delta ** (1/2))/(2*a)
    print("R1= %.3f" %(r1))
    print("R2= %.3f" %(r2))