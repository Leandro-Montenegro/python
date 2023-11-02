# Una concesionaria de autos necesita un sistema para registrar y gestionar los trabajos que hacen en su taller.
# Por cada trabajo se conoce:
#
# - Identificador del trabajo: un entero.
# - Tipo de trabajo: un entero en el rango 100 a 350 (ambos incluídos).
# - DNI del cliente: un entero.
# - Patente del vehículo: una cadena.
# - Monto cobrado: un flotante no negativo.
#
# Se solicita un programa, comandado por menú de opciones, que permita lo siguiente:
#
# 1) Cargar un arreglo con "n" trabajos de forma manual o generando los datos aleatoriamente.
# Únicamente se debe programar una de las opciones.
#
# 2) Mostrar el arreglo ordenado por identificador de trabajo de forma ascendente.
#
# 3) Informar el monto acumulado que se cobró por cada tipo de trabajo.
#
# 4) Mostrar todos aquellos trabajos cuyo tipo sea "t" y el monto superior a "m", siendo "t" y "m" valores solicitados al usuario.
#
# 5) Informar si existe un trabajo para la patente "p", siendo "p" un valor cargado por el usuario.
# Si existe, mostrar sus datos y modificar su monto descontándole el 10%. Si no existe, informar esta situación con un mensaje.
#
# 6) Mostrar el trabajo más caro cobrado para un cliente cuyo DNI es "d", siendo "d" un valor ingresado por teclado.


import random


class Trabajos:
    def __init__(self, id, tipo, dni, patente, monto):
        self.id = id
        self.tipo = tipo
        self.dni = dni
        self.patente = patente
        self.monto = monto

    def __str__(self):
        cad = '|Identificador del trabajo: ' + str(self.id) + ' |Tipo de trabajo: ' + str(self.tipo)
        cad += ' |DNI del cliente: ' + str(self.dni) + ' |Patente del vehículo: ' + str(self.patente)
        cad += ' |Monto cobrado: $' + str(self.monto)
        return cad


def validar_mayor_que(limite, mensaje):
    numero = int(input(mensaje))
    while numero <= limite:
        print('Error!!!! El numero ingresado debe ser mayor a', limite)
        numero = int(input(mensaje))

    return numero


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


def cargar_vec(v):
    n = len(v)
    for i in range(n):
        id = random.randint(1, 100)
        tipo = random.randint(100, 350)
        dni = random.randint(20000000, 50000000)
        patente = "Patente " + str(i)
        monto = round(random.uniform(45000, 300000),2)
        v[i] = Trabajos(id, tipo, dni, patente, monto)


def selection_sort(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]


def mostrar_vec(v):
    n = len(v)
    for i in range(n):
        print(v[i])


def mostrar_vec_acu(acum):
    n = len(acum)
    for i in range(n):
        if acum[i] > 0:
            print('El tipo es', i + 100, ': ', acum[i])


def mont_acum(v, acum):
    n = len(v)
    for i in range(n):
        acum[v[i].tipo - 100] += v[i].monto


def pto_4(t, m, vec):
    n = len(vec)
    for i in range(n):
        if vec[i].tipo == t and vec[i].monto > m:
            print(vec[i])


def linear_search(p, v):
    for i in range(len(v)):
        if v[i].patente == p:
            return i
    return -1


def principal():
    opcion = -1
    n = int(input('Ingrese la cantidad de trabajos a procesar: '))
    v = [None] * n

    while opcion != 0:
        opcion = menu()

        if opcion == 0:
            print("Adios!!!")

        elif opcion == 1:
            cargar_vec(v)

        elif v is not None:
            if opcion == 2:
                selection_sort(v)
                mostrar_vec(v)

            elif opcion == 3:
                acum = [0] * 251
                mont_acum(v, acum)
                mostrar_vec_acu(acum)

            elif opcion == 4:

                t = int(input('Ingrese el tipo de trabajo que busque: '))
                m = float(input('Monto a superar: '))
                print('Punto 4: ')
                print(pto_4(t, m, v))

            elif opcion == 5:
                p = int(input("ingrese una patente para ver si existe: "))
                linear_search(p, v)
            elif opcion == 6:
                pass

        else:
            print("Primero debe ejecutar la opcion 1")


if __name__ == "__main__":
    principal()
