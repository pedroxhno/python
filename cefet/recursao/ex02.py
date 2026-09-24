# Faça uma função recursiva que receba um número inteiro e calcule o 
# nésimo termo da série de Fibonacci

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


num = int(input('entre com numero: '))
print(fibo(num))

# 1 1 2 3 5 8 13 21 34

# 0 + 1

# fibo(n) = fibo(n-1) + fibo(n-2)

# 5   4   3
# 4   3   2
# 2   1   0
# 1   0   -1
