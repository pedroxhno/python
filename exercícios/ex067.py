while True:
    contador = 1
    n = int(input('\nDeseja a tabuada de qual número? '))
    if n < 0:
        print('Programa encerrado!')
        break
    print(f'----- Tabuada de {n} -----\n')
    while contador <= 10:
        print(f'{n} x {contador} = {n * contador}')
        contador += 1
