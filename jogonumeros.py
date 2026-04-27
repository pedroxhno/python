import random

while True:

  n = random.randint(1, 30)

  print('Eu pensei em um número entre 1 e 30. Você tem 5 tentativas pra acertar!')

  for t in range(1, 6 ):
    chute = int(input(f'Tentativa {t}: Qual seu palpite? '))

    if chute == n:
      print(f'Parabéns! Você acertou o número {n} em {t} tentativas!')
      break
    elif chute < n:
      print('Tente um número MAIOR.')
    else: # chute > n
      print('Tente um número MENOR.')
  else:
      print(f'Poxa, suas 5 tentativas acabaram. O número era {n}.')

  sair = input('Deseja jogar novamente? (s/n) ')
  if sair != 's':
        print('Obrigado por jogar.')
        break