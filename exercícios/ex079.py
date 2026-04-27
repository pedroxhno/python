valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente na lista.')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar != 'S':
        break
print(f'Você digitou os valores {sorted(valores)}')
