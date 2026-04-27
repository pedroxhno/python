distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da viagem será de R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'O valor da viagem será de R${valor:.2f}')