#Faça um programa que leia 3 números diferentes e os imprima em
#ordem crescente e decrescente. Se houver números iguais exibir
#mensagem de erro.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 == n2 or n1 == n3 or n2 == n3:
    print('ERRO! Você digitou números iguais.')
else:
    if n1 > n2:
        n1, n2 = n2, n1

    if n1 > n3:
        n1, n3 = n3, n1

    if n2 > n3:
        n2, n3 = n3, n2

    print(f'Crescente: {n1}, {n2}, {n3}')
    print(f'Decrescente: {n3}, {n2}, {n1}')


