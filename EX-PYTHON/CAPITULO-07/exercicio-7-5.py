import os

with open('arquivo_vazio.txt', 'w'):
    pass

nome_arquivo = input("Digite o nome do arquivo que você deseja excluir: ")

try:
    os.remove(nome_arquivo)
    print("Arquivo excluído com sucesso.")
except FileNotFoundError:
    print("Arquivo não encontrado. Por favor, verifique o nome do arquivo e tente novamente.")
