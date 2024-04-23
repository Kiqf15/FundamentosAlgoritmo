x = 5
def f1():
    global x
    x = 4
def f2(a,b):
    global x
    return a+b+x
total = f2(1,2)
f1()
print(total)