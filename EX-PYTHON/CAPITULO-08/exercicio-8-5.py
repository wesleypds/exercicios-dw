class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Este animal faz um som genérico.")

animal = Animal("Bobby", 5)

animal.emitir_som()
