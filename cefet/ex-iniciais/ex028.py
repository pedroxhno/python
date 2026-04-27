#Faça um programa que leia um número binário de 4 dígitos e diga
#qual é o seu decimal correspondente

binario = int(input('Digite um número binário de 4 digitos: ')) #1234
n3 = binario // 1000 # 1
n2 = (binario % 1000) // 100 # 2
n1 = ((binario % 1000) // 10) % 10 # 3
n0 = binario % 10 # 4

decimal = (n3*2**3 + n2*2**2 + n1*2 + n0)
print(decimal)