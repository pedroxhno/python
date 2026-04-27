#Faça um programa que leia dois valores A e B e em seguida efetue a troca dos valores de forma que
#a variável A passe a ter o valor da variável B e vice e versa.

a = 2
b = 3
print(f'ANTES {a}, {b}')
a, b = b, a
print(f'DEPOIS {a}, {b}')