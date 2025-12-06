class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Dirigir")
    
class Carro(Veiculo):
    pass

class Barco(Veiculo):
    def mover(self):
        print("Velejar!")

class Aviao(Veiculo):
    def mover(self):
        print("Voar!")


carro1 = Carro("Toyota", "Corolla")
barco1 = Barco("Ibiza", "Touring 20")
aviao1 = Aviao("Boeing", "747")

for x in (carro1, barco1, aviao1):
    print(x.marca)
    print(x.modelo)
    x.mover()