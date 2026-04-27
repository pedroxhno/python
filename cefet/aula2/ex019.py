#Faça um programa que leia 3 nomes e os coloque em ordem
#alfabética.

nome1 = input('Digite o 1º nome: ')
nome2 = input('Digite o 2º nome: ')
nome3 = input('Digite o 3º nome: ')

# python já sabe comparar strings

if nome1 > nome2:
    nome1, nome2 = nome2, nome1
if nome1 > nome3:
    nome1, nome3 = nome3, nome1
if nome2 > nome3:
    nome2, nome3 = nome3, nome2

print(f'Ordem alfabética: {nome1}, {nome2}, {nome3}')