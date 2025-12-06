lista = []

print("Digite 5 números ou 'sair' para finalizar")

for i in range (5):
    valor = input(f"{i + 1}º número: ")

    if valor == "sair":
        print("Programa finalizado")
        exit()

    lista.append(int(valor))

soma = 0

for num in lista:
    soma += num

maior = lista[0]
menor = lista [0]

for num in lista:
    if num > maior:
        maior = num
    elif num < num:
        menor = num

print(f"Soma: {soma}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")