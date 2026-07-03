# Dado um vetor de 100 elementos, determine a diferença entre a soma dos elementos de índice par
# e a soma dos elementos de índice ímpar.

from random import randint

tot = 100
vet = []
soma_impares = 0
soma_pares = 0

for i in range(tot):
    vet.append(randint(0, 1000))

for i in range(0, len(vet), 2):
    soma_pares += vet[i]
for i in range(1, len(vet), 2):
    soma_pares += vet[i]
dif = soma_pares - soma_impares
print(f'a diferença entre a soma dos elementos de índice par e a soma dos elementos de índice ímpar é {dif}')