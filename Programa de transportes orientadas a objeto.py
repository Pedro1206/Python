class transporte(object):
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo

class terrestre(transporte):
    def __int__(self, tipo, modelo):
        super().__init__(tipo, modelo)
    def cor(self):
        print("Cor = ", c)
    def ano(self):
        print("Ano= ", a)

class aquático(transporte):
    def __int__(self, tipo, modelo):
        super().__init__(tipo, modelo)
    def velocidade(self):
        print("Velocidade= ", v)
    def Lugares(self):
        print("Lugares= ", l)

 # variaveis mutaveis.
c = "azul"
a = 2020
v = "100KM/H"
l = 2

terrestre1 = terrestre("terrestre", 5421515)
aquático1 = aquático("aquatico", 554545)

n = str(input("Diga o tipo entre aguatico e terrestre:"))

if n == "terrestre":
    print("-------Terrestre------")
    print("Tipo= ", terrestre1.tipo)
    print("Modelo= ", terrestre1.modelo)
    terrestre1.cor()
    terrestre1.ano()
if n == "aquatico":
    print("--------Aquático-----")
    print("Tipo= ", aquático1.tipo)
    print("Modelo= ", aquático1.modelo)
    aquático1.velocidade()
    aquático1.Lugares()
