# O professor deseja dividir uma turma com N alunos em dois grupos: 
# um com M alunos e outro com (N-M) alunos. Faça o programa que lê o 
# valor de N e M e informa o número de combinações possívei
# – Número de combinações é igual a N!/(M! * (N-M)!)
# – Use funções para evitar repetição de código

from math import factorial

def calcular_combinacoes(n, m):
    num_combinacoes = factorial(n) / (factorial(m) * factorial((n - m)))
    return num_combinacoes

num_alunos = int(input('Digite o numero de alunos: '))

while True:
    grupo_um = int(input('Digite o numero de alunos de um grupo: '))
    if grupo_um > num_alunos:
        print('ERRO! numero maior que o numero de alunos')
    if grupo_um < num_alunos:
        break

grupo_dois = num_alunos - grupo_um
# grupo_dois <= grupo_um

if grupo_dois > grupo_um:
    print('ERRO')
else:
    print(grupo_um)
    print(grupo_dois)
    combinacoes = calcular_combinacoes(grupo_um, grupo_dois)
    print(combinacoes)

