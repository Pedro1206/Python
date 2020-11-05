nome = str(input("Diga seu nome:"))
idade = int(input("Diga sua idade:"))

atual = 2020
data = []

def CalculaAno(data):
    ano = atual-idade
    if idade > 17:
        print(nome, " é maior de idade e nasceu em ", ano)
    else:
        print(nome, " é menor de idade e nasceu em ", ano)
CalculaAno(data)

