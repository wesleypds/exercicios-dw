soma = 0
contagem = 0

while True:
    numero = float(input("Digite um número positivo (ou um número negativo para parar): "))

    if numero < 0:
        break

    soma += numero
    contagem += 1

if contagem > 0:
    media = soma / contagem
    print(f"A média dos números positivos digitados é {media}.")
else:
    print("Nenhum número positivo foi digitado.")
