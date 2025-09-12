class ItemCardapio():
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def getnome(self):
        return self.nome
    
    def setnome(self, novo_nome):
        self.nome = novo_nome

    def getdesc(self):
        return self.descricao

    def setdesc(self, nova_desc):
        self.descricao = nova_desc

    def getpreco(self):
        return self.preco

    def setpreco(self, novo_preco):
        self.preco = novo_preco
    
    def exibir_detalhes(self):
        print(f'{self.getnome()} - {self.getpreco()} - {self.getdesc()}')

class Cliente():
    def __init__(self, nomec, telefone):
        self.nomec = nomec
        self.telefone = telefone
    
    def exibir_detalhesC(self):
        print(f'{self.nomec} - {self.telefone}')

class Pedido():
    def __init__(self, cliente, status="Em Aberto."):
        self.cliente = cliente
        self.itens_pedido = [] 
        self.status = status

    def adicionar_item(self, item):
        self.itens_pedido.append(item)
        print(f"Item {item.getnome()} adicionado ao pedido.")

    def calcular_total(self):
        total = 0
        for item in self.itens_pedido:
            total = total + item.getpreco()
        return total

    def exibir_resumo(self):
        print("Informacoes do Cliente:")
        print("")
        self.cliente.exibir_detalhesC()
        print("")
        print("itens no pedido:")
        print("------------------")
        for item in self.itens_pedido:
            print(f"Item: {item.getnome()} - Preco: R$ {item.getpreco()} - Descricao: {item.getdesc()}") 
        print("------------------")
        print(f"Valor total do pedido: R$ {self.calcular_total():.2f}")
        print("------------------")
        print(f"Status do pedido: {self.status}\n")

    def finalizar_pedido(self):
        self.status = "Finalizado"

cliente1 = Cliente("lucs", "11111111111")
item1 = ItemCardapio("X-Burguer", 17.51, "Pao, carne e queijo.")
item2 = ItemCardapio("Batata Frita", 8.50, "Batatas fritas ao oleo.")
item3 = ItemCardapio("Coca Cola Latinha", 999.50, "Refrigerante sabor noz de cola. Contem 350ml")

pedido1 = Pedido(cliente1)

pedido1.adicionar_item(item1)
pedido1.adicionar_item(item2)
pedido1.adicionar_item(item3)

pedido1.exibir_resumo()

finalizar = int(input("Pressione 1 para finalizar o pedido: "))
print("------------------")
if finalizar == 1:
    pedido1.finalizar_pedido()
    print("\nPedido Finalizado, imprimindo recibo:\n")
    print("------------------")
    print("Resumo do Pedido:")
    print("")
    pedido1.exibir_resumo()