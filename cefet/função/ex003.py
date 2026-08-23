# Faça uma função que receba dois valores e retorne a média aritmética

def calcular_media(a, b):
    media = (a + b) / 2
    return media

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

resultado = calcular_media(a, b)

print(resultado)
