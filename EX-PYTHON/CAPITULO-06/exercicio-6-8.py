numeros = input("Digite uma lista de números separados por espaço: ")

lista_numeros = list(map(int, numeros.split()))

lista_quadrados = list(map(lambda x: x**2, lista_numeros))

print("A lista de quadrados é:", lista_quadrados)
