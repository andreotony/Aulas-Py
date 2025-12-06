while True:
    texto = input("Digite um texto: \n")

    vogais = "aáàâãeéêiíoóôõuúAÁÀÂÃEÉÊIÍOÓÔÕUÚ"

    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1
    print(f"O número de vogais no texto é: {contador}")

    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        break