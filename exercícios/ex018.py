import math

angulo = math.radians(float(input('Digite um ângulo (em graus): ')))
sin = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f'seu seno vale {sin:.3f}')
print(f'seu cosseno vale {cos:.3f}')
print(f'sua tangente vale {tan:.3f}')