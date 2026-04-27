valor = float(input('Digite o valor do produto: '))
forma = int(input('Digite a forma de pagamento\n1 - Dinheiro/Cheque\n2 - Cartão\n'))

if forma == 1:
    valor -= valor * 0.10
    print(f'O valor do produto é R${valor:.2f}')

elif forma == 2:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela == 1:
        valor -= valor * 0.05
        qtd = valor / parcela
        print(f'O valor do produto é R${valor:.2f} e cada parcela será de R${qtd:.2f}')
    elif parcela == 2:
        qtd = valor / parcela
        print(f'O valor do produto é R${valor:.2f} e cada parcela será de R${qtd:.2f}')
    else: # parcela >= 3
        valor += valor * 0.2
        qtd = valor / parcela
        print(f'O valor do produto é R${valor:.2f} e cada parcela será de R${qtd:.2f}')
else:
    print('Erro! Opção inválida de pagamento.')