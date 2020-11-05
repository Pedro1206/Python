n = int(input("Digite o número de elementos do conjunto:"))
k = int(input("Digite o valor da combinação:"))

import math

if n >= k:
    print(math.comb(n,k))
else:
    print("Por favor digite um valor aceitavel")
