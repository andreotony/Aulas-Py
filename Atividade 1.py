#Aula 1 - Conversão de tipos
#Questão 1
num_String = "123"
num_Float = float(num_String)
print(num_String)
print(num_Float)

#Questão 2 - 
frase = "Python é incrível!"
num_Caracteres = len(frase)
print(num_Caracteres)
frase_Maiuscula = frase.upper()
print(frase_Maiuscula)
frase_Troca = frase.replace("incrível", "poderoso")
print(frase_Troca)

#Questão 3 - 
lista_Num = [10, 20, 30, 40, 50]
print(lista_Num[3])
lista_Num.append(60)
lista_Num.remove(20)
print(lista_Num)

#Questão 4 -
aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Engenharia"
}
aluno["notas"] = [8.5, 7.0, 9.2]
print(aluno["curso"])

#Questão 5
cores = ("vermelho", "verde", "azul", "verde")
conj_cores = set(cores)
conj_cores.add("amarelo")
print(conj_cores)

#Questão 6
a = 15
b = 4
print( a // b)
print( a % b)

#Questão 7
lista_Dados = [42, 3.14, "Python", True, [1, 2]]
for elemento in lista_Dados:
    print(elemento, type(lista_Dados))

#Questão 8
texto = "Programação"
print(texto[::-1])
print(texto == texto[::-1])

#Questão 9
lista_Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_Matriz[1] [1])
lista_Matriz[2][1] = 10
print(lista_Matriz)

#Questão 1o
estoque = {"maçã": 10, "banana": 5, "laranja": 8}
estoque["pêra"] = 12
estoque.pop("banana")
print(estoque.keys())
