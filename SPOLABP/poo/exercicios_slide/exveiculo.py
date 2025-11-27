class Veiculo:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def exibir_detalhes(self):
        print(f"Nome: {self.nome} - Marca: {self.marca}")

class Carro(Veiculo):
    def __init__(self, nome, marca, num_portas):
        super().__init__(nome, marca)
        self.numero_portas = num_portas

    def exibir_detalhes(self):
        print(f"Nome: {self.nome} - Marca: {self.marca} - {self.numero_portas} portas")

class Moto(Veiculo):
    def __init__(self, nome, marca, cilindradas):
        super().__init__(nome, marca)
        self.cilindradas = cilindradas
    
    def exibir_detalhes(self):
        print(f"Nome: {self.nome} - Marca: {self.marca} - Cilindradas: {self.cilindradas}")

corolla = Carro("Corolla", "Toyota", 4)
mobi = Carro("Fiat", "Mobi", 4)
strada = Carro("Fiat", "Strada", 2)

cg = Moto("Honda", "CG", 162)
fazer = Moto("Yamaha", "Fazer", 249)
ninja = Moto("Kawasaki", "Ninja", 400)

corolla.exibir_detalhes()
mobi.exibir_detalhes()
strada.exibir_detalhes()
cg.exibir_detalhes()
fazer.exibir_detalhes()
ninja.exibir_detalhes()