# Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos. Por cada
# trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o nombre del mismo,
# el tipo de trabajo (un valor de 0 a 3, 0: interior, 1: exterior, 2: piletas, 3: tapizados), el importe a cobrar por
# ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la información referida
# a los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
# 1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo
# y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual, o puede generar los datos en forma
# automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
# 2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
# 3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay varios
# trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).
# 4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado. Si existe,
# mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros
# de búsqueda, debe mostrar sólo el primero que encuentre.
# 5- Determinar y mostrar la cantidad de trabajos por tipo.

import random


class Trabajo:
    def __init__(self, numero, descripcion, tipo, importe, personal):
        self.numero = numero
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.personal = personal

    def __str__(self):
        r = "numero: " + str(self.numero) + ", descripcion: " + str(self.descripcion) + ", tipo: " + str(self.tipo)
        r += ", importe: " + str(self.importe) + ", personal: " + str(self.personal)
        return r


def menu():
    print("MENU DE OPCIONES:")
    print("opcion 1 - Cargar el arreglo pedido con los datos de los n trabajos. ")
    print("opcion 2 - Mostrar todos los datos de todos los trabajos. ")
    print("opcion 3 -Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado. ")
    print("opcion 4 - Determinar si existe un trabajo cuya descripción sea igual a d. ")
    print("opcion 5 - Determinar y mostrar la cantidad de trabajos por tipo. ")
    print("opcion 6 - salir.")


def mostrar_vec(v):
    n = len(v)
    for i in range(n):
        print(v[i])


def cargar_vec(v):
    n = len(v)
    for i in range(n):
        numero = i
        descripcion = str(i)
        tipo = random.randint(0, 3)
        importe = round(random.uniform(0, 100000), 2)
        personal = random.randint(1, 50)
        v[i] = Trabajo(numero, descripcion, tipo, importe, personal)


def validar(minimo, mensage):
    n = int(input(mensage))
    while n <= minimo:
        print("ingrese otro")
        n = int(input(mensage))
    return n


def ordenamiento(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].importe < v[j].importe:
                v[i], v[j] = v[j], v[i]


def may_personal(v):
    mayor = v[0]
    for i in range(1, len(v)):
        if mayor is None or v[i].personal > mayor.personal:
            mayor = v[i]
    return mayor


def linear_search(d, v):
    n = len(v)
    for i in range(n):
        if v[i].descripcion == d:
            return i
    return -1


def trabajos_tipo(v):
    conteo = [0] * 4
    for i in range(len(v)):
        pos = v[i].tipo
        conteo[pos] += 1

    for i in range(len(conteo)):
        if conteo[i] > 0:
            print("tipo: ", i, "cantidad: ", conteo[i])


def main():
    v = []
    opcion = -1
    carga = False
    while opcion != 6:
        menu()
        opcion = int(input("ingrese una opcion: "))
        if opcion == 1:
            n = validar(0, "ingrese un numero: ")
            v = [None] * n
            cargar_vec(v)
            carga = True
        else:
            if not carga:
                print("debe cargar primero...")
            else:
                if opcion == 2:
                    ordenamiento(v)
                    mostrar_vec(v)

                elif opcion == 3:
                    print("trabajo con mayor cantidad de personal: ")
                    print(may_personal(v))
                if opcion == 4:
                    d = input("ingrese la descripcion a buscar: ")
                    pos = linear_search(d, v)
                    if pos == -1:
                        print("no se encontró...")
                    else:
                        print("encontrado")
                        print(v[pos])
                if opcion == 5:
                    trabajos_tipo(v)
        if opcion == 6:
            print("hasta luego")


if __name__ == "__main__":
    main()
