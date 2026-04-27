salario = float(input('Qual seu salário? '))
if salario > 1250:
    salario = salario * 1.1
    print(f'Seu novo salário é R${salario:.2f}')
else:
    salario = salario * 1.15
    print(f'Seu novo salário é R${salario:.2f}')