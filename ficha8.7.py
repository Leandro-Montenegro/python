"""7. Problema estilo Parcial 1 (básico)
Desarrolle un programa completo en Python que permita generar una sucesión de 5000 números enteros aleatorios,
usando como semilla del generador el número 76. Los valores de cada uno de esos 5000 número deben estar entre 1 y 65000
(incluidos ambos). A partir de esa sucesión el programa debe:
1 - Determinar la cantidad de números pares que sean múltiplos de 6
2 - Determinar la cantidad de números son mayores del primer número de la serie, no incluir dicho número
3 - Determinar la cantidad de números que perteneces al segundo millar de números
4 - Determinar el porcentaje que representan la cantidad de números del punto 2 respecto del total de números procesados"""


import random
random.seed(76)
cont = 0
primer_num = 0
cont_may = 0
cont_mill = 0
#primer numero = None

for i in range(5000):
    num = random.randint(1, 65000)

    if num % 2 == 0 and num % 6 == 0:
        cont += 1

    if i == 0:
        primer_num = num
    if num > primer_num:
        cont_may += 1

#forma con banderas
#if primer_numero is None:
#      primer_numero = numero
#   else:
#       if numero > primer_numero:
#          contador_mult_primer_num += 1

    if (num > 1000) and (num < 2000):
        cont_mill += 1

porc = (cont_may * 100) // 5000
print(cont)
print(cont_may)
print(cont_mill)
print(porc)
