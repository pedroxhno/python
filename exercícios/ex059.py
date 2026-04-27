n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
parar = False

while not parar:
    print("""
Digite a operação que deseja efetuar: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Mostrar o maior
[ 4 ] Inserir novos números
[ 5 ] Sair do programa
""")
    c = int(input('Sua opção: '))
    if c == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}\n')
        parar = True
    elif c == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}\n')
        parar = True
    elif c == 3:
        parar = True
        if n1 > n2:
            print(f'O maior número é {n1}\n')
        elif n2 > n1:
            print(f'O maior número é {n2}\n')
        else:
            print('Os dois números são iguais.\n')
    elif c == 4:
        n1 = float(input('Digite o novo 1º número: '))
        n2 = float(input('Digite o novo 2º número: '))
    elif c == 5:
        print('Finalizando o programa...')
        parar = True
    else:
        print('Opção inválida. Tente novamente.\n')