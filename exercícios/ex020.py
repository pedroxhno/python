import random

aluno1 = str(input('Digite um aluno: '))
aluno2 = str(input('Digite outro aluno: '))
aluno3 = str(input('Digite outro aluno: '))
aluno4 = str(input('Digite outro aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print(f'a ordem será: {lista}')