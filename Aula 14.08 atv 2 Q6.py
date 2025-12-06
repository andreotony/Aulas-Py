idade = int(input("Digite sua idade:\n"))
if idade >= 18:
    habilitacao = (input("tem habilitação(sim/não)\n"))
    if habilitacao == "sim":
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("Menor de idade")