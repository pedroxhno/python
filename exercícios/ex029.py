velocidade = float(input('Qual a velocidade do carro? (em Km/h) '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado!')
    print(f'A multa será no valor de R${multa:.2f}')
else:
    print('Você está numa boa velocidade!')