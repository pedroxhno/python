#  Faça uma função que receba um caracter e retorne True se for vogal e False caso contrário

def eh_vogal(carac):
    if carac in 'aeiou':
        return True
    else:
        return False

letra = str(input('Digite uma letra: '))[0]
resultado = eh_vogal(letra)
print(resultado)
