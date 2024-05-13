import random

numero_secreto = random.randint(1, 10)

while True:
    try:
        palpite = int(input("Adivinhe um número entre 1 e 10: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número.")
            break
        else:
            print("Desculpe, tente novamente.")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")
