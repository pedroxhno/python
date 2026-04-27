print('=== ANALISADOR DE PA ===')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1 + r * 10
for c in range(a1,an,r):
    print(c)