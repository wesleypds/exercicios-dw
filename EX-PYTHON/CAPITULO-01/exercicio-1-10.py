import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

D = B**2 - 4*A*C

if D > 0:
    raiz1 = (-B + math.sqrt(D)) / (2*A)
    raiz2 = (-B - math.sqrt(D)) / (2*A)
    print(f"As raízes da equação são {raiz1} e {raiz2}")
elif D == 0:
    raiz = -B / (2*A)
    print(f"A raiz da equação é {raiz}")
else:
    parte_real = -B / (2*A)
    parte_imaginaria = math.sqrt(-D) / (2*A)
    print(f"As raízes da equação são {parte_real} + {parte_imaginaria}i e {parte_real} - {parte_imaginaria}i")
