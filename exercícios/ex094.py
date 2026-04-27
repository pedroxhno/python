grupo = list()
pessoa = dict()
idademaiormedia = list()
mulheres = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome do jogador: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    if pessoa['sexo'] == 'F':
      mulheres.append(pessoa['nome'])

    continuar = input('deseja continuar? [S/N]').upper()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]')
    if continuar == 'N':
        break

for pessoa in grupo:
    soma += pessoa['idade']
media = soma / len(grupo)

for pessoa in grupo:
    if pessoa['idade'] > media:
        idademaiormedia.append(pessoa['nome'])

print('-=' * 30)
print(f"""
O grupo tem {len(grupo)} pessoas.
A média de idade é de {media:.2f} anos.
As mulheres do grupo são: {mulheres}
As pessoas com idade acima da média do grupo são: {idademaiormedia}
""")



