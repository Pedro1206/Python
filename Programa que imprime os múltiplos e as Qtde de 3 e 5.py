multi3 = 0
multi5 = 0

for i in range(1,101):
    if (i % 3 == 0):
        print(i,"é múltiplo de 3", sep="->")
        multi3 += 1
    if (i % 5 == 0):
        print(i,"é multiplo de 5", sep="->")
        multi5 += 1
print("Qtde de múltiplos de 3: ", multi3)
print("Qtde de múltiplos de 5: ",multi5)
