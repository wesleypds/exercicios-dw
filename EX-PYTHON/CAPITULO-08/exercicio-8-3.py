class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R${} realizado com sucesso.".format(valor))

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque de R${} realizado com sucesso.".format(valor))

    def exibir_saldo(self):
        print("O saldo da conta é R${}.".format(self.saldo))

conta = ContaBancaria()

conta.depositar(100)
conta.exibir_saldo()
conta.sacar(50)
conta.exibir_saldo()
