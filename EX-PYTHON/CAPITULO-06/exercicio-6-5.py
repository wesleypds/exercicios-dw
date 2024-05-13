alunos = {}
for _ in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

alunos_aprovados = {nome: nota for nome, nota in alunos.items() if nota >= 7}

print(alunos_aprovados)
