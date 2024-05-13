alunos = {}
for _ in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

notas_arredondadas = {nome: round(nota) for nome, nota in alunos.items()}

print(notas_arredondadas)
