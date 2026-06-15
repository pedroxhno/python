# Faça um programa que mostre a tabuada de 1 até 10 de um número inteiro lido do teclado. 

n = int(input('Digite n: '))
for i in range(1, 11):
    print(f'{i} x {n} = {i*n}')
