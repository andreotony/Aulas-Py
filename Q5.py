while True:
    def calcular(x, y):
        soma = x+y
        sub = x-y
        mult = x*y
        div = x/y
        return soma, sub, mult, div
    x = input("Digite o primeiro número: ")
    y = input("Digite o segundo número: ")

    x = float(x)
    y = float(y)

    soma, sub, mult, div = calcular(x, y)

    print(f"A soma desses números é: {soma}")
    print(f"A subtração desses números é: {sub}")
    print(f"A multiplicação desses números é: {mult}")
    print(f"A divisão desses números é: {div}")
 



    comando = input("Digite 'sair' para encerrar ou tecle 'enter' para reiniciar: ")
    if comando.lower() == "sair":
        break