n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 1 a 20: '))
    if 0 <= n <= 20:
        break
print(f'O número digitado foi: {n_extenso[n]}')