tupla = ('Jaime', 'Jorge', 'Edmilson', 'Aristóteles', 'Arnaldo', 'Pedro', 'Matheus')
for p in tupla:
    print(f'\nNa palavra {p} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
