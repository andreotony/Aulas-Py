def resultado_alunos(alunos):
    resultado = {}
    for nome in alunos.items():
        if nota >= 7:
            resultado[nome] = "Aprovado"
        else:
            resultado[nome] = "Reprovado"

    for nome, status in resultado.items():
        print(f"O aluno {nome} esta {status}")