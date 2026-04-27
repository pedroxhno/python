from random import randint
jogadores = dict()
for c in range(1, 5):
    jogadores[c] = randint(1, 6)
print(f'valores sorteados')
for k, v in jogadores.items():
    print(f'    Jogador{k}: {v}')

print('-'*20)

for c in range(4, 0, -1):
    print(f'    jogador{jogadores.values()}')
