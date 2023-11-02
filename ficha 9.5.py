# Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios,
# usando como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000
# números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).
#
# A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
# indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
#
# Suma de todos los números generados: 451459554
# A partir de esa sucesión el programa debe:
#
# Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
# Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
# Indicar cuantos números generados son pares menores a 15000.
# Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados. Aclaración 1:
# NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este
# porcentaje, haga primero la multiplicación que corresponda, y luego la división.
print("SIMULACRO DE PARCIAL 1")
import random
random.seed(49)
n = 20000
elem_control = 0
cont_num = 0
cont_mult5 = 0
cont_mult7 = 0
cont_mult9 = 0
num_may = 0
cont_pares = 0

for i in range(n):
    num = random.randint(1, 45000)
    elem_control += num
#PROCESOS
#Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.

    if num % 5 == 0:
        cont_mult5 += 1
    if num % 7 == 0:
        cont_mult7 += 1
    if num % 9 == 0:
        cont_mult9 += 1

# Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.

    if (num % 10 >= 5) and (num % 10 <= 8):
        if i == 0 or num > num_may:
            num_may = num

# Indicar cuantos números generados son pares menores a 15000.

    if num % 2 == 0 and num < 15000:
        cont_pares += 1

#Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados

porcentaje = (cont_pares * 100) // n

print('Control de validez de los números generados - La suma de todos ellos es:', elem_control)
print('Resultados pedidos por el enunciado:')
print('La cantidad de numeros multiplo de 5 fueron:', cont_mult5)
print('La cantidad de numeros multiplo de 7 fueron:', cont_mult7)
print('La cantidad de numeros multiplo de 9 fueron:', cont_mult9)
print('El mayor numero que terminan con un numero entre 5 y 8 es:', num_may)
print('La cantidad de numeros pares menores a 15000 son:', cont_pares)
print('y representan el', porcentaje, '%')
