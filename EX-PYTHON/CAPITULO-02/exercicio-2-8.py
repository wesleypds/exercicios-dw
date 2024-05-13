data = input("Digite uma data no formato dd/mm/aaaa: ")

if len(data) == 10:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    if 1 <= dia <= 31 and 1 <= mes <= 12 and 1 <= ano <= 9999:
        print("A data está no formato correto.")
    else:
        print("A data não está no formato correto.")
else:
    print("A data não está no formato correto.")
