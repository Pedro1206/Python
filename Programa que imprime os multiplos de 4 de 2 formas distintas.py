ordem = str(input("Diga abaixo se vc quer um abaixo do outro ou ladose quer um lado a lado:"))


multi4 = 0

for i in range(1,101):
    if (i % 4 == 0):
        if ordem == "abaixo":
            print(i, "é múltiplo de 4", sep="->")
        elif ordem == "lado":
            print(i, ", ", end="")
        multi4 += 1
print("\nQtde de múltiplos de 4: ", multi4)
