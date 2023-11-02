"""9. Problema estilo Parcial 1 (Complicado)
Desarrolle un programa completo en Python que permita generar una sucesión de 27000 números enteros aleatorios,
 usando como semilla del generador al valor 37 (es decir, random.seed(37)). Los valores de cada uno de esos 27000
  números deben estar entre -20000 y 30000 (incluidos ambos - DEBE usar random.randint(-20000, 30000) para generar
  cada uno de estos números). A partir de esa sucesión, el programa debe:

1 - Determinar cuántos de esos números son mayores o iguales que -20000 pero menores que -5000; también
determinar cuántos números son mayores o iguales a -5000 pero menores que 15000, y cuántos números
son mayores o iguales que 15000 pero además son divisibles por 9.

2 - Determinar el promedio entero de todos los números generados que sean mayores o iguales a 1000 pero
que además tengan su último dígito igual a 4 o a 6 (es decir, el resto de dividir por 10 debe ser 4 o 6).
Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.

3 - Determinar el mayor entre todos los números generados que sean positivos impares, pero que además
tengan su último digito diferente de 1 (es decir, además de ser impar, el resto de dividir por 10 debe ser
diferente de 1).

4 - Determinar el porcentaje entero que la cantidad de números divisibles por 7 representa sobre la cantidad
total de números. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que
corresponda, y luego la división."""

import random
random.seed(37)
n = 27000
num_men_menos5000 = 0
num_menoigual_15000 = 0
num_mayoigual_15000 = 0
cont_may1000 = 0
acum_may1000 = 0
num_div7 = 0
mayor_pos_impar = 0
#primer_pos_impar = True
#mayor_pos_impar = None

# 1 - Determinar cuántos de esos números son mayores o iguales que -20000 pero menores que -5000; también
# determinar cuántos números son mayores o iguales a -5000 pero menores que 15000, y cuántos números
# son mayores o iguales que 15000 pero además son divisibles por 9.

for i in range(n):
    num = random.randint(-20000, 30000)

    if (num >= -20000) and (num < -5000):
        num_men_menos5000 += 1
    if (num >= -5000) and num < 15000:
        num_menoigual_15000 += 1
    if (num >= 15000) and num % 9 == 0:
        num_mayoigual_15000 += 1

# 2 - Determinar el promedio entero de todos los números generados que sean mayores o iguales a 1000 pero
# que además tengan su último dígito igual a 4 o a 6 (es decir, el resto de dividir por 10 debe ser 4 o 6).
# Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.

    ult_dig = num % 10
    if num >= 1000 and (ult_dig == 4 or ult_dig == 6):
        cont_may1000 += 1
        acum_may1000 += num

# 3 - Determinar el mayor entre todos los números generados que sean positivos impares, pero que además
#  tengan su último digito diferente de 1 (es decir, además de ser impar, el resto de dividir por 10 debe ser
# diferente de 1).

    if num > 0 and num % 2 == 1 and ult_dig != 1:
        if i == 0 or num > mayor_pos_impar:
            mayor_pos_impar = num


# 4 - Determinar el porcentaje entero que la cantidad de números divisibles por 7 representa sobre la cantidad
# total de números. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que
# corresponda, y luego la división.

    if num % 7 == 0:
        num_div7 += 1


promedio = 0
if cont_may1000 > 0:
    promedio = acum_may1000 // cont_may1000

porc = (num_div7 * 100) // n

# salidas

print('La cantidad de numeros entre -20000 incluido y -5000 son:', num_men_menos5000)
print('La cantidad de numeros entre -5000 incluido y 15000 son:', num_menoigual_15000)
print('La cantidad de numeros mayor a 15000 incluido y multiplos de 9 son:', num_mayoigual_15000)
print('El promedio de los numeros mayores a 1000 y terminan con 4 o 6 son:', promedio)
print('El mayor de los numeros positivos impares que no terminan en 1 es:', mayor_pos_impar)
print('El Porcentaje de los numeros divisibles por 7 sobre el total de numeros leidos es:', porc, '%')

