print("Insira 5 números para se obter a soma e a média")

n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))
n4 = int(input("Digite o quarto número inteiro:"))
n5 = int(input("Digite o quinto número inteiro:"))

r1 = n1 + n2 + n3 + n4 + n5
r2 = r1/5

print("{} é a soma e {} é a média".format(r1, r2))
