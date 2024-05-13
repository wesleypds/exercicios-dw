class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        self.velocidade += 10 * segundos
        print("O carro acelerou por {} segundos e agora está a {} m/s.".format(segundos, self.velocidade))

    def frear(self, segundos):
        self.velocidade -= 5 * segundos
        self.velocidade = max(0, self.velocidade)
        print("O carro freou por {} segundos e agora está a {} m/s.".format(segundos, self.velocidade))

carro = Carro()

carro.acelerar(5)
carro.frear(3)
