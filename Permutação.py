n = int(input("Digite o número :"))
k = int(input("Digite o valor:"))

import math

if n >= k:
    print(math.perm(n,k))
else:
    print("Por favor digite um valor aceitavel")
