A = {}
A = set()

def CalculaPar(n):
    if n%2 == 0:
        A.add(n)
    else:
        print("Somente inteiros")

while True:
    n = int(input("diga um número inteiro:"))
    Par = CalculaPar(n)
    print(A)
