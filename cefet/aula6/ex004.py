# Um dado é lançado 50 vezes, e o valor correspondente é
# armazenado em um vetor. Faça um programa que determine o
# percentual de ocorrências de face 6 do dado dentre esses 50
# lançamentos. Obs: utilize a função randint() para gerar os 50
# lançamentos do dados. randint(1,6) -> gera números inteiros
# aleatórios de 1 a 6. Insira no seu programa:

from random import randint

tot = 50
face_ocorrencia = 6
tot_ocorrencia = 0
vetor = []

for i in range(tot):
    vetor.append(randint(1, 6))

for num in range(len(vetor)):
    if vetor[num] == face_ocorrencia:
        tot_ocorrencia += 1
media = tot_ocorrencia / tot * 100
print(f'a porcentagem de ocorrências de faces {face_ocorrencia} é de {media:.2f}%')
