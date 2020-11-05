print("Digite os valores para se obter a soma entre 1 e 50")
n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
l1 = 0
l2 = 50

if n1 > 0 and n2 > 0 and n1 <= 50 and n2 <= 50:
    print(n1+n2)
else:
    print("Por favor digitar um valor entre 1 e 50")
