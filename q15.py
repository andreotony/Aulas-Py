def conta_maiusculas(texto):
    contador = 0

    for letra in texto:
        if letra.isupper():
            contador += 1

    print(f"O texto contém {contador} letras maiúsculas.")

    print("O texto contém {} letras maiúsculas.".format(contador))

    return contador

frase = input("Digite um texto: \n")
resultado = conta_maiusculas(frase)

print("\nRetorno da função:", resultado)
