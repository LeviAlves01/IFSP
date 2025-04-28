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

nome = str(input("Digite o nome do funcionário: "))
funcao = str(input("Digite o cargo do funcionário: "))
salario_base = float(input("Digite o salário base do funcionário: R$"))

funcionario(nome, salario_base)

if (funcao=="gerente"):
    bonus = float(input("Digite seu bônus: R$"))
    gerente = gerente(nome, salariobase, bonus)
    gerente.calcular_salario()