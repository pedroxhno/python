jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
jogador['total de partidas'] = int(input('Quantidade de partidas: '))
for c in range(1, jogador['total de partidas'] + 1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = gols[:]
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["total de partidas"]} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'    => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
