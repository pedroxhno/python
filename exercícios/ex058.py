from random import randint

acertou = False
print('Penseu num número aleatório entre 1 e 10')
t = 1
n = randint(1, 10)
while not acertou:
    j = int(input('Seu chute: '))
    if j == n:
        print(f'Você ganhou em {t} tentativas!')
        acertou = True
    else:
        print('Tente novamente!')
        t += 1