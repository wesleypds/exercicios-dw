def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Digite um número: "))

for i in range(1, n+1):
    print(f"O fatorial de {i} é {fatorial(i)}")
