# 2. Sílaba 'li'
# Se solicita crear un programa que permita ingresar un texto, las palabras se encontraran separadas únicamente por
# espacios en blanco y el mismo debe finalizar con un punto. En base a ese texto determinar:
#
# a) Cantidad de palabras que comienzan con consonantes y terminan en vocales
#
# b) Cantidad de palabras que poseen la secuencia ‘li’ a partir de la tercera letra de la palabra
#
# c) Cantidad de palabras con menos de 4 letras y porcentaje que dicha cantidad representa sobre el total del texto


def es_vocal(car):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return car in vocales


def es_digito(car):
    digitos = "0123456789"
    return car in digitos


def es_consonante(car):
    if not es_vocal(car) and not es_digito(car):
        return True
    return False


def main():
    cl = ctp = r1 = r2 = r3 = 0
    emp_cons = False
    car_ant = ""
    tiene_li = men4 = False
    men_3l = pal4 = 0

    m = open("texto.txt", "rt")
    texto = m.read()
    m.close()
    for car in texto:
        if car == " " or car == ".":
            if cl >= 1:
                ctp += 1
            if emp_cons and es_vocal(car_ant):
                r1 += 1
            if tiene_li:
                r2 += 1
            if men4:
                pal4 += 1

            cl = 0
            tiene_li = men4 = False

        else:
            cl += 1
            if cl == 1 and es_consonante(car):
                emp_cons = True

            if cl >= 3:
                if car_ant in "Ll" and car in "Ii":
                    tiene_li = True
            if cl < 4:
                men4 = True

        car_ant = car

    r3 = (pal4 * 100) / ctp
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
