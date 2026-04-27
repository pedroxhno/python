maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else: #p peso < menor
            menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor}')

