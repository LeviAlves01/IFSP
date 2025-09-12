class funcionario:
    def __init__(self, nome, salariobase):
        self.nome = nome
        self.salariobase = salariobase
    
    def calcular_salario(self):
        print(f"O funcionário {self.nome} receberá R${self.calcular_salario}")

class gerente(funcionario):
    def __init__(self, nome, salariobase, bonus):
        super().__init__(nome, salariobase)
        self.bonus = bonus
    
    def calcular_salario(self, salariobase, bonus):
        salario = salariobase + bonus
        print(f"O funcionário {self.nome} receberá R${salario}")

class vendedor(funcionario):
    def __init__(self, nome, salariobase, comissao, vendas):
        super().__init__(nome, salariobase)
        self.comissao = comissao
        self.vendas = vendas

    def calcular_salario(self, salariobase, comissao, vendas):
        salario = salariobase+comissao+vendas
        print(f"O funcionário {self.nome} receberá R${salario}")

class desenvolvedor(funcionario):
    def __init__(self, nome, salariobase, nivelexp):
        super().__init__(nome, salariobase)
        self.nivelexp = nivelexp

    def calcular_salario(self, salariobase, nivelexp):
        salario = salariobase+nivelexp
        print(f"O funcionário {self.nome} receberá R${salario}")

Joao = gerente("João", 1500, 50)
Maria = vendedor("Maria", 1700, 60, 700)
Luis = desenvolvedor("Luis", 1000, 10)

Joao.calcular_salario(1500, 50)
Maria.calcular_salario(1700, 60, 700)
Luis.calcular_salario(1000, 10)