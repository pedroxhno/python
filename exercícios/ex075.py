n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite o 2 número: '))
n3 = int(input('Digite o 3 número: '))
n4 = int(input('Digite o 4 número: '))
n5 = int(input('Digite o 5 número: '))
pares = 0
tupla = (n1, n2, n3, n4, n5)
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro 3 apareceu na posição {tupla.index(3)+1}.')
print(f'Os valores pares digitados foram:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')