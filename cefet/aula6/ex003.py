# Faça um programa que preencha por leitura um vetor de 5 posições, e informe
# a posição em que um valor x (lido do  teclado) está no vetor.
# Caso o valor x não seja encontrado, o programa deve imprimir o valor -1.
# Faça a questão de duas formas: não utililizando o método index() e utilizando o método index().

tot = 5
vetor = []

for i in range(tot):
    vetor.append(int(input('digite um numero: ')))
num = int(input('digite o numero que deseja saber o index: '))
if num not in vetor:
    print('-1')
else:
    print(f'sua posição no vetor é {vetor.index(num)}')
