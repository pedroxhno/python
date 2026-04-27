grupo = list()
jogador = dict()
gols = list()

while True:
    print('-=' * 30)
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    jogador['total de partidas'] = int(input('Quantidade de partidas: '))
    for c in range(1, jogador['total de partidas'] + 1):
        gols = (int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = gols
    jogador['total de gols'] = sum(gols)
    grupo.append(jogador.copy())

    continuar = input('deseja continuar? [S/N]').upper()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]')
    if continuar == 'N':
        break

print('-=' * 30)
for c in range(0, len(grupo)):
    jogador['código do jogador'] = c
    print(f"""Cód      Nome      Gols        Total
    {c}        {jogador['nome']}       {jogador['gols']}       {jogador['total de gols']}       """)
print('-=' * 30)
print('Deseja levantar dados de qual jogador? ')

