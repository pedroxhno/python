from random import randint
print('Vamos jogar ímpar ou par!')
vitorias= 0
while True:
    while True:
        j = int(input('[ 1 ] Impar\n[ 2 ] Par\n'))
        if j in [1,2]:
            break
        else:
            print('Opção inválida. Tente novamente!')
    nj = int(input('Digite um número: '))
    while nj < 0 or nj > 10:
        print('Escolha um número de 0 a 10!')
        nj = int(input('Digite um número: '))
    nm = randint(0, 10)
    nt = nj + nm
    print(f'\nO computador colocou {nm}. Deu {nt}.', end=' ')
    print('Par!' if nt % 2 == 0 else 'Impar!')
    if nt % 2 == 1 and j == 1 or nt % 2 == 0 and j == 2:
        print('Você ganhou!')
        vitorias += 1
    elif nt % 2 == 0 and j == 1 or nt % 2 == 1 and j == 2:
        print('Você perdeu!')
        break
    print('-=' * 20)
print(f'\nO jogador venceu {vitorias} vezes!')