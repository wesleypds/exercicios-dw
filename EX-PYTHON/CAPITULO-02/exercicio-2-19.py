import random

numero_aleatorio = random.randint(1, 10)

palpite = int(input("Tente adivinhar o número que eu gerei, entre 1 e 10: "))

if palpite == numero_aleatorio:
    print("Parabéns! Você acertou.")
else:
    if palpite > numero_aleatorio:
        print("O número que você digitou é maior do que o número que eu gerei.")
    else:
        print("O número que você digitou é menor do que o número que eu gerei.")
