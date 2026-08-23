# Faça uma função que receba um número inteiro e retorne True se o 
# número for par e False se o número for ímpar

def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = eh_par(int(input('Digite um numero: ')))
print(num)