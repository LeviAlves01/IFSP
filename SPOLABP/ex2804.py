class Produto:
    def __init__(self, nome, preco, quantidade_inicial):
        self.nome = nome
        self.preco = preco
        self.__quantidade = quantidade_inicial

    def calcular_valortotal(self):
        return self.preco * self.__quantidade
    
    def atualizar_quantidade(self, valor):
        if valor >= 0:
            self.__quantidade = valor
            self.preco = self.preco * self.__quantidade
            print(f"{valor} produtos foram adicionados. A nova quantidade de produtos é: {self.__quantidade} e o novo preço é: R${self.preco}")
        else:
            print("Digite um valor válido")

    def get_quantidade(self):
        return self.__quantidade
    
    def get_preco(self):
        return self.__preco
    
tenis = Produto("Tenis", 50, 1)
anel = Produto("Anel", 10, 2)
celular = Produto("Celular", 500, 3)

print(tenis.calcular_valortotal())
print(tenis.atualizar_quantidade(2))

print(anel.calcular_valortotal())
print(anel.atualizar_quantidade(4))

print(celular.calcular_valortotal())
print(celular.atualizar_quantidade(5))