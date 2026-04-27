#faça um programa que leia um número binário de 4 dígitos e diga
#quantos dígitos zero existem nesse número.

binario = input('Digite um número binário de 4 dígitos (ex: 1010): ')
zeros = 0

if binario[0] == '0':
    zeros += 1
if binario[1] == '0':
    zeros += 1
if binario[2] == '0':
    zeros += 1
if binario[3] == '0':
    zeros += 1

# c in range(0, 4):
#   if binario[c] == '0':
#       zeros += 1

print(f'O número {binario} possui {zeros} dígitos zero.')