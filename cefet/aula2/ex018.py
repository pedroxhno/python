#Faça um programa que leia 5 números e identifique o maior e o menor.

n1 = int(input('Digite o 1º número: '))
maior = n1
menor = n1

n2 = int(input('Digite o 2º número: '))
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

n3 = int(input('Digite o 3º número: '))
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

n4 = int(input('Digite o 4º número: '))
if n4 > maior:
    maior = n4
elif n4 < menor:
    menor = n4

n5 = int(input('Digite o 5º número: '))
if n5 > maior:
    maior = n5
elif n5 < menor:
    menor = n5

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')