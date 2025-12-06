def contador_vogais(texto):

    vogais = "aáàâãeéêiíoóôõuúAÁÀÂÃEÉÊIÍOÓÔÕUÚ"

    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1


    print(f"O numero de vogais no texto é: {contador}")

    return contador

textousuario = input("digite seu texto para contar as vogais: \n")
resultado = contador_vogais(textousuario)

