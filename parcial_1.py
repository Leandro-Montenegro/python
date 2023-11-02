import random

random.seed(47)
n = 13000
inicio = 1
fin = 33000

#inicializar variables:
num_div4 = 0
num_par = 0
num_div7 = 0
suma_num = 0
men_num = None
cant_suma = 0
porc = 0

for i in range(n):
    num = random.randint(inicio, fin)

###1)Determinar cuántos eran mayores o iguales a 1 pero menores a 15000 y además eran divisibles por 4.

    if 15000 > num >= 1:
        if num % 4 == 0:
            num_div4 +=1

###2)cuantos eran mayores o iguales a 15000 pero menores que 22000 pero además eran pares.

    if 22000 > num >= 15000:
        if num % 2 == 0:
            num_par += 1

###cuantos eran mayores o iguales a 22000 pero además eran divisibles por 7. ")

    if num >= 22000:
        if num % 7 == 0:
            num_div7 += 1

###3)Determinar la suma de todos los números generados que estén entre 4000 y 11000 (incluídos ambos).")

    if 11000 >= num >= 4000:
        suma_num += num
        cant_suma += 1
    print(num)



###Determinar el menor entre todos los números generados cuyos últimos dos dígitos sean iguales a 23 es decir, aquellos
# cuyo resto al dividir por 100 es igual a 23).

    if men_num is None or (num < men_num and num % 100 == 23):
        men_num = num


###Determinar el porcentaje entero que la cantidad de números entre 4000 y 11000 (incluidos ambos) representa"
# sobre la cantidad total de números. Observación: en el cálculo de este porcentaje, haga primero la
# multiplicación que corresponda, y luego la división.")

porc = cant_suma * 100 // n



print("numeros mayores o iguales a 1 pero menores a 15000 y además eran divisibles por 4: ", num_div4)
print("numeros mayores o iguales a 15000 pero menores que 22000 pero además eran pares: ", num_par)
print("cuantos eran mayores o iguales a 22000 pero además eran divisibles por 7: ", num_div7)
print("la suma de todos los números generados que estén entre 4000 y 11000 es de : ", suma_num)
print("el menor numero entre todos los números generados cuyos últimos dos dígitos sean iguales a 23 es : ", men_num)
print("cantidad de numeros entre 4000 y 11000", num)
print("el porcentaje es de ", porc)
