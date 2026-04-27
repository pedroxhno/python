tupla = ('lápis', 3,
         'Borracha', 5,
         'Caderno', 20,
         'Estojo', 10,
         'Caneta', 1,
         'Livro', 5,
         'Macaco', 2000)
print(f'{'==' * 20}\nLISTAGEM DE PREÇOS\n{'==' * 20}')
print(f"""{tupla[0]}{'.' * (30-len(tupla[0]))}R${tupla[1]:.2f}
{tupla[2]}{'.' * (30-len(tupla[2]))}R${tupla[3]:.2f}
{tupla[4]}{'.' * (30-len(tupla[4]))}R${tupla[5]:.2f}
{tupla[6]}{'.' * (30-len(tupla[6]))}R${tupla[7]:.2f}
{tupla[8]}{'.' * (30-len(tupla[8]))}R${tupla[9]:.2f}
{tupla[10]}{'.' * (30-len(tupla[10]))}R${tupla[11]:.2f}
{tupla[12]}{'.' * (30-len(tupla[12]))}R${tupla[13]:.2f}
{'==' * 20}""")