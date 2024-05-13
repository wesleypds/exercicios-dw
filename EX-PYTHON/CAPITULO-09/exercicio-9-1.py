num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

try:
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
