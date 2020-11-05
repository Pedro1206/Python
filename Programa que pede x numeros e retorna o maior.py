qtd = 5
maior = 0

for x in range(qtd):
    n = int(input("Digite um número:"))
    if n > maior or x == 0:
        maior = n
print(maior)
