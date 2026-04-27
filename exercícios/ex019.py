import random

aluno1 = str(input('Digite um aluno: '))
aluno2 = str(input('Digite outro aluno: '))
aluno3 = str(input('Digite outro aluno: '))
aluno4 = str(input('Digite outro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'o aluno escolhido foi {random.choice(lista)}')