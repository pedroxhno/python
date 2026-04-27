media_idade = 0
mulheres_menos_20 = 0
soma_idade = 0
homem_mais_velho = 0
nome_homem_velho = 0
for c in range(1, 5):
    print(f'----- {c}ª Pessoa -----')
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip().capitalize()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        homem_mais_velho = idade
        nome_homem_velho = nome
    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
media_idade = soma_idade / 4
print(f'A média da idade do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho do grupo é {nome_homem_velho} e tem {homem_mais_velho} anos.')
print(f'Existem {mulheres_menos_20} mulher(es) com menos de 20 anos no grupo.')
