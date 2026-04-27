print('=== APROVADOR DE EMPRÉSTIMOS ===')
valor = float(input(f'Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual seu salário mensal? '))
anos = float(input('Em quantos anos você deseja pagar? '))
prestacao = valor / (anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Emprestímo ACEITO!')