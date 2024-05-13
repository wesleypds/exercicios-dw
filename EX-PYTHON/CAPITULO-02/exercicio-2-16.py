peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso normal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
