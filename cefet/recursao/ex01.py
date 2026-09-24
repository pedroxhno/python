# Faça uma função recursiva que receba um número inteiro e calcule a 
# soma dos n primeiros números inteiros.

def soma_inteiros(n):
    if n == 1:
        return 1
    else:
        return n + soma_inteiros(n-1)

num = int(input('entre com numero: '))
print(soma_inteiros(num))

# 5