# 5. Con m y b
# Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto.
# En base al texto ingresado, determinar:
#
# a) Cuántas palabras tienen una m y una b a partir de la tercer letra.
#
# b) Cuántas palabras comienzan con la letra p seguida de cualquier vocal.
#
# c) Cuántas palabras comienzan y terminan con el mismo carácter.
#
# ********************************************************************************
# Ejemplo: 'Mi amiga Ambar siempre piensa y cambia pronto.'
# ********************************************************************************
# Palabras tienen una m y una b a partir de la tercer letra: 1
# Palabras que comienzan con la letra p seguida de cualquier vocal: 1
# Palabras que comienzan y terminan con el mismo carácter: 2

def es_vocal(car):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return car in vocales


cl = ctp = cbm = emp_p = emp_term_igual = 0
hay_b = hay_m = hay_vocal = hay_p = False
anterior = ""

texto = input("texto")
for car in texto:
    if car == " " or car == ".":
        if cl > 0:
            ctp += 1
        if hay_b and hay_m:
            cbm += 1
        if hay_vocal:
            emp_p += 1
        if primera == ultima:
            emp_term_igual += 1

        cl = 0
        hay_m = hay_b = False
        hay_p = False
        hay_vocal = False
        empieza = ""
        termina = ""
    else:
        cl += 1
        if cl >= 3:
            if car == "m":
                hay_m = True
            if car == "b":
                hay_b = True
        if cl == 1 and car == "p":
            hay_p = True
        if cl == 2 and es_vocal(car) and hay_p:
            hay_vocal = True
        if cl == 1:
            primera = car
        ultima = car


print(cbm)
print(emp_p)
print(emp_term_igual)
