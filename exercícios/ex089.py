alunos = []

while True:
    nome = input('Nome do aluno: ').capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2]])

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<15}{'MÉDIA':>6}')
print('-' * 30)

for i, aluno in enumerate(alunos):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{i:<4}{aluno[0]:<15}{media:>6.1f}')

print('-' * 30)

while True:
    idx = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if idx == 999:
        break
    if 0 <= idx < len(alunos):
        print(f'Notas de {alunos[idx][0]}: {alunos[idx][1]}')
    else:
        print('Aluno inválido.')
