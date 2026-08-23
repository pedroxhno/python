# Faça um programa que leia duas matrizes A e B 2x2 e
# imprima a matriz C que é a soma das matrizes A e B.

matrizA = []
matrizB = []
matrizC = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f'numero [{i}][{j}]: ')))
    matrizA.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input(f'numero [{i}][{j}]: ')))
    matrizB.append(linha)

# matrizC soma
for i in range(2):
    linha_soma = []
    for j in range(2):
        soma = matrizA[i][j] + matrizB[i][j]
        linha_soma.append(soma)
    matrizC.append(linha_soma)

print("\nMatriz A:")
for linha in matrizA:
    print(linha)
print("\nMatriz B:")
for linha in matrizB:
    print(linha)
print("\nMatriz C (A + B):")
for linha in matrizC:
    print(linha)