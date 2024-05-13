frase = input("Digite uma frase: ")

palavras = frase.split()

palavras = [palavra.strip() for palavra in palavras]

frase_limpa = ' '.join(palavras)

print(f"A frase sem espaços em branco desnecessários é: {frase_limpa}")
