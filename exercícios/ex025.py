nome = str(input('Digite seu nome: '))
n = nome.lower().find('silva')
if n != -1:
 print(f"Seu nome tem 'Silva'")
else:
 print("Seu nome não tem 'Silva'")

#nome = str(input('Digite seu nome: '))
#print(f"Seu nome tem 'Silva'? {'silva' in nome.lower()}")