valor = int(input('Qual é o valor que será sacado? R$'))

restante = valor

notas_50 = restante // 50
restante %= 50

notas_20 = restante // 20
restante %= 20

notas_10 = restante // 10
restante %= 10

notas_1 = restante // 1
restante %= 1

print(f"""
Para sacar R${valor}, serão entregues:
{notas_50} cédula(s) de R$50
{notas_20} cédula(s) de R$20
{notas_10} cédula(s) de R$10
{notas_1} cédula(s) de R$1
""")

