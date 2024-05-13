numeros = []
for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

numeros.sort()

segundo_menor = numeros[1]
segundo_maior = numeros[-2]

print(f"O segundo menor número é {segundo_menor}.")
print(f"O segundo maior número é {segundo_maior}.")
