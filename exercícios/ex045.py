import random
import time

print('Vamos jogar JOKENPO!')
m = random.choice(['pedra', 'papel', 'tesoura'])
j = str(input('Faça sua jogada! (pedra, papel ou tesoura)')).lower()

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('=-' * 20)
print(f'O computador jogou {m} e o jogador {j}')
if j == m:
    print('Empate!')
elif j == 'pedra' and m == 'tesoura' or j == 'papel' and m == 'pedra' or j == 'tesoura' and m == 'papel':
    print('Você ganhou!')
elif j == 'pedra' and m == 'papel' or j == 'papel' and m == 'tesoura' or j == 'tesoura' and m == 'pedra':
    print('Você perdeu!')
else:
    print('Erro!')
print('=-' * 20)