A = set()
B = []

def CalculaNum(n):
    if n%2 == 1:
        B.append(n)
    else:
        A.add(n)

while True:
    n = int(input(":"))
    CalculaNum(n)
    print("Pares: ", A)
    print("Impares: ", B)
