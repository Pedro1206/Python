n = 1
qtde = 0
soma = 0
media = 0
num = 0

while n != 0:
    num = int(input("Informe um número:\n"))
    soma += num
    qtde += 1
    n = int(input("Digite zero caso queira encerrar o programa..."))
media = soma/qtde
print("Foram informados",qtde, "números e a média", media)
