class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R${} realizado com sucesso.".format(valor))

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque de R${} realizado com sucesso.".format(valor))

conta = ContaBancaria()

conta.depositar(100)
try:
    conta.sacar(150)
except SaldoInsuficienteError as e:
    print(e)
