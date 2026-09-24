# Faça um programa que leia um conjunto de linhas, contendo, cada 
# uma, o número de um empregado, a hora de início (hora, minuto e 
# segundo) e a hora do término (hora, minuto e segundo) de uma 
# determinada tarefa. A última linha conterá o número do empregado 
# igual a zero. Calcule para cada empregado, a duração da tarefa que ele 
# executou. Escreva para cada empregado, o seu número e a duração da 
# sua tarefa em horas, minutos e segundos.
# Obs.: Usar uma função que receba como parâmetros horas, minutos e 
# segundos e retorne o total de segundos. Usar uma função que receba 
# como parâmetro o total de segundos e retorne em horas, minutos e 
# segundos.

def converter_pra_segundos(h, m, s, ht, mt, st):
    tot_seg = h * 3600 + m * 60 + s
    tot_segt = ht * 3600 + mt * 60 + st
    return tot_segt - tot_seg 

def converter_pra_horas(num_seg):
    h = num_seg // 3600
    m = (num_seg - h * 3600) // 60
    s = num_seg - (h * 3600) - (m * 60)
    return h, m, s

horas = int(input('Digite as horas de início: '))
min = int(input('Digite os minutos de início: '))
seg = int(input('Digite os segundos de início: '))
horast = int(input('Digite as horas de término: '))
mint = int(input('Digite os minutos de término: '))
segt = int(input('Digite os segundos de término: '))
print(converter_pra_segundos(horas, min, seg, horast, mint, segt))
print(converter_pra_horas(converter_pra_segundos(horas, min, seg, horast, mint, segt)))

# 3661 = 1h 1m 1s
# h = // 3600
# m = tot - seg_h // 60
# s = tot - seg_h - seg_m
