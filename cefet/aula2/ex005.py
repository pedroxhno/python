# Faça um programa que leia um peso no planeta Terra e o
# número de um planeta e imprima o valor do seu peso neste planeta.
# A relação dos planetas é dada a seguir juntamente com o valor das gravidades
# relativas ao planeta Terra.

peso = float(input('Digite seu peso: '))
print("""
[1] Mercúrio
[2] Vênus
[3] Marte
[4] Júpiter
[5] Saturno
[6] Urano""")
escolha = int(input('Digite o número do planeta que deseja ver seu peso: '))
while escolha not in range(1, 7):
    print('Escolha inválida')
    escolha = int(input('Digite o número do planeta que deseja ver seu peso: '))
if escolha == 1:
    print(f'Seu peso: {peso:.2f}kg => {peso*0.37:.2f}kg')
elif escolha == 2:
    print(f'Seu peso: {peso:.2f}kg => {peso*0.88 :.2f}kg')
elif escolha == 3:
    print(f'Seu peso: {peso:.2f}kg => {peso*0.38 :.2f}kg')
elif escolha == 4:
    print(f'Seu peso: {peso:.2f}kg => {peso*2.64 :.2f}kg')
elif escolha == 5:
    print(f'Seu peso: {peso:.2f}kg => {peso*1.15:.2f}kg')
else:   # elif escolha == 6:
    print(f'Seu peso: {peso:.2f}kg => {peso*1.17 :.2f}kg')