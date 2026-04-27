from datetime import date
atual = date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo, {maiores} são maiores de idade e {menores} são menores de idade')