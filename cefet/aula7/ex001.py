# Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da
# matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

matriz = []
k = 5

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'numero [{i}{j}]: ')))
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])

# a00 a01 a02
# a10 a11 a22
# a20 a21 a22

for i in range(3):
    matriz[i][i] *= k

for i in range(len(matriz)):
    print(matriz[i])