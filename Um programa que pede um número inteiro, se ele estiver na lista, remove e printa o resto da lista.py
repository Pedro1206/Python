n = int(input("Digite um número inteiro:"))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if n in lista:
    lista.remove(n)
    print(lista)
else:
    print(n, " não está na lista")
