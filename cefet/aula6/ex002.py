# Faça um programa que preencha por leitura um vetor de 10
# posições, e conta quantos valores diferentes existem no vetor.

tot = 10
lista = []

for i in range(tot):
    lista.append(int(input('digite um numero: ')))
lista_unicos = []

for num in range(len(lista)):
    if lista[num] not in lista_unicos:
        lista_unicos.append(lista[num])
print(lista)
print(lista_unicos)
