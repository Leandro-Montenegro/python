# . Sílaba "de" en la primera mitad
# Desarrollar un programa en Python que permita cargar el texto completo desde un archivo. Siempre se supone que el
# usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las
# demás por un espacio en blanco. El programa debe:
#
# a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
#
# b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
#
# c) Determinar la longitud de la palabra más larga del texto.
#
# d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra.


def es_digito(car):
    digitos = "0123456789"
    return car in digitos


def main():
    cl = ctp = cdig = ctl = posicion = paldemitad = 0
    tienen3omenos = tienen4a6 = tienenmas6 = 0
    may = tiene_de = tiene_d = False
    anterior = ""
    m = open("texto.txt", "rt")
    texto = m.read()
    m.close()

    for car in texto:
        if car == " " or car == ".":
            if cl > 1:
                ctp += 1
                ctl += cl
            if cl > may:
                may = cl
            if cl <= 3:
                tienen3omenos += 1
            if (cl >= 4) and (cl <= 6):
                tienen4a6 += 1
            if cl > 6:
                tienenmas6 += 1
            mitad = cl // 2
            if tiene_de and posicion <= mitad:
                paldemitad += 1

            cl = 0
            tiene_dig = False
            tiene_de = False

        else:
            cl += 1
            if es_digito(car):
                tiene_dig = True
                cdig += 1
            if car in "dD" and not tiene_de:
                tiene_d = True
            else:
                if car in "eE" and tiene_d:
                    tiene_de = True
                    posicion = cl
                tiene_d = False


    print(tienen3omenos)
    print(tienen4a6)
    print(tienenmas6)
    print(cdig)
    print(may)
    print(paldemitad)

if __name__ == "__main__":
    main()

