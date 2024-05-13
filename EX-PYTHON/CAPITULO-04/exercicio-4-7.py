import re

nome_usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

nome_usuario_limpo = re.sub(r'\W+', '', nome_usuario)
senha_limpa = re.sub(r'\W+', '', senha)

print(f"O nome de usuário processado é: {nome_usuario_limpo}")
print(f"A senha processada é: {senha_limpa}")
