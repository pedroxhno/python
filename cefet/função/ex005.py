# Faça uma função que receba um caracter e retorne True se for 
# consoante e False caso contrário

def eh_consoante(carac):
    if carac in 'bcdfghjklmnpqrstvwxyz':
        return True
    else:
        return False

letra = str(input('Digite uma letra: '))[0]
resultado = eh_consoante(letra)
print(resultado)

