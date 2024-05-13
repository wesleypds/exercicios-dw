def decifrar_mensagem(mensagem_codificada, mensagem_decodificada='', i=0):
    if i == len(mensagem_codificada):
        return mensagem_decodificada
    else:
        if mensagem_codificada[i].isalpha():
            if mensagem_codificada[i] == 'a':
                mensagem_decodificada += 'z'
            else:
                mensagem_decodificada += chr(ord(mensagem_codificada[i]) - 1)
        else:
            mensagem_decodificada += mensagem_codificada[i]
        return decifrar_mensagem(mensagem_codificada, mensagem_decodificada, i + 1)

mensagem_codificada = "b cbe"
mensagem_decodificada = decifrar_mensagem(mensagem_codificada)
print(f"A mensagem decodificada é: '{mensagem_decodificada}'")
