#Questão 1#
print("Questão 1")
class Carros:
    def __init__(self, marca, modelo):
       self.marca = marca
       self.modelo = modelo
    def carro(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")
    def dirigir(self):
        print("O carro está em movimento.")

carro_1 = Carros("Nissan", "Kicks")
carro_2 = Carros("Volkswagen", "Polo")
carro_1.carro()
carro_2.carro()

print("\n\n")
#Questão 2#
print("Questão 2")


class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dog(self):
        print(f"Au, au!\nMeu nome é {self.nome} e tenho {self.idade} anos")
    def aniniversario(self):
        print(f"Au, au. É o {self.nome} de novo, fiz aniversário agora eu tenho {1 + self.idade} anos.")

cachorro = Cachorro("Luffy", 2)
cachorro.dog()
print("\n\n")
#Questão 3#
print("Questão 3")

class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def livro(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}")

livro_1 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)
livro_2 = Livro("Broquéis", "Cruz e Sousa", 1893)
livro_3 = Livro("O Cortiço", "Aluísio Azevedo", 1890)

livro_1.livro()
livro_2.livro()
livro_3.livro()

print("\n\n")
#Questão 4#
print("Questão 4")

carro_1.dirigir()

print("\n\n")
#Questão 5#
print("Questão 5")

cachorro.aniniversario()

print("\n\n")
#Questão 6#
print("Questão 6")
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        print(f"Bem vindo {self.titular}, depósito realizado no valor de: {valor}R$")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado no valor de: {valor}, seu saldo atual é: {self.saldo}")
        
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Titular: {self.titular}\nSaldo: {self.saldo}")

conta = ContaBancaria("André")

deposito = int(input("Digite o valor a ser depositado: "))

conta.deposito(deposito)

saque = int(input("Digite o valor para saque: "))

conta.saque(saque)

conta.extrato()




        