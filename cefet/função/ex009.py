# Faça um programa que, dado uma figura geométrica que pode ser 
# uma circunferência, triângulo ou retângulo, calcule a área e o 
# perímetro da figura
# • O programa deve primeiro perguntar qual o opcao da figura: – (1) circunferência – (2) triângulo – (3) retângulo
# • Dependendo do opcao de figura, ler o (1) tamanho do raio da 
# circunferência; (2) tamanho de cada um dos lados do triângulo; (3) 
# tamanho dos dois lados retângulo
# • Usar funções sempre que possível

import math

def menu():
    print('(1) circunferência \n(2) triângulo \n(3) retângulo\n')
    opcao = int(input('Qual opção você deseja: '))
    return opcao

def calcular_circ():
    raio = float(input('digite o raio: '))
    area = round((math.pi * pow(raio, 2)), 2)
    perimetro = round((2 * math.pi * raio), 2)
    return perimetro, area

def calcular_tria():
    lado_um = float(input('digite o lado 1: '))
    lado_dois = float(input('digite o lado 2: '))
    lado_tres = float(input('digite o lado 3: '))

    perimetro = lado_um + lado_dois + lado_tres
    sperimetro = perimetro / 2
    area = math.sqrt(sperimetro * (sperimetro - lado_um) * (sperimetro - lado_dois) * (sperimetro - lado_tres)) 
    return perimetro, area

def calcular_reta():
    base = float(input('digite a base: '))
    altura = float(input('digite a altura: '))
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area

opcao = menu()
if opcao == 1:
    perimetro, area = calcular_circ()
elif opcao == 2:
    perimetro, area = calcular_tria()
elif opcao == 3:
    perimetro, area = calcular_reta()        
else:
    print("opção invalida! tente novamente")

print(f'O perimetro é {perimetro} e a área é {area}')