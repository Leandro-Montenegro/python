# Una academia de inglés para niños de escolaridad primaria y nivel inicial, desea un programa para procesar los datos
# de sus alumnos. Por cada alumno se tienen los siguientes datos: DNI del alumno, el nombre del alumno, el apellido del
# alumno, DNI del Tutor (adulto responsable del niño), el importe de la cuota y el nivel en el que cursa el niño (un valor entre 0 y 12 incluidos, de la forma 0: Inicial, 1: Primer Junior, 2: Primer Younger, etc.). Se desea almacenar la información referida a los n alumnos en un arreglo de objetos de clase Alumno (definir la clase Alumno y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de los n alumnos. Valide que el número de nivel sea un valor entre 0 y 12
# (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar todos los datos de todos los alumnos, en un listado ordenado de menor a mayor según el apellido del alumno.
#
# 3- Usando el arreglo creado en el punto 1, determine la cantidad de alumnos que cursan en cada nivel (o sea, 13 contadores).
# Muestre sólo los resultados diferentes de 0.
#
# 4- Determinar el monto total que debe abonar el Tutor con número de DNI igual a x, siendo x un valor que se carga por teclado
# (sumar los importes de las cuotas de los niños que el Tutor tiene a su cargo).
#
# 5- Determinar si existe un alumno con un apellido que sea igual a x (siendo x un valor que se carga por teclado).
# Si existe, modificar el importe de su cuota con un descuento del 10 % y mostrar los datos actualizados del alumno.
# Si no existe, informar con un mensaje. Si existe más de un objeto que coincida con esos parámetros de búsqueda,
# debe mostrar sólo el primero que encuentre.


import random


class Servicio:
    def __init__(self, codigo, cliente, tipo, monto ):
        self.codigo = codigo
        self.cliente = cliente
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        r = "codigo: " + str(self.codigo) + ", cliente: " + str(self.cliente)
        r += ", tipo: " + str(self.tipo) + ", monto: " + str(self.monto)
        return r

def menu():
    print("MENU DE OPCIONES:")
    print("OPCION 1 - :")
    print("OPCION 2 - :")
    print("OPCION 3 - :")
    print("OPCION 4 - :")
    print("OPCION 5 - : ")


def read(v):
    for i in range(len(v)):
        codigo = i + 1
        cliente = clientes()
        tipo = random.randint(1, 10)
        monto = random.uniform(1, 1000)
        v[i] = Servicio(codigo, cliente, tipo, monto)
    return v


def clientes():
    nombres = "juan", "pepito", "raul", "gisell", "antonela"
    return random.choice(nombres)


def acum(v):
    res = [0] * 10
    for i in range(len(v)):
        res[v[i].tipo - 1] += 1
    for i in range(len(res)):
        if res[i] != 0:
            print("tipo", i + 1, ", servicios", res[i])


def busqueda(v, nom):
    existe = False
    suma = 0
    for i in range(len(v)):
        if v[i].cliente == nom:
            existe = True
            if existe:
                res = v[i].importe + 2000
                return res
        else:
            if not existe:
                print("no existe.")
                break


def validar(min, mensaje="ingrese tamaño: "):
    n = int(input(mensaje))
    while n <= min:
        if n <= min:
            print("error")
            return n
    return n


def mostrar(v, i1, i2):
    cont = 0
    for i in range(len(v)):
        if i1 <= v[i].monto <= i2:
            print(v[i])
            cont += 1
    print(cont)


def ordenar(v):
    n = len(v)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def mostrar_pto5(v):
    n = len(v)
    for i in range(n):
        print(v[i])


def main():
    opc = -1
    v = [None]
    carga = False
    while opc != 5:
        menu()
        opc = int(input("ingrese una opcion: "))
        if opc == 1:
            n = validar(0)
            v = [0] * n
            read(v)
            carga = True
        else:
            if not carga:
                print("cargue el vec: ")
            else:
                if opc == 2:
                    i1 = int(input("ingrese minimo: "))
                    i2 = int(input("ingrese maximo: "))
                    ordenar(v)
                    mostrar(v, i1, i2)
                if opc == 3:
                    acum(v)
                if opc == 4:
                    v = []
                    nom = input("ingrese nombre: ")
                    v = busqueda(v, nom)
                    mostrar_pto5(v)
        if opc == 5:
            print("adios. ")


if __name__ == "__main__":
    main()
