from random import randint
jogo = list()
n_jogos = int(input('Quantos jogos você deseja? '))
print(f'======= SORTEANDO {n_jogos} JOGOS ======')
for c in range(1, n_jogos+1):
    for d in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    jogo.clear()