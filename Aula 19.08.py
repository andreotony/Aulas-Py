for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finalmente terminei!")


adjetivos = ["vermelho", "lá ele", "saboroso"]
frutas = ["maçã", "banana", "morango"]
for x in adjetivos:
    for y in frutas:
        print(y, x)

def minha_funçao(primeiro_nome, segundo_nome):
    print(primeiro_nome, segundo_nome)

minha_funçao("André", "Ótony")
