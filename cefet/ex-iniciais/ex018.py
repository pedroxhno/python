#Faça um programa que entre com um número de 3 dígitos (em apenas uma variável)
#e o escreva na ordem inversa em que foi digitado.
#Ex.: se o usuário digitar 379 terá que aparecer na tela 973.

num = int(input('Digite um número de 3 digitos: ')) #123
n3 = num % 10 #3
n1 = num // 100 # 1
n2 = (num // 10) % 10 #2
print(f'{n3}{n2}{n1}')