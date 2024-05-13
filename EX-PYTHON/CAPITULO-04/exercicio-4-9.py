import re

cpf = input("Digite um CPF no formato DDD.DDD.DDD-DD: ")

if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF não está no formato correto.")
