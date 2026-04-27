import random

print('\33[1;36mVamos jogar pedra, papel ou tesoura!\33[m')

vj = 0
vm= 0

while True:

    while True:
        j = input('\nEscolha: pedra, papel ou tesoura? ').lower()
        if j in ['pedra', 'papel', 'tesoura']:
            break
        else:
            print("Escolha inválida. Digite pedra, papel ou tesoura.")

    m = random.choice(['pedra', 'papel', 'tesoura'])

    print(f'Você escolheu {j} e a máquina escolheu {m}.')

    if m == j:
        print('Empate!')
    elif (m == 'pedra' and j == 'tesoura') or \
        (m == 'tesoura' and j == 'papel') or \
        (m == 'papel' and j == 'pedra'):
        print('Você perdeu!')
        vm += 1
    else:
        print('Você ganhou!')
        vj += 1

    print(f'Placar: {'\33[1;34m'}Você {vj}{'\33[m'} x {'\33[1;31m'}{vm} Máquina{'\33[m.'}')
    sair = input(f'Quer jogar de novo? ({'\33[1;32m'}s{'\33[m'}/{'\33[1;31m'}n{'\33[m)'}').lower()
    if sair != 's':
        print('Obrigado por jogar.')
        break