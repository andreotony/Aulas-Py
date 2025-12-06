from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    

Luffy = Cachorro()
Mimi = Gato()
Paçoca = Cachorro()
animais = [Luffy, Mimi, Paçoca]

for animal in animais:
    print(animal.emitir_som())