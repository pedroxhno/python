# Faça uma função que retorne o valor absoluto de um número

def valor_absoluto(num):
    if num >= 0:
        return num
    else:
        num *= -1
        return num

num = valor_absoluto(float(input('Digite um numero: ')))
print(num)