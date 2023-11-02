# Desarrolle un programa completo en Python que permita generar una sucesión de  14000 números enteros aleatorios,
# usando como semilla del generador al valor 973 (es decir, random.seed(973)). Los valores de cada uno de esos 14000
# números deben estar entre 100 y 21100 (incluidos ambos - DEBE usar random.randint(100, 21100) para generar cada uno
# de estos números).
#
# A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
# indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
#
# Suma de todos los números generados: 149000017
# A partir de esa sucesión, el programa debe:
#
# Determinar cuántos eran menores o iguales que 11000, cuántos eran mayores que 11000 pero menores que 17000 y además
# eran divisibles por 3 y por 8 al mismo tiempo, y cuántos eran mayores o iguales que 17000.
# Determinar el promedio entero de todos los números generados que sean divisibles por 9 pero que sean también menores
# o iguales a 15000. Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.
# Determinar el mayor entre todos los números generados cuyo valor esté entre 1000 y 14000 (incluidos ambos).
# Determinar el porcentaje entero que la cantidad de números divisibles por 6 representa sobre la cantidad total de
# números. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin decimales. Observación: en el cálculo
# de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.

import random
random.seed(973)
n = 14000
cont_men11000 = 0
cont_may11000 = 0
cont_may17000 = 0
cont_div9 = 0
acum_div9 = 0
may = 0
cont_div6 = 0

for i in range(n):
    num = random.randint(100, 21100)
    if num <= 11000:
        cont_men11000 += 1
    if (num > 11000) and (num < 17000) and (num % 3 == 0) and (num % 8 == 0):
        cont_may11000 += 1
    if num >= 17000:
        cont_may17000 += 1

    if num % 9 == 0 and num <= 15000:
        cont_div9 += 1
        acum_div9 += num

    if (num >= 1000) and (num <= 14000):
        if i == 0 or num > may:
            may = num
    if num % 6 == 0:
        cont_div6 += 1

promedio = acum_div9 // cont_div9
porcentaje = (cont_div6 * 100) // n

print("menores o iguales que 11000:", cont_men11000)
print("mayores que 11000 pero menores que 17000 y además eran divisibles por 3 y por 8 al mismo tiempo:", cont_may11000)
print("mayores o iguales que 17000:", cont_may17000)
print("el promedio entero de todos los números generados que sean divisibles por 9 pero que sean también menores o iguales a 15000:", promedio)
print("el mayor entre todos los números generados cuyo valor esté entre 1000 y 14000:", may)
print("el porcentaje entero que la cantidad de números divisibles por 6 representa sobre la cantidad total de números:", porcentaje, "%")
