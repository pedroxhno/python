# Dado um vetor com 20 elementos, gerar outro vetor que contenha somente números
# múltiplos de 3 encontrados no # primeiro vetor.

from random import randint

tot = 20
vet = []
vet_mult3 = []

for i in range(tot):
    vet.append(randint(0, 100))

for num in range(len(vet)):
    if vet[num] % 3 == 0:
        vet_mult3.append(vet[num])

print(sorted(vet))
print(sorted(vet_mult3))