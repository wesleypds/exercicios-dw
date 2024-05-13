import shutil

nome_diretorio = 'temp'

try:
    shutil.rmtree(nome_diretorio)
    print("Diretório '{}' excluído com sucesso.".format(nome_diretorio))
except FileNotFoundError:
    print("Diretório não encontrado. Por favor, verifique o nome do diretório e tente novamente.")
