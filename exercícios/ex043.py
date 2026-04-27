print('=== CALCULADORA DE IMC ===')
peso = float(input('Digite seu peso (em quilogramas): '))
altura = float(input('Digite sua altura (em metros): '))
imc = peso / (altura * altura)
print(f'Seu IMC vale {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else: # imc >= 40
    print('Você está com obesidade mórbida!')