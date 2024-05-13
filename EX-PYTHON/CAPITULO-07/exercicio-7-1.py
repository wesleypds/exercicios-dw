nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Por favor, verifique o nome do arquivo e tente novamente.")
