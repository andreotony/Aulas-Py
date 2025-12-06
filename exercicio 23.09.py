class Carro:
    def __init__(self):
        self.ligado = True

    def ligar(self):
        print("O carro está ligado")

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.motor = Carro()
    def partida(self):
        print(f"{self.nome} deu partida!")
        self.motor.ligar()

veiculo = Motor("Motor V8")
veiculo.partida()

print("\n -----------------\n")

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def formacao(self):
        print(f"Professor {self.nome}, está apto a dar aulas.")

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def mostrar_professores(self):
        print(f"Professores da Universidade {self.nome}:")
        for x in self.professores:
            print("-", x.nome)

prof_A = Professor("Caio Falcão")

universidade_A = Universidade("IFMA - Barreirinhas")

universidade_A.adicionar_professor(prof_A)

universidade_A.mostrar_professores()
prof_A.formacao()

print("\n -----------------\n")

class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, num_pag, autor):
        self.titulo = titulo
        self.num_pag = num_pag
        self.autor = autor

    def mostrar_obras(self):
        print(f"--{self.titulo}--")
        print(f"Numero de páginas: {self.num_pag}")
        print(f"Autor: {self.autor.nome}")

escritor = Autor("Calos Almada")

livro1 = Livro("Harmonia Funcional", 365, escritor)

livro1.mostrar_obras()




