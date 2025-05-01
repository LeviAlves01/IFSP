class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self._quantidade = quantidade

    def calcular_valor(self):
        print(f"A quantidade de {self.nome} é {self._quantidade} e o valor é: R${self.preco * self._quantidade}")
    
class Carrinho_de_compras(Produto):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco, quantidade)
    
    def adicionar_produtos(self, valor):
        if valor>0:
            self._quantidade = self._quantidade+valor
            self.preco = self._quantidade*self.preco
            print(f"{valor} produtos foram adicionados. A nova quantidade de produtos é: {self._quantidade} e o preço é: R${self.preco}")
        else:
            print("Forneça um valor válido.")

    def remover_produtos(self, valor):
        if valor>0:
            self._quantidade = self._quantidade-valor
            self.preco = self._quantidade*self.preco
            print(f"{valor} produtos foram removidos. A nova quantidade de produtos é: {valor} e o preço é: R${self.preco}")
        else:
            print("Forneça um valor válido.")

    def get_quantidade(self):
        return self._quantidade
    
    def get_preco(self):
        return self.preco

anel = Carrinho_de_compras("Anel", 10, 2)
fone = Carrinho_de_compras("Fone", 20, 4)

print(anel.calcular_valor())
print(anel.adicionar_produtos(3))

print(fone.calcular_valor())
print(fone.remover_produtos(2))