n = int(input('Digite um número: '))
print('Para qual base deseja converter esse número?')
base = int(input('[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n'))
if base == 1:
    print(f'O número {n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif base == 2:
    print(f'O número {n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif base == 3:
    print(f'O número {n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Erro!')