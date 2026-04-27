pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).capitalize()
pessoa['ano de nascimento'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = 35 + pessoa['ano de contratação'] - pessoa['ano de nascimento']
print('-=' * 30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} = {v}')

