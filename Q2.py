notas = (7.5, 8.0, 5.0, 9.0, 6.5)

media = sum(notas) / len(notas)

print(f"Sua média é: {media}")

if media >= 9:
    print("Seu desempenho foi EXCELENTE")

if 7 <=  media < 9:
    print("Seu desempenho foi BOM")

if 5 <=  media < 7:
    print("Seu desempenho foi REGULAR")

if media < 5:
    print("Seu desempenho foi RUIM")

comando = input("Digite 'sair' para encerrar o programa: ")
if comando == "sair":
    exit()