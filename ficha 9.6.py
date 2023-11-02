# 6. Simulacro 2 del Parcial 1
# Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios,
# usando como semilla del generador el número 20220512 (es decir random.seed(20220512)). Los valores de cada uno de
# esos 25000 números deben estar entre 1 y 50000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).
#
# A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
# indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
#
# Suma de todos los números generados: 559657283
# A partir de esa sucesión el programa debe:
#
# 1-Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y
# finalmente la cantidad de    números que no cumplen ninguna de las 2 condiciones.
# 2-Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza con 1.
# 3-Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
# 4-Indicar el porcentaje entero que representa cada contador del punto 1. Aclaración 1: NO se pide el porcentaje
# redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero
# la multiplicación que corresponda, y luego la división.

import random
print("Simulacro 2 del Parcial 1")
print()
random.seed(20220512)

# VARIBALES

n = 25000
elem_control = 0
cont_3 = 0
cont_5 = 0
cont_ninguna = 0
may = 0
cont_pares = 0
acum_pares = 0

for i in range(n):
    num = random.randint(1, 45000)
    elem_control += num

# 1-Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y
# finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.

    if num % 3 == 0:
        cont_3 += 1
    else:
        if num % 5 == 0:
            cont_5 += 1
        else:
            cont_ninguna += 1

# 2-Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza con 1.

    cadena_numero = str(num)    # se convierte int en num para obtener el digito 1
    primer_digito = cadena_numero[0]
    if primer_digito == "1":
        if i == 0 or num > may:
            may = num

# caso alterno con bandera
# cadena_numero = str(num)
#     primer_digito = cadena_numero[0]
#     if primer_digito == '1':
#         if bandera_primer_caso:
#             mayor = num
#             bandera_primer_caso = False

# 3-Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
    if num % 2 == 0 and num % 11 == 0:
        acum_pares += num
        cont_pares += 1


if cont_pares > 0:
    promedio = acum_pares // cont_pares
else:
    promedio = 0

#4-Indicar el porcentaje entero que representa cada contador del punto 1.

porcentaje_3 = (cont_3 *100 // n)
porcentaje_5 = (cont_5 * 100 // n)
porcentaje_ninguna = (cont_ninguna * 100 // n)

print("la suma de todos los números generados con el mecanismo indicado son: ", elem_control)
print('Resultados pedidos por el enunciado:')
print('Cantidad de números múltiplos de 3:', cont_3)
print('Cantidad de números múltiplos de 5 y no de 3:', cont_5)
print('Cantidad restante de números:', cont_ninguna)
print('Número Mayor: ', may)
print('Promedio de pares múltiplos de 11:', promedio)
print('Porcentaje de números múltiplos de 3:', porcentaje_3)
print('Porcentaje de números múltiplos de 5 y no de 3:', porcentaje_5)
print('Porcentaje restante de números:', porcentaje_ninguna)

