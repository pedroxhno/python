valores = list()
valores_pares = list()
valores_impares = list()
cont = 0

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar != 'S':
        break
while cont < len(valores):
    if valores[cont] % 2 == 0:
        valores_pares.append(valores[cont])
    else:
        valores_impares.append(valores[cont])
    cont += 1

print(f'Os valores digitados foram: {valores}')
print(f'Os pares valores digitados foram: {valores_pares}')
print(f'Os ímpares valores digitados foram: {valores_impares}')