from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números foram: {sorted(numeros)}')
print(f'O menor valor foi: {min(numeros)}') # {sorted(numeros)[0]}
print(f'O maior valor foi: {max(numeros)}') # {sorted(numeros)[-1]}
