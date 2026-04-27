#Faça um programa que leia 2 palavras e diga se elas são iguais ou
#diferentes.

p1 = str(input('Digite uma palavra: ')).strip()
p2 = str(input('Digite outra palavra: ')).strip()
if p1 == p2:
    print(f'{p1} e {p2} são iguais!')
else:
    print(f'{p1} e {p2} não são iguais!')