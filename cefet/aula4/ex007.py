# Faça um programa que leia 100 números inteiros e diga qual é o menor. 

menor = 0

for i in range(1, 101):
    n = int(input('Digite um numero: '))
    if i==1:
        menor = n
    else: # i>=2
        if n < menor:
            menor = n

print(menor)