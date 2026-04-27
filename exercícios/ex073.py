times = ('Flamengo', 'Cruzeiro', 'Bragantino',
         'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG',
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio',
         'Ceará', 'Vasco da Gama', 'São Paulo', 'Santos', 'Vitória',
         'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')
print(f'Lista de times do Brasileirão: {times}\n{'=-' * 20}')
print(f'O G4 é: {times[:5]}\n{'=-' * 20}')
print(f'O Z4 é: {times[-4:]}\n{'=-' * 20}')
print(f'Times em ordem alfabética:\n{sorted(times)}\n{'=-' * 20}')
print(f'O Vasco da Gama está na posição {times.index('Vasco da Gama')+1}')