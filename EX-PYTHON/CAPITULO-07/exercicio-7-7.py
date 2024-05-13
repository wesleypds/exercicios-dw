import os

os.makedirs('temp', exist_ok=True)

with open('temp/temp.txt', 'w') as f:
    pass

print("Diretório 'temp' e arquivo 'temp.txt' criados com sucesso.")
