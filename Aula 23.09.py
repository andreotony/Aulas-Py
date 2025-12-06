class Professor:
    def __init__(self, nome):
        self.nome=nome

    def ministrar_aula(self):
            print(f"Professor(a) {self.nome} está dando aula.")

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = [] 

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def mostrar_professores(self):
        print(f"Professores da escola {self.nome}:")
        for prof in self.professores:
            print("-", prof.nome)

prof1 = Professor("Juliane")
prof2 = Professor("Carlos Ronaldo")

escola = Escola("IFMA - São José de Ribamar")

escola.adicionar_professor(prof1)
escola.adicionar_professor(prof2)

escola.mostrar_professores()
prof1.ministrar_aula()

print("\n -----------------\n")

class Coracao:
     def __init__(self):
        self.batendo = True

     def bater(self):
        if self.batendo:
             print("Tum-Tum...")

class Pessoa:
     def __init__(self, nome):
          self.nome = nome
          self.coracao = Coracao()

     def viver(self):
        print(f"{self.nome} está vivo!")
        self.coracao.bater()

p1 = Pessoa("Carlos Ronaldo")
p1.viver()

print("\n -----------------\n")

