ntermos = int(input('Digite quantos termos você quer ver: '))
a = 0
b = 1
contador = 2
print(a)
while contador < ntermos:
    c = a + b
    print(c)
    a = b
    b = c
    contador += 1
