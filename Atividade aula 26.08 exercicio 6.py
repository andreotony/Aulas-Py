texto = input("Diginte um texto: ")
vogais = "aeiouAEIOU"

contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print("O numero de vogais e: ", contador)