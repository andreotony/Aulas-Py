def coletar_nomes():
    nomes = []

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome == "sair":
            break
        nomes.append(nome)

    print(f"\nVocê digitou {len(nomes)} nomes -> {nomes}")

    
    print("Você digitou {} nomes -> {}".format(len(nomes), nomes))

    return nomes


lista_nomes = coletar_nomes()
print("\nLista final:", lista_nomes)