matriz = list()
l0 = list()
l1 = list()
l2 = list()

for c in range(1, 10):

    num = int(input(f'Digite um valor para a [{(c-1)//3}, {(c-1)%3}]: '))
    matriz.append(num)

    if c < 4:
        l0.append(matriz[-1])
    elif c < 7:
        l1.append(matriz[-1])
    else:
        l2.append(matriz[-1])

print('-=' * 30)
print(f"""
[ {l0[0]} ] [ {l0[1]} ] [ {l0[2]} ]
[ {l1[0]} ] [ {l1[1]} ] [ {l1[2]} ]
[ {l2[0]} ] [ {l2[1]} ] [ {l2[2]} ]
""")