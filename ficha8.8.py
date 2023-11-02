"""8. Problema estilo Parcial 1 (no tan básico)
Desarrolle un programa completo en Python que permita generar una sucesión de 45000 números enteros aleatorios,
 usando como semilla del generador el número 95. Los valores de cada uno de esos 45000 número deben estar entre
  1 y 95000 (incluidos ambos). A partir de esa sucesión el programa debe:"""

#
import random
random.seed(95)
#variables
segundo_num = 0
cant_num_menores = 0
cont_69 = 0
cont_6 = 0
cont_9 = 0
may_mult4 = 0

# segundo_numero = primer_numero = None
# primer_mult4 = True
# may_mult4 = None

#ciclo
for i in range(45000):
    num = random.randint(1, 95000)
#1 - Determinar la cantidad de números que son menores al segundo numero leído de la secuencia

    if i == 1:
        segundo_num = num
    if num < segundo_num:
        cant_num_menores += 1

#otra forma:
    # incluyendo el primer numero del secuencia
    #     if i == 0:
    #         primer_numero = num
    #
    #     if i == 1:
    #        segundo_numero = num
    #        if primer_numero < segundo_numero:
    #            cant_menores_seg_num += 1
    #
    #     if i > 1 and num < segundo_numero:
    #         cant_menores_seg_num += 1


#2 - Determinar la cantidad de números que son múltiplos de 6, múltiplos de 9 y múltiplos de ambos

    if num % 6 == 0 and num % 9 == 0:
        cont_69 += 1
    if num % 6 == 0:
        cont_6 += 1
    if num % 9 == 0:
        cont_9 += 1

#3 - Informar cual es el mayor numero múltiplo de 4 que se encontró en la serie


    if num % 4 == 0:
        if i == 0 or num > may_mult4:
            may_mult4 = num


#  if num % 4 == 0:
#         if primer_mult_4:
#             mayor_mult = num
#             primer_mult_4 = False
#         elif num > mayor_mult4:
#             mayor_mult4 = num


#4 - Determinar cual es porcentaje que representa la cantidad del punto 1 respecto del total de números procesados

porc = (cant_num_menores * 100) // 45000

#salidas
print(cant_num_menores)
print(cont_69)
print(cont_6)
print(cont_9)
print(may_mult4)
print(porc)


