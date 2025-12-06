try:
    x = "Olá"
    print(x)
   

except NameError:
    print("A variavel nao esta definida")

except ZeroDivisionError:
    print("Divisão por zero")

except:
    print("Outra coisa deu errado")

else:
    print("Nada deu errado")

print("\n-----------\n")


try:
    f = open("demofile.txt", 'w')
    try:
        f.write("Lorem Ipsum")

    except:
        print("Algo deu errado ao gravar o arquivo")

    else:
        print("Gravação bem sucedida")

    finally:
        f.close()
    
except:
    print("Algo deu errado ao abrir o arquivo")



print("\n-----------\n")
'''
class Abaixodezeroexception(Exception):
    pass

x = -1

if x < 0:
    raise Abaixodezeroexception("Desculpe, não há numeros inteiros positivos menores que 0")

    
'''

x = "Olá!"

if not type(x) is int:
    raise TypeError("Somente numeros inteiros são permitidos!")