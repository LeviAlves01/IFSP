class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som de animal")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("Au au!")
        
    def latir(self):
        print("Woof woof!")
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print("Miau!")

    def miar(self):
        print("Meow meow!")

c = Cachorro("Rex")
g = Gato("Mimi")

print(c.nome)
c.emitir_som()
c.latir()

print(g.nome)
g.emitir_som()
g.miar()