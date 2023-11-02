# 1. Sílaba "mo"
# Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es
# cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es
#  cargar cada caracter uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para
#  indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
#  El programa debe:
#
# a) Determinar cuántas palabras tenían más de 4 letras.
#
# b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".
#
# c) Determinar el promedio de letras por palabra en todo el texto.
#
# d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".
#
# ********************************************************************************
# Ejemplo: 'el mono momoxy toca el xilofon.'
# ********************************************************************************
# Palabras con más de 4 letras: 2
# Palabras tenían al menos una vez la letra "x" o la letra "y": 2
# El promedio de letras por palabra en todo el texto es: 4.17
# Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1

pal_mas_4letras = 0
cont_letras = 0
cont_palabras = 0
hay_x = 0
hay_y = 0
palabras_conxy = 0
cont_letras_punto3 = 0
palabra_con_mo = 0

m = open("texto.txt")
texto = m.read()
m.close()

for car in texto:
    if car != " " and car != ".":
        cont_letras_punto3 += 1
        cont_letras += 1
        if car == "x" or car == "y":
            hay_x += 1
            hay_y += 1
    else:
        cont_palabras += 1
        if cont_letras > 4:
            pal_mas_4letras += 1
        cont_letras = 0
        if hay_x or hay_y:
            palabras_conxy += 1
        hay_y = 0
        hay_x = 0

promedio = cont_letras_punto3 / cont_palabras

print("palabras de más de 4 letras: ", pal_mas_4letras)
print("palabras que tienen al menos una vez la letra 'x' o la letra 'y': ", palabras_conxy)
print(promedio)
print(palabra_con_mo)












