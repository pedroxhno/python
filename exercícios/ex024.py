cidade = input('Digite o nome de uma cidade: ').strip()
dividido = cidade.lower().split()
if dividido[0] == 'santo':
   print("A cidade começa com 'Santo'")
else:
    print("A cidade não começa com 'Santo'")

#cidade = input('Digite o nome de uma cidade: ').strip()
#print(cidade[:5].lower() == 'santo')
