class Livro:
    def __init__(self, autor, ano, numDePag):
        self.autor = autor
        self.ano = ano
        self.numDePag = numDePag

book1 = Livro("Xxxx", "1991", "300")
print(book1.ano)
print(book1.autor)
print(book1.numDePag)

book2 = Livro("yyYY", "1983", 467)
print(book2.ano)
print(book2.autor)
print(book2.numDePag)

#---------------------#

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

p1 = Pessoa("João", 36)

print(p1)

