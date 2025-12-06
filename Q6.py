lista = []

while True:

    nome = input("Digite um nome para guardar na lista ou 'sair' para encerrar: \n")
    if nome.lower() == "sair":
        break

    lista.append(nome)

print(f"Os nomes armazenados foram: {', '.join(lista)}")



