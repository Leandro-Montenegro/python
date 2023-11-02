# 3. Solamente 'a'
# Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto.
# En base al texto ingresado, determinar:
#
# a) Cuál es la longitud de la palabra más larga.
#
# b) Cuántas palabras tienen la a como única vocal
#
# c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras.
#
# ********************************************************************************
#
# Ejemplo: "el agua clara salta por las piedras."
#
# La longitud de la palabra más larga es 7 letras
#
# Las palabras cuya única vocal es la a son: 3
#
# El porcentaje de estas palabras sobre el total es 43 %


def es_vocal(car):
    return car in "aeiou"


cl = ctp = ctl = pal_a = 0
may = tiene_a = tiene_eiou = False
texto = input("texto")
for car in texto:
    if car == " " or car == ".":
        if cl > 0:
            ctp += 1
            ctl += cl
            if cl > may:
                may = cl
        if tiene_a and not tiene_eiou:
            pal_a += 1

        cl = 0
        tiene_a = tiene_eiou = False
    else:
        cl += 1
        if es_vocal(car):
            if car == "a":
                tiene_a = True
            else:
                if car in "eiou":
                    tiene_eiou = True
porc = 0
porc = pal_a * 100 / ctp


print(may)
print(pal_a)
print(round(porc, 2))
print(ctp)
