valores=list()

for cont in range(0, 5):
    num = valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Você digitou os valores {valores}')

print(f'\nO maior valor digitado foi {max(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == max(valores):
        print(c, end='..')

print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == min(valores):
        print(c, end='..')