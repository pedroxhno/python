continuar = True

n_maior = 0
n_menor = float('inf')
num = 0
soma = 0
while continuar == True:
    n = int(input('Digite um número: '))
    soma += n
    if n > n_maior:
        n_maior = n
    if n < n_menor:
        n_menor = n
    num += 1
    sair = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if sair != 'S':
        continuar = False
print(f'A média dos {num} números é {soma / num:.2f}')
print(f'O menor número digitado foi {n_menor} e o maior foi {n_maior}')