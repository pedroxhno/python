# Faça um programa que leia um vetor vet de 20 números inteiros.
# O programa deve gerar, a partir do vetor lido, um outro vetor posque contenha apenas
# os valores inteiros positivos de vet.
# A partir do vetor pos, deve ser gerado um outro vetor semdup que contenha
# apenas uma ocorrência de cada valor de pos.

from random import randint

tot = 20
vet = []
pos = []
semdup = []

for i in range(tot):
    vet.append(randint(-10, 10))

for num in range(len(vet)):
    if vet[num] > 0:
        pos.append(vet[num])

for num in range(len(pos)):
    if pos[num] not in semdup:
        semdup.append(pos[num])

print(sorted(vet))
print(sorted(pos))
print(sorted(semdup))