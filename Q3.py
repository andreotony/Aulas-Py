while True:
    aluno = {"Hyllorin": 8, "Thunder": 4, "Dorilda": 7}

    for nome, notas in aluno.items():
        if notas > 7:
            print(f"{nome}: aprovado(a)")
        else:
            print(f"{nome}: reprovado")

    comando = input("Digite 'sair' para encerrar: ")
    if comando == "sair":
        print("Programa encerrado.")
        break