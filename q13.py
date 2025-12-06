def operacao(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b

    print(f"A soma de a e b é: {soma}")
    print(f"A subtração de a e b é: {sub}")
    print(f"A multiplicação de a e b é: {mult}")
    print(f"A divisão de a e b é: {div}")

    return (soma, sub, mult, div)

a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))

resultado = operacao(a, b)
print(resultado)