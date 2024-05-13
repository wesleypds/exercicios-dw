cpf = input("Digite um número de CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("O CPF é válido.")
else:
    print("O CPF não é válido.")

