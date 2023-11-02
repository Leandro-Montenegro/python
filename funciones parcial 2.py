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


def porcentaje(total, parcial):
    porc = 0
    if total != 0:
        porc = (parcial * 100) / total
    return porc


def promedio(suma, cantidad):
    promedio = 0
    if cantidad != 0:
        promedio = suma / cantidad
    return promedio


# definir funcion principal
def main():
    # cargar cadena
    texto = input("ingrese cadena")
    # variables
    cp = cl = 0
    # recorrer cadena
    for car in texto:
        #analizar dentro de la palabra
        if car != "" and car != "":
            cl += 1
        #analizar fuera de la palabra
        else:
            cp += 1
        # reset de variables
        cl = 0
    # calculos finales
    # mostrar resultados


# invocar a la funcion principal
if __name__ == "__main__":
    main()
