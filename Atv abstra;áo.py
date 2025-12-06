from abc import ABC, abstractmethod


class Pagamento(ABC):
    def processar_pagamento(self):
        pass

    def cancelar_pagamento(self):
        pass

class Cartao_de_credito(Pagamento):
    def processar_pagamento(self):
        return input("Você escolheu a opção Cartão de Crédito\nDigite o valor: ")

class PIX(Pagamento):
    def processar_pagamento(self):
        return input("Você escolheu a opção PIX\nDigite o valor: ")
    
class Boleto(Pagamento):
    def processar_pagamento(self):
        return input("Você escolheu a opção Boleto\nDigite o valor: ")

    
compra = Cartao_de_credito()
compra.processar_pagamento()