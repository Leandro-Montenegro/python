import random


def promedio(vec):
    cant = len(vec)
    acu = 0
    for i in range(cant):
        acu += vec[i]
    prom = acu / cant
    return prom


def buscar_mayor(v):
    may = 0
    for i in range(1, len(v)):
        if v[i] > v[may]:
            may = i
    return may


def sumar_vector(v):
    suma = 0
    for i in range(len(v)):
        suma += v[i]
    return suma


def contar_valores(v, x):
    cant = 0
    for i in range(len(v)):
        if v[i] == x:
            cant += 1
    return cant


def cargar_vec(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input('Ingese el valor para la posicion vec[' + str(i) + ']: '))
    return v


def ordenar_vector(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i + 1, n):
            if vec[i] > vec[j]:
                vec[i], vec[j] = vec[j], vec[i]


def linear_search(v, x):
    for i in range(len(v)):
        if x == v[i]:
            return True
    return False


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


def validar_mayor_que(minimo, mensaje):
    n = int(input(mensaje))
    while n <= minimo:
        print('INVALIDO! INGRESE OTRO')
        n = int(input(mensaje))
    return n


def es_impar(v,x):
    cant = 0
    for i in range(len(v)):
        if v[i] % 2 != 0 and v[i] > x:
            cant += 1
        return cant


def menu():
    cadena = 'Menu de Opciones:\n' + \
    '===========================================\n' + \
    '1 - Cargar trabajaos \n' + \
    '2 - Mostrar datos ordenados por identificador \n' + \
    '3 - Monto acumulado por tipo \n' + \
    '4 - Mostrar trabajos con filtro (tipo y monto) \n' + \
    '5 - Buscar trabajo por patente \n' + \
    '6 - Mostrar trabajo mas caro \n' + \
    '0 - Salir \n' + \
    'Ingrese su opcion: '
    return int(input(cadena))


class Empleado:
    def __init__(self, legajo, nombre, direccion, sueldo, antiguedad):
        self.legajo = legajo
        self.nombre = nombre
        self.direccion = direccion
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def __str__(self):
        res = "legajo: " + str(self.legajo) + ", nombre: " + str(self.nombre)
        res += ", direccion" + str(self.direccion) + ", sueldo", str(self.sueldo)
        res += ", antiguedad", str(self.antiguedad)
        return res

