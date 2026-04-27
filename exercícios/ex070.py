total_gasto = preco_mais_1000 = produto = nome_mais_barato = 0
preco_mais_barato = float('inf')
while True:
    produto += 1
    print(f'========== Produto: {produto} ==========')
    nome = input('Nome do produto: ').strip().title()
    preco = float(input('Preço do produto: R$'))
    total_gasto += preco
    if produto == 1:
        nome_mais_barato = nome
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            nome_mais_barato = nome
    if preco > 1000:
        preco_mais_1000 += 1
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Opção inválida! Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
print(f"""
========== RESUMO ==========
Total gasto: R${total_gasto:.2f}
Produto mais barato: {nome_mais_barato} (R${preco_mais_barato:.2f})
Produtos acima de R$1000.00: {preco_mais_1000}
""")