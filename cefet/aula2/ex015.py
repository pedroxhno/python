#Faça um programa que leia um número inteiro de 3 dígitos e
#informe se o algarismo da casa das centenas é par ou ímpar.

num = int(input('Digite um número inteiro de 3 algarismos: '))
num_centena = num // 100
if num_centena % 2 == 0:
    print(f'{num_centena} é par!')
else:
    print(f'{num_centena} é impar!')