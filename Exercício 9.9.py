#Questão 1#

class Animal:
    def falar(self):
        print("Som de animal")

class Cachorro:
    def falar(self):
        print("Au, au!")

class Gato:
    def falar(self):
        print("Miau!")

animais_lista = [Cachorro(), Gato()]
for animal in animais_lista:
    animal.falar()

#Questão 2#

class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        print("a área do quadrado é: ", self.lado * self.lado)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio    
    def area(self):
        print("a area é do cículo é: ", 3.14 * self.raio ** 2)

forma1 = Quadrado(2)
forma2 = Circulo(1)

for x in (forma1, forma2):
    x.area()

#Questão 3#

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def salario():
        pass

class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def salario(self):
        print("Salário de Gerente = R$ 5000,00")

class Estagiario(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def salario(self):
        print("Salário de Estagiário = R$ 1500,00")

funcionarios = [Estagiario("André"), Gerente("Carlos Ronaldo")]

for pessoa in funcionarios:
    pessoa.salario()

#Questão 4#

class Veículo:
    def mover(self):
        pass

class Carro(Veículo):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("Dirigindo...")

class Bicicleta(Veículo):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("Pedalando...")

class Aviao(Veículo):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("Voando...")

veiculos = [Carro(), Bicicleta(), Aviao()]

for x in veiculos:
    x.mover()