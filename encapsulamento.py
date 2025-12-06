
# 1. Classe ContaBancaria
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saque inválido.")

    def ver_saldo(self):
        return self.__saldo



# 2.atributo protegido

class Pessoa:
    def __init__(self, nome, anoNasceu):
        self.nome = nome
        self._anoNasceu = anoNasceu   # atributo protegido (por convenção)


# 3. @property

class ContaBancariaComProperty:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo!")


# 4. @property e setter

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome    # somente leitura

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("O preço não pode ser negativo.")

