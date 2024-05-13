def contagemRegressiva(n):
    if n >= 0:
        print(n)
        contagemRegressiva(n - 1)
    else:
        print("Contagem regressiva finalizada!")

contagemRegressiva(5)
