#Faça um programa que leia um total de segundos e transforme para hora, minuto e segundo

seg = int(input('digite um numero de segundos: ')) #3722

horas = seg // 3600 # 1h
minutos = (seg % 3600) // 60 # 2m
segundos = (seg % 3600) % 60 # 2s
print(f'{horas} horas, {minutos} minutos e {segundos} segundos')