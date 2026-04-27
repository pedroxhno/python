print('=== ANALISADOR DE PA ===')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

n = 0
while n < 10:
    an = a1 + r * n
    print(an)
    n += 1