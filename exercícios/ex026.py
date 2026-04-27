frase = input('Digite uma frase: ').lower().strip()
print(f'Sua frase tem {frase.count('a')} letras A')
print(f'A primeira letra A apareceu na posição {frase.find('a')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('a')+1}')