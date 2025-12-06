maior_numero = None
for i in range(5):
    numero = int(input("Digite um numero: "))
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
    print(maior_numero)