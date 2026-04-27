#Faça um programa que leia um número e diga se ele está
#compreendido entre 20 e 90 ou não.

n = float(input('Digite um número: '))
if 20 < n < 90:
    print(f'{n} está entre 20 e 90')
else:
    print(f'{n} não está entre 20 e 90')