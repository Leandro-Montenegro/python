# 6. Sílaba "pe"
# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo
# cadena de caracteres. Se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra
# de ese texto está separada de las demás por un espacio en blanco. El programa debe:
#
# a) Determinar cuántas palabras tienen 3, 5 o 7 letras.
#
# b) Determinar la cantidad de palabras con más de tres letras, que tienen una vocal en la tercera letra.
#
# c) Determinar el porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto.
#
# d) Determinar la cantidad de palabras que contienen más de una vez la sílaba "pe".




def main():
    texto = input("ingrese cadena")

    ctp = cl = cpe = r4 = 0
    anterior = False

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                ctp += 1
            if cpe > 1:
                r4 += 1
            cl = 0
            cpe = 0

        else:
            cl += 1
            if car in "eE" and anterior in "pP":
                cpe += 1
        anterior = car

    print(r4)

if __name__ == "__main__":
    main()
