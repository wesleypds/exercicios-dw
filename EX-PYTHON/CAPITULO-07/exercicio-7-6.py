import os

with open('arquivo.txt', 'w'):
    pass

import shutil

nome_arquivo = input("Digite o nome do arquivo que você deseja copiar: ")

novo_nome_arquivo = nome_arquivo.rsplit('.', 1)[0] + '.cópia'

try:
    shutil.copy(nome_arquivo, novo_nome_arquivo)
    print("Arquivo copiado com sucesso. O novo arquivo é chamado '{}'.".format(novo_nome_arquivo))
except FileNotFoundError:
    print("Arquivo não encontrado. Por favor, verifique o nome do arquivo e tente novamente.")

