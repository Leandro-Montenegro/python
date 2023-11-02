# 2. Último y Primero
# Desarrollar un programa que permita cargar por teclado un vector de n elementos y luego:
#
# Informe cuántas veces se repite en el vector el último número ingresado
# Genere un nuevo vector, conteniendo sólo los elementos menores al primer valor ingresado.


def validar_tamanio():
    n = int(input("ingrese el tamaño del vector: "))
    while n < 0:
        n = int(input(" el tamaño debe ser mayor a 0"))
    return n


def crear (tam):
    v = []
    for i in range(tam):
        dato = int(input("ingrese v[" + str(i) + "]: "))
        v.append(dato)
    return v


def contar_repeticiones(v):
    repeticiones = 0
    for elemento in v:
        if elemento == v[-1]:
            repeticiones += 1
    return repeticiones


def buscar_menores(v):
    menores = list()
    for elemento in v:
        if elemento < v[0]:
            menores.append(elemento)
    return menores
