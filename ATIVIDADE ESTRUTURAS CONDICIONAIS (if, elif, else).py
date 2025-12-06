# 1. Peça um número e diga se ele é positivo.
num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
else:
    print("O número NÃO é positivo.")

# 2. Peça a idade e informe se é maior de idade ou menor de idade.
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

# 3. Nota: Aprovado, Recuperação ou Reprovado.
nota = float(input("Digite sua nota (0 a 10): "))
if nota >= 7:
    print("Aprovado.")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")

# 4. Número positivo, par e múltiplo de 5.
n = int(input("Digite um número: "))
if n > 0:
    print("É positivo.")
if n % 2 == 0:
    print("É par.")
if n % 5 == 0:
    print("É múltiplo de 5.")

# 5. Semáforo.
cor = input("Cor do semáforo (verde/amarelo/vermelho): ").lower()
if cor == "verde":
    print("Pode seguir.")
elif cor == "amarelo":
    print("Atenção.")
elif cor == "vermelho":
    print("Pare.")
else:
    print("Cor inválida.")

# 6. Pode dirigir?
idade = int(input("Digite sua idade: "))
if idade >= 18:
    habilitacao = input("Tem habilitação? (sim/não): ").lower()
    if habilitacao == "sim":
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Não pode dirigir.")

# 7. Par ou Ímpar em uma linha.
print("Par" if int(input("Digite um número: ")) % 2 == 0 else "Ímpar")

# 8. Número entre 10 e 20.
x = int(input("Digite um número: "))
if 10 <= x <= 20:
    print("Está entre 10 e 20.")
else:
    print("Não está entre 10 e 20.")

# 9. Maior de três números.
a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
print("Maior número:", max(a, b, c))

# 10. Usuário e senha.
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
