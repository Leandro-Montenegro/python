# 7. Dificultad = pow (parcial, 3)
# Desarrollar un programa en Python que permita cargar por teclado un texto completo. Se supone que el usuario cargará
# un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio
# en blanco. El programa debe:
#
# a) Determinar la cantidad de palabras que tuvieron exactamente 3 vocales.
#
# b) Determinar el porcentaje de palabras que tuvieron algún dígito ('0' al '9') y más de 4 letras.
#
# c) De las palabras que terminan con la primera letra de todo el texto, determinar el orden de la que tiene menor
#  cantidad de caracteres. Por ejemplo, en el texto: 'Ana está en la casa', hay 4 palabras que terminan en la primera
#  letra del texto ('Ana', 'está', 'la', 'casa'), la que menos caracteres tiene es: 'la' y su orden es 4
#  (porque es la cuarta palabra del texto).
#
# d) Determinar la cantidad de palabras que contienen 'men' en la primera mitad de la palabra.


def es_vocal(car):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return car in vocales


def es_digito(car):
    digitos = "0123456789"
    return car in digitos


def main():

    cl = ctp = cvocal = r1 = 0
    cdig = mas4let = r2 = 0
    primero = True
    anterior = menor = tiene_m = tiene_me = tiene_men = None
    r3 = posr4 = r4 = 0

    m = open("texto.txt", "r")
    texto = m.read()
    m.close()

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                ctp += 1
            if cvocal == 3:
                r1 += 1
            if cdig and cl > 4:
                mas4let += 1
            if anterior == cl1:
                if menor is None or cl < menor:
                    menor = cl
                    r3 = ctp
            if posr4 <= (cl // 2) and tiene_men:
                r4 += 1
            cl = 0
            cvocal = 0
            tiene_men = False

        else:
            cl += 1
            if es_vocal(car):
                cvocal += 1
            if es_digito(car):
                cdig += 1
            if primero:
                cl1 = car
                primero = False
            anterior = car
            if car in "mM":
                tiene_m = True
            else:
                if car in "eE" and tiene_m:
                    tiene_me = True
                else:
                    if car in "nN" and tiene_me:
                        tiene_men = True
                        posr4 = cl
                    tiene_me = False
                tiene_m = False


    r2 = (mas4let * 100) / ctp

    print(r1)
    print(r2)
    print(r3)
    print(r4)

if __name__ == "__main__":
    main()
