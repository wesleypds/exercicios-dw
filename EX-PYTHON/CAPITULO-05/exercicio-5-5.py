def minha_funcao():
    x = 10
    print(f"O valor de x dentro da função é {x}.")

minha_funcao()

try:
    print(f"O valor de x fora da função é {x}.")
except NameError:
    print("Erro: a variável x não está definida fora da função.")
