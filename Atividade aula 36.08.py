soma = 0
numero = int(input("Digite um numero ou digite 0 para sair\n"))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro numero"))

print(soma)