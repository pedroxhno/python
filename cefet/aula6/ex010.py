# Existem 20 candidatos à presidência, com códigos que variam de 1 até 20. Codificou-se 21 para votos brancos e 22 para votos nulos. Cada voto vem em um cartão (contendo só um voto) e o último cartão vem com o número 0 (zero)
# Faça um programa que auxilie a operação dos votos, imprimindo a quantidade de votos de cada candidato, o número de votos em branco, o número de votos nulos e o total de votantes. Imprima também o(s) candidato(s) que venceram a eleição e o número de votos do(s) vencedor(es).

votos_candidatos = [0] * 21  

num_brancos = 0
num_nulos = 0
tot_votantes = 0

print("Vote de 1 a 20 para os candidatos | 21 para Branco | 22 para Nulo | 0 para Encerrar")

while True:
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
        
    tot_votantes += 1
    
    if 1 <= voto <= 20:
        votos_candidatos[voto] += 1
    elif voto == 21:
        num_brancos += 1
    elif voto == 22:
        num_nulos += 1
    else:
        print("Voto inválido!")
        tot_votantes -= 1

for i in range(1, 21):
    print(f"Candidato {i}: {votos_candidatos[i]} voto(s)")

print(f"Votos em Branco: {num_brancos}")
print(f"Votos Nulos: {num_nulos}")
print(f"Total de Votantes: {tot_votantes}")

mais_votos = max(votos_candidatos[1:])

vencedores = []
for i in range(1, 21):
    if votos_candidatos[i] == mais_votos and mais_votos > 0:
        vencedores.append(i)

if len(vencedores) == 0:
    print("Nenhum candidato recebeu votos.")
elif len(vencedores) == 1:
    print(f"Vencedor da eleição: Candidato {vencedores[0]} com {mais_votos} voto(s)!")
else:
    print(f"Empate entre os candidatos: {vencedores} com {mais_votos} voto(s) cada!")