print("Bem-vindo a Bistrô do Levi. \n Vamos iniciar o seu pedido.")

class ItemCardapio:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibir_detalhes(self):
        print(f"{self.nome} - {self.descricao} - {self.preco}")

    def get_preco(self):
        return self.preco
    
    def get_nome(self):
        return self.nome
    
    def get_descricao(self):
        return self.descricao

class Cliente:
    def __init__(self, nomec, telefone):
        self.nomec = nomec
        self.telefone = telefone

    def get_nomec(self):
        return self.nomec
    
    def get_telefone(self):
        return self.telefone
    

class Pedido(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco, descricao)

    def adicionar_item(self, ItemCardapio, ItensPedido, valortotal):
        self.ItensPedido = [ItensPedido+ItemCardapio]
        self.valortotal = valortotal + self.preco
        
        
        for i in range(ItensPedido):
            self.valortotal = valortotal + self.preco
            i = 0
            
    

    def calcular_total(self, ItensPedido, total):
        self.ItensPedido = ItensPedido
        self.total = total
        
        
cardapio_lanchonete = []
xBurguer = ItemCardapio("XBurguer", "Hamburguer daora", 80.56)



