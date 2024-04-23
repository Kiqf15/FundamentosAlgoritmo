from random import randint, uniform

int = []
reais = []

for i in range(10):
    int.append( randint(0,50))

for i in range(15):
    reais.append( round(uniform(0,50)))

str = ['oi', 'como', 'voce', 'ta', '?']
complex = [2+3j, -3+2j, 7j, 9-5j, 8+1j]

completa = [int, reais, str, complex]

int = []
reais = []
str = []
complex = []



for i in range(50):
    completa[0].append(randint(0,100))


print(completa)