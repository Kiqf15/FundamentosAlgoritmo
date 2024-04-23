def minimo(x,y):
  if x < y:
    return y
  else:
    return x

def maximo(x, y):
  if x > y:
    return y
  else:
    return x

def multiplo(x, y):
  return(x%y==0)


print(minimo(1, 2))
print(maximo(1, 2))
print(multiplo(2, 2))