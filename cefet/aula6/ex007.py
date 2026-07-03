# Dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor.
# NÃO utilize as funções min() e max()

from random import randint
max = 0
min = 0

tot = 100
vet = []

for i in range(tot):
    vet.append(randint(0, 1000))

# varre o vetor pra pegar o max e min
for num in range(len(vet)):
    if num == 1:
        max = vet[num]
        min = vet[num]
    else:
        if vet[num] > max:
            max = vet[num]
        if vet[num] < min:
            min = vet[num]

print(f'o maior elemento é {max}')
print(f'o menor elemento é {min}')