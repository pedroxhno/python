# Dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor.
# Utilize as funções min() e max()

from random import randint

tot = 100
vet = []

for i in range(tot):
    vet.append(randint(0, 1000))
print(f'o maior elemento é {max(vet)}')
print(f'o menor elemento é {min(vet)}')