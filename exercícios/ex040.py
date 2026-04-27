print('=== AVALIADOR DE NOTAS ===')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.2f}')
if m >= 7:
    print('Aprovado!')
elif m < 5:
    print('Reprovado!')
else: # 5 <= m < 7
    print('Recuperação!')