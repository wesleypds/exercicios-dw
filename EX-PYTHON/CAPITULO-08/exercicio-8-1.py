class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)

pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
