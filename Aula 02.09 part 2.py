class Pessoa:
    def __init__(self, pnome, unome):
        self.primeironome = pnome
        self.ultimonome = unome

    def minhaFuncao(self):
        print(self.primeironome, self.ultimonome)

class Estudante(Pessoa):
    def __init__(self, pnome, unome, meiaPassagem, escola, anograduacao):
        super().__init__(pnome, unome)
        self.meiaPassagem = meiaPassagem
        self.escola = escola
        self.anograduacao = anograduacao
    def funcao2(self):
        print(f"Meia passagem: {self.meiaPassagem}\nNome da IE: {self.escola}\nAno de graduação: {self.anograduacao}")

        
p1 = Estudante("André", "Santos", "Sim", "Softex", 2017)
p1.minhaFuncao()
p1.funcao2()