nome = input('Digite seu nome: ').strip()
dividido = nome.split()
print(f'Primeiro nome: {dividido[0]}')
print(f'Último nome: {dividido[len(dividido)-1]}')