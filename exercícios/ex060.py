n = int(input('Digite um número: '))
fatorial = 1
numero = n
while n > 1:
    fatorial *= n
    n -= 1
print(f'O fatorial de {numero} é {fatorial}')

#for c in range(1, n):
    #if c > 1:
        #f *= c
#print(f'O fatorial de {f} é {fatorial}')