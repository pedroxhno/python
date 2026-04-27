import math

cateto1 = float(input('Digite um cateto: '))
cateto2 = float(input('Digite outro cateto: '))
hipotenusa = math.hypot(cateto1, cateto2)
print(f'A hipotenusa vale {hipotenusa:.2f}')