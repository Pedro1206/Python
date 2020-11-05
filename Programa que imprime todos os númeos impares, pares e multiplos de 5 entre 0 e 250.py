multi5 = 0
x = 1
impar = 0
par = 0
contI = 0
contP = 0

for x in range(0, 250):
    if x%2 == 1:
        impar = x
        contI +=1
    if x%2 == 0:
        par = x
        contP +=1
        print("{} é impar e {} é par".format(impar, par))
    if x%5 == 0:
        print(x,"é multiplo de 5", sep="->")
        multi5 +=1
print("{} Qtd total de números impares e {} qtd total de números pares".format(contI, contP))
print("Qtde de múltiplos de 5: ", multi5)
