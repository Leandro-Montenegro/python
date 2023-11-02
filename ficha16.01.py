# 1. Ordenar y buscar
# Se pide un programa que cargue n elementos numéricos aleatorios entre 1 y 100 inclusive (pueden existir duplicados).
# A partir de ese arreglo:
#
# Ordenarlo de forma ascendente y mostrarlo
# Buscar un elemento x dentro del arreglo (x se ingresa por teclado). Si no existe, informarlo. Si existe, determinar
# cuántos valores impares mayores a x se encontraron en el arreglo.


from arreglos import *
import random


def test():

    n = validar_mayor_que(0, "ingrese num mayor a 0: ")
    v = [0] * n
    a = cargar_vec(v)
    print("vector", a)
    ordenar_vector(a)
    print("vector ordenado", a)
    x = int(input("ingrese numero a buscar: "))
    b = linear_search(a, x)
    print(b)
    c = es_impar(a, x)
    print(c)


if __name__ == "__main__":
    test()
