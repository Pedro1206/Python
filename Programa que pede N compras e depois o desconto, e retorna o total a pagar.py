print("Informe os valores das compras e a % de desconto no final")
print("Digite fim para indicar o final das compras")

compras = []
n = 0

while True:
    n = input("compras:")
    if n == "f" or n == "fim":
        break
    else:
        compras.append(float(n))

porcentagem = float(input("Informe o desconto:"))

desconto = (sum(compras)/100)*porcentagem
total = sum(compras)-desconto
print(total)
