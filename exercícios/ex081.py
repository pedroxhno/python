valores = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar != 'S':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} valores')
print(f'Você digitou os valores {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')