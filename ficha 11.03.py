# 3. Silaba "ta"
# El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza
# con un punto, y las palabras están separadas por espacios únicamente.
# Se debe mostrar:
#
# a) Ver el porcentaje de vocales respecto del total de letras de la frase.
#
# b) La longitud promedio de las palabras
#
# c) La longitud de la palabra mas larga del texto
#
# d) Cantidad de palabras que comienzan con "ta"


def es_vocal(car):
    vocales = "aeiou"
    return car in vocales


def main():
    cl = ctp = cvoc = pal_ta = 0
    ctl = 0
    may = tiene_voc = tiene_t = tiene_ta = False
    texto = input("texto: ")

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                ctp += 1
                ctl += cl  # incrementa el acumulador de letras de la frase en la cantidad de letras de la palabra
                if cl > may:  # hace la busqueda de la palabra de mayor longitud
                    may = cl  # si encuentra un mayor, almacena la longitud de la palabra
                if tiene_ta:
                    pal_ta += 1
            cl = 0
            tiene_ta = False

        else:
            cl += 1
            if es_vocal(car):
                cvoc += 1
            if cl == 1 and car in "tT":
                tiene_t = True
            if cl == 2 and car in "aA":
                tiene_ta = True
                tiene_t = False

    porc = 0
    porc = (cvoc * 100) / ctl

    promedio = 0
    promedio = ctl / ctp

    print(cvoc)
    print(porc)
    print(promedio)
    print(may)
    print(pal_ta)


if __name__ == "__main__":
    main()
