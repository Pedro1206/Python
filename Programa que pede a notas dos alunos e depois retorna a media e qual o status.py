print("Informe as notas dos alunos entre 0 e 10")
print("Informe um número abaixo de 0 ou acima de 10 para parar")

n = 0
notas = []


def CalculaMedia(notas):
    media = sum(notas)/len(notas)
    if media >= 7:
        print(media," = aprovado")
    elif media <= 5:
        print(media, " = Reprovado")
    else:
        print(media, " = Recuperação")

while True:
    n = float(input("Notas:"))
    if n <= 10 and n >= 0:
        notas.append(n)
    else:
        break
CalculaMedia(notas)
