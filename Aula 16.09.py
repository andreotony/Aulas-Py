class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"O motor {self.tipo} está ligado")

    def desligar(self):
        print(f"O motor {self.tipo} está desligado")

class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)

    def ligar_carro(self):
        print(f"O carro {self.marca}, {self.modelo} está ligado.")
        self.motor.ligar()

    def desligar_carro(self):
        print(f"O carro {self.marca}, {self.modelo} está desligado.")
        self.motor.desligar()

a1 = input("Digite a marca: ")
b1 = input("Digite o modelo: ")
c1 = input("Digite o motor: ")
carro = Carro(a1, b1, c1)
carro.ligar_carro()
carro.desligar_carro()

