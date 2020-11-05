n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))
n4 = int(input("Digite o quarto número inteiro:"))
n5 = int(input("Digite o quinto número inteiro:"))
n6 = int(input("Digite o sexto número inteiro:"))
n7 = int(input("Digite o sétimo número inteiro:"))
n8 = int(input("Digite o oitavo número inteiro:"))
n9 = int(input("Digite o novo número inteiro:"))
n10 = int(input("Digite o décimo número inteiro:"))

x = 1

if ( n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 > 0):
    for x in ( n1, n2, n3, n4, n5, n6, n7, n8, n9, n10):
        if x%2 == 1:
            impar = x
        else:
            par = x
            print("{} é impar e {} é par".format(impar, par))
else:
    print("Por Favor digite um número inteiro")
