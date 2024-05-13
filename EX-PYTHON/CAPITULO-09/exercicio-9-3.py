def calcular(operacao, num1, num2):
    try:
        if operacao == 'soma':
            return num1 + num2
        elif operacao == 'subtração':
            return num1 - num2
        elif operacao == 'multiplicação':
            return num1 * num2
        elif operacao == 'divisão':
            return num1 / num2
        else:
            print("Operação inválida.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception as e:
        print("Erro desconhecido:", str(e))

print(calcular('soma', 5, 3))
print(calcular('subtração', 5, 3))
print(calcular('multiplicação', 5, 3))
print(calcular('divisão', 5, 3))
print(calcular('divisão', 5, 0))
print(calcular('operação inválida', 5, 3))
