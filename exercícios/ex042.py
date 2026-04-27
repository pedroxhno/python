print('=== ANALISADOR DE TRIANGULOS ===')

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de outra reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    triangulo = True
    print(f'\nAs retas {r1}, {r2} e {r3} PODEM formar um triangulo!')
else:
    triangulo = False
    print(f'\nAs retas {r1}, {r2} e {r3} NÃO PODEM formar um triangulo!')

if triangulo == True:

    if r1 == r2 == r3:
       print(f'O triângulo é EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3 or r3 == r1:
       print(f'O triângulo é ISÓSCELES!')
    else: # r1 != r2 != r3
       print(f'O triângulo é ESCALENO!')