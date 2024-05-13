def calcular_media(lista_numeros):
    try:
        if not lista_numeros:
            print("Erro: A lista está vazia.")
            return

        soma = sum(lista_numeros)

        media = soma / len(lista_numeros)

        return media
    except TypeError:
        print("Erro: A lista contém valores não numéricos.")
    except Exception as e:
        print("Erro desconhecido:", str(e))

print(calcular_media([1, 2, 3, 4, 5]))
