lista = []

import math

def Fatoralista(lista):
    print(math.factorial(lista[0]), ", ", math.factorial(lista[1]), ", ", math.factorial(lista[2]), ", ", math.factorial(lista[3]))

for i in range(4):
   n = int(input(":"))
   lista.append(n)

print("-----lista-----")
print(lista)
print("-----Fatoriais da lista------")
Fatoralista(lista)
