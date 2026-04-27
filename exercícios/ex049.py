n = int(input('Qual número você deseja a tabuada? '))
print(f'A tabuada de {n} é:')
print('=-' * 10)
for c in range(1,11):
    print(f'{n} x {c} = {n * c}')
print('=-' * 10)