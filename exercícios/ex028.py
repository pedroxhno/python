import random

n = random.randint(1, 5)
print('Pensei num número de 1 a 5')
chute = int(input('Qual seu chute? '))
if chute == n:
    print('Você acertou!')
else:
    print('Você errou!')
    print(f'O número era {n}')