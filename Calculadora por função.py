a = int(input("1 valor:"))
b = int(input("2 valor:"))

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def subtrai(self):
        return  self.a - self.b
    def multiplica(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

c = Calculadora(a, b)

print('Soma: ', c.soma())
print('Subtração: ', c.subtrai())
print('Multiplicação: ', c.multiplica())
print('Divisão ', c.divide())
