def menu(memoria_atual):
    print(f"""
        Estado da memória: {memoria_atual}
        (1) Somar
        (2) Subtrair
        (3) Multiplicar
        (4) Dividir
        (5) Limpar memória
        (6) Sair do programa""")
    opcao = int(input('Qual opção você deseja: '))
    return opcao

def somar(memoria, num):
    return memoria + num

def subtrair(memoria, num):
    return memoria - num

def multiplicar(memoria, num):
    return memoria * num

def dividir(memoria, num):
    if num == 0:
        print('erro: divisão por zero')
        return memoria
    else:
        return memoria / num

def limpar():
    return 0

estado_memoria = 0

while True:
    opcao = menu(estado_memoria)

    if opcao == 6:
        print("saindo")
        break
    
    elif opcao == 5:
        estado_memoria = limpar()
        
    elif opcao in [1, 2, 3, 4]:
        numero = float(input('digite um numero: ')) 
        
        if opcao == 1:
            estado_memoria = somar(estado_memoria, numero)
        elif opcao == 2:
            estado_memoria = subtrair(estado_memoria, numero)
        elif opcao == 3:
            estado_memoria = multiplicar(estado_memoria, numero)
        elif opcao == 4:
            estado_memoria = dividir(estado_memoria, numero)
            
    else:
        print("opção invalida! tente novamente")