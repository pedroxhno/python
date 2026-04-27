km = float(input('quantos km foram rodados: '))
d = int(input('quantos dias se passaram: '))
p = 60*d + 0.15*km
print(f'o valor que será pago por {km}km rodados em {d} dias será de {p:.2f}R$')