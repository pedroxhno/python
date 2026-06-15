# Faça um programa que leia 100 números inteiros e diga quantos são ímpares

qtd_impares = 0

for i in range(1, 7):
    n = int(input('Digite um numero: '))
    if n%2 == 1:
        qtd_impares+=1

print(qtd_impares)