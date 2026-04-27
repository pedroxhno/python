pessoas = list()
dados = list()
mais_pesados = list()
mais_leves = list()
maior_peso = menor_peso = 0

while True:

    dados.append(str(input('Nome: ').capitalize()))
    peso = int(input('Peso (KG): '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
        mais_pesados = [pessoas[-1][0]]
        mais_leves = [pessoas[-1][0]]

    else:

        if peso >= maior_peso:
            maior_peso = peso
            mais_pesados = [pessoas[-1][0]]
        elif peso == maior_peso:
            mais_pesados.append(pessoas[-1][0])

        if peso <= menor_peso:
            menor_peso = peso
            mais_leves = [pessoas[-1][0]]
        elif peso == menor_peso:
            mais_leves.append(pessoas[-1][0])

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar != 'S':
        break

print('-=' * 30)
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mais_pesados} com {maior_peso}Kg')
print(f'O menor peso foi de {mais_leves} com {menor_peso}Kg')