valores = list()
pares = list()
impares = list()

for c in range(0, 7):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print('==' * 20)
print(f'Os valores digitados foram: {sorted(valores)}')
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores impares digitados foram: {sorted(impares)}')

