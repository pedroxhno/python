sexo = input('Digite seu sexo (F/M): ').strip().upper()
while sexo not in 'FM':
    sexo = input('Digite um sexo válido (F/M): ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')