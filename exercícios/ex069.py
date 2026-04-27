maiores_18 = homens = mulheres = mulheres_menos_20 = contador = 0

while True:

    contador += 1
    print('\n', '=' * 10, f'Pessoa {contador}', '=' * 10)

    sexo = input('\nDigite o seu sexo: [M/F] ').upper()
    while sexo not in 'MF':
        sexo = input('Sexo inválido! Digite [M] para masculino ou [F] para feminino: ').upper()

    idade = int(input('Digite sua idade: '))
    while idade < 0:
        idade = int(input('Idade inválida! Digite sua idade: '))

    if idade >= 18:
        maiores_18 += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    if sexo == 'M':
        homens += 1

    continuar= input('Deseja continuar? [S/N] ').upper()
    if continuar != 'S':
        break

print(f"""\n{'='*40}
Cadastro finalizado!
Total de pessoas cadastradas: {contador}
Pessoas com 18 anos ou mais: {maiores_18}
Homens cadastrados: {homens}
Mulheres com menos de 20 anos: {mulheres_menos_20}
{'='*40}""")