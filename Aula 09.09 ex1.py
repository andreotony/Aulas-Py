class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Dirigir!")

class Barco:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Velejar!")

class Aviao:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Voar!")

carro1 = Carro("Ford", "Mustang")
barco1 = Barco("Ibiza", "Touring 20")
aviao1 = Aviao("Boeing", "747")

for x in (carro1, barco1, aviao1):
    x.mover()