# Faça uma função que informe o status do aluno a partir da sua média 
# de acordo com a tabela a seguir:
# – Nota acima de 6 “Aprovado”
# – Nota entre 4 e 6 “Verificação Suplementar”
# – Nota abaixo de 4 “Reprovado”

def mostrarStatus(nota):
    if nota >= 6:
        return 'Aprovado'
    if 4 <= nota < 6:
        return 'Verificação suplementar'
    if nota < 4:
        return 'Reprovado'

media = float(input('digite a media: '))
print(mostrarStatus(media))

