print('=== ANALISADOR DE TRIANGULOS ===')

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de outra reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} PODEM formar um triangulo!')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO PODEM formar um triangulo!')