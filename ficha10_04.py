# 4. Inicio con sílaba "pa"
# Desarrollar un programa en Python que permita cargar por teclado un texto. Siempre se supone que usuario cargará un punto para indicar el final del texto, y que cada
# palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe determinar:
#
# a) La cantidad de palabras que comienzan con la expresión "pa" y termina con la letra "n"
#
# c) La cantidad de palabras que presentan mas de dos vocales a partir de la tercera letra de la palabra
#
# d) El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad de total de palabras del texto
#
# e) Cantidad de palabras de mas de 5 letras


texto = input("ingrese texto, ingrese punto para finalizar: ")
cont_pa = cl = ctp = cont_vc = cant_vocales = cant_pal_vocales = pal_mas_5letras = 0
tiene_p = tiene_pa = tiene_n = False
car_ant = ""

def es_vocal (car):
    vocales = "aeiou"
    return car in vocales

def porcentaje(pal_con_vocales, total):
    porc = 0
    if total > 0:
        porc = (pal_con_vocales * 100) // total
    return porc


for car in texto:
    if car == " " or car == ".":
        if cl > 0:
            ctp += 1
        if tiene_pa and car_ant == "n":
            cont_pa += 1
        if cant_vocales > 2:
            cant_pal_vocales += 1

        if cl > 5:
            pal_mas_5letras += 1

        cl = 0
        cant_vocales = 0
        tiene_p = False
        tiene_pa = False

    else:
        cl += 1
        if cl == 1 and car == "p" and not tiene_pa:
            tiene_p = True
        if cl == 2 and car == "a":
            tiene_pa = True
        tiene_p = False

        if cl > 3:
            if es_vocal(car):
                cant_vocales += 1
    car_ant = car

porc = porcentaje(cant_pal_vocales, ctp)

print(ctp)
print(cont_pa)
print(cant_pal_vocales)
print(pal_mas_5letras)
print(porc, "%")
