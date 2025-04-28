class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def get_saldo(self):
        return self._saldo
    
minhaconta = ContaBancaria(1000)

print(minhaconta.depositar(200))
print(minhaconta.sacar(500))