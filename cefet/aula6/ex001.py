# Faça um programa que leia dois vetores de 3 posições, que
# representam forças sobre um ponto no espaço 3D, e escreva a força
# resultante. Dica: força resultante é obtida pela soma dos valores das coordenadas correspondentes
# nos dois # vetores: (x1 + x2), (y1+ y2), (z1 + z2)

f1 = [float(input('x da força1: ')), float(input('y da força1: ')), float(input('z da força1: '))]
f2 = [float(input('x da força2: ')), float(input('y da força2: ')), float(input('z da força2: '))]

fr = [f1[0] + f2[0], f1[1] + f2[1], f1[2] + f2[2]]
print(f'as coordenadas da força resultante são {fr}')