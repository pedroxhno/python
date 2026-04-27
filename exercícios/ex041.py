idade = int(input('Qual a sua idade? '))
if idade <= 9:
    print('Você está na categoria MIRIM!')
elif 0 < idade <= 14:
    print('Você está na categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Você está na categoria JUNIOR!')
elif 19 < idade <= 20:
    print('Você está na categoria SÊNIOR!')
else: # idade > 20
    print('Você está na categoria MASTER!')