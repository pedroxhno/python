ano = int(input('Em qual ano você nasceu? '))
idade = 2025 - ano
if idade < 18:
    print(f'Você ainda não precisa se alistar. Faltam {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de você se alistar!')
else: # idade > 18
    print(f'Seu prazo de alistamento já passou há {idade - 18} anos.')