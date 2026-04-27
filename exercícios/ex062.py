print('=== ANALISADOR DE PA ===')
a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ntermos = int(input('Quantos termos deseja ver? '))
inicio = 0

while inicio < ntermos:
    if ntermos == 0:
        break
    an = a1 + razao * inicio
    print(an)
    inicio += 1