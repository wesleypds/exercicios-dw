vinhos = [
    {"nome": "Vinho A", "preco": 45},
    {"nome": "Vinho B", "preco": 60},
    {"nome": "Vinho C", "preco": 30},
    {"nome": "Vinho D", "preco": 80},
    {"nome": "Vinho E", "preco": 55}
]

vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))

for vinho in vinhos_caros:
    print(f"{vinho['nome']}: R${vinho['preco']}")
