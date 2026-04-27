dados = dict()
dados['nome'] = str(input('Digite seu nome: ').capitalize())
dados['media'] = float(input('Digite sua média: '))
if dados['media'] >= 6:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
print('-' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')