#Faça um programa que leia um valor inteiro representado uma certa quantidade em real (moeda),
#e diga qual é o número máximo de notas de dois reais e o mínimo de moedas de um real
#em que esse valor pode ser representado.

num = int(input('Digite o número de reais em sua conta: '))

notas_2 = num // 2
moedas = num % 2
print(f'R${num} dão {notas_2} notas de R$2 e {moedas} moedas')