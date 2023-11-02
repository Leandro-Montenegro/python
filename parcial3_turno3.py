from class_parcial import *
import random


def menu():
    print("\nMENU DE OPCIONES:")
    print("opcion 1 - Cargar el arreglo.")
    print("opcion 2 - Mostrar los datos.")
    print("opcion 3 - c. Determinar cuántos errores se produjeron en el rango de cada una de las horas posibles. ")
    print("opcion 4 - Determinar si existe un error")
    print("opcion 5 - salir. ")


def mensaje():
    mensajes = random.randint(0, 23)
    avisos = str(mensajes)
    return avisos


def read(v):
    for i in range(len(v)):
        codigo = random.randint(1000, 5000)
        numero = i + 1
        mensajes = mensaje()
        horas = random.randint(0, 23)
        segundos = random.randint(1, 59)
        v[i] = Error(codigo, numero, mensajes, horas, segundos)
    return v


def mostrar(v, s1, s2):
    ordenar(v)
    n = len(v)
    acum = 0
    for i in range(n):
        if s1 <= v[i].segundos <= s2:
            print(v[i])
            acum += 1
    print(acum)


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def validar(minimo, mensaje="ingrese cantidad de elementos: "):
    n = int(input(mensaje))
    while n < minimo:
        print("error")
        if n < minimo:
            int(input(mensaje))
    return n


def acum(v):
    res = [0] * 24
    may = 0
    for i in range(len(v)):
        res[v[i].horas] += 1
    for i in range(len(res)):
        if res[i] != 0:
            print("cantidad de errores en el rango: ", i, ":", res[i])
            if may is None or may < res[i]:
                may = res[i]
    print(may)


def busqueda(v, num, des):
    existe = False
    for i in range(len(v)):
        if v[i].numero == num and v[i].mensajes == des:
            print(v[i])
            break
    if not existe:
        print("no existe.")


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
                print("cargue el vector...")
            else:
                if opc == 2:
                    s1 = int(input("ingrese segundos minimos:"))
                    s2 = int(input("ingrese segundos maximos:"))
                    mostrar(v, s1, s2)
                if opc == 3:
                    acum(v)

                if opc == 4:
                    num = int(input("ingrese num a buscar: "))
                    des = input("ingrese mensaje a buscar: ")
                    busqueda(v, num, des)

        if opc == 5:
            print("salir")


if __name__ == '__main__':
    main()


