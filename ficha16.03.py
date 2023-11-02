# 3. Concurso de baile
# Desarrollar un programa que permita procesar el puntaje obtenido por una pareja de bailarines en un concurso de TV.
#
# Para ello, generar un vector de 7 elementos, representando a los miembros del jurado. Por cada celda, generar un valor
# aleatorio entre -1 y 10 (inclusive) indicando la puntuación recibida.
#
# A continuación, informar:
#
# Los tres mejores puntajes recibidos.
# Si algún jurado los calificó con un puntaje x ingresado por teclado. En caso afirmativo, mostrar las notas mayores a esa
# que recibieron.
# La diferencia entre el mayor y el menor puntaje.
# El puntaje total obtenido. Si es menor a 20, indicar que quedan descalificados. En caso contrario, informar como puntaje
# final el promedio de los puntos obtenidos, excluyendo los extremos.


import random
from arreglos import *


def cargar_vec(v):
    n = len(v)
    for i in range(n):
        v[i] = random.randint(-1, 10)
    return v


def buscar_binario(v, x):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


def buscar_mayores(vec, pos):
    may = list()
    n = len(vec)
    for i in range(pos + 1, n):
        if vec[i] > vec[pos]:
            may.append(vec[i])
    return may


def promedio(v):
    acum = 0
    for i in v:
        acum += i
    prom = acum / len(v)
    return prom


def mayores_x(x, vec):
    may = []
    for i in vec:
        if i > x:
            may.append(i)
    return may


def resta(v):
    men = v[0]
    may = v[-1]
    return may - men


def sumar_total(v):
    acu = 0
    for i in v:
        acu += i
    if acu < 20:
        print("quedan descalificados")

    else:
        vpt4 = v[1:-1]
        prom = promedio(vpt4)
        print("Punto 4:", prom)


def main():
    n = validar_mayor_que(0, "ingrese num mayor que 0: ")
    vec = [0] * n
    vec = cargar_vec(vec)
    ordenar_vector(vec)
    print(vec)
    vec_pto_1 = vec[n - 3:]
    print("Punto 1: los 3 mayores son: ", vec_pto_1)
    x = int(input("Ingrese un puntaje: "))
    pos = buscar_binario(vec, x)
    if pos == -1:
        print("no existe...")
    else:
        pto2 = buscar_mayores(vec, pos)
        print("Punto 2: los mayores al valor ingresado son: ", pto2)
    pto3 = resta(vec)
    print("Resta entre mayor y menor:", pto3)
    pto4 = sumar_total(vec)


if __name__ == "__main__":
    main()
