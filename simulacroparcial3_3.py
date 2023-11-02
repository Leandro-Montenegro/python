# Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta se registran los
# siguientes datos: el número de factura, importe de la factura, el tipo de factura (A, B, C o E), el apellido de la
# persona que realiza la compra, y el tipo del perfume vendido (un número entero para indicar su marca, entre 1 y 17,
# por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.). Se desea almacenar la información referida a las ventas que realiza
# la perfumería en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que
# permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de n ventas realizadas. Valide que el importe de la factura sea mayor a 0 y
# menor a 200000. Valide que el tipo de factura sea alguno de los tipos válidos: A, B, C o E, y valide también que el tipo
# de perfume sea un número entero entre 1 y 17 ambos incluidos. Puede hacer la carga en forma manual, o puede generar los
# datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una
# debe programar.
#
# 2- Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea distinto de
# t (x y t son valores que se cargan por teclado). El listado debe salir ordenado de mayor a menor según los apellidos
# de las personas que realizaron la compra.
#
# 3- Determinar y mostrar el importe total facturado para cada uno de los 17 tipos posibles pero informe por pantalla
# solamente el total facturado correspondiente al tipo de perfume z (cargar el número z por teclado).
#
# 4- Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de perfume se
# encuentre entre 5 y 12 y que no sean con factura de tipo C. Si no existe ninguna venta que cumpla con ese criterio
# informarlo por pantalla.
#
# 5- Determinar si existe una venta cuyo número de factura sea igual a n (cargar n por teclado) y cuyo importe de factura
# sea menor a a un valor p que se carga por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.


import random


class Perfumeria:
    def __init__(self, numero, importe, tipo, apellido, tipoperf):
        self.numero = numero
        self.importe = importe
        self.tipo = tipo
        self.apellido = apellido
        self.tipoperf = tipoperf

    def __str__(self):
        r = "numero: " + str(self.numero) + ", importe: " + str(self.importe) + ", tipo: " + str(self.tipo)
        r += ", apellido: " + str(self.apellido) + ", tipoperf: " + str(self.tipoperf)
        return r


def validar_importe(minimo, maximo):
    num = minimo - 1
    while num < minimo or num > maximo:
        num = int(input("ingrese un numero"))
        if num < minimo or num > maximo:
            print("el numero debe ser mayor a ", minimo, "y menor a", maximo)
    return num


def mostrar_datos_por_rango_perfume(v, tp_minimo, tp_maximo):
    print('Listado de datos de Facturas')
    for i in v:
        if tp_minimo <= i.tipoperf <= tp_maximo:
            cad = f'Nro Factura {i.numero} - Comprador: {i.apellido} - Importe ${i.importe:.2f}'
            print(cad)


def validar(minimo, mensaje="ingresa el tamaño del vec: "):
    n = int(input(mensaje))
    while n < minimo:
        int(input(mensaje))
    return n


def validar_tipo_factura(mensaje='Ingrese su opcion: ', *args):
    tipo = ''
    while tipo not in args:
        tipo = input(mensaje)
        if tipo not in args:
            print(f'El tipo de factura es invalido!!! Solo se permiten {args}')
    return tipo


def acumular(v):
    res = [0] * 17
    for i in v:
        res[i.tipoperf - 1] += i.importe
    return res


def read(v):
    n = len(v)
    for i in range(n):
        numero = i + 1
        importe = random.uniform(0, 200000)
        tipo = random.choice(("A", "B", "C", "D"))
        apellido = crear_nombre()
        tipoperf = random.randint(1, 17)
        v[i] = Perfumeria(numero, importe, tipo, apellido, tipoperf)


def menu():
    print("MENU DE OPCIONES: ")
    print("opcion1 - Cargar el arreglo pedido con los datos de n ventas realizadas.")
    print("opcion2 - Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo"
          " de la factura sea distinto de t")
    print("opcion3 - Determinar y mostrar el importe total facturado para cada uno de los 17 tipos posibles ")
    print("opcion4 - Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de "
          "perfume se encuentre entre 5 y 12 y que no sean con factura de tipo C")
    print("opcion5 - Determinar si existe una venta cuyo número de factura sea igual a n")
    print("opcion6 - salir")
    return menu


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].apellido < v[j].apellido:
                v[i], v[j] = v[j], v[i]


def busqueda(v, n, p):
    pos = -1
    for i in range(len(v)):
        if v[i].importe < p and v[i].numero == n:
            pos = i
            break
    return pos


def mostrar(v, x, t):
    ordenar(v)
    n = len(v)
    for i in range(n):
        if v[i].importe > x and v[i].tipo != t:
            print(v[i])


def crear_nombre():
    nombres = 'Juan Socarron', 'Carlos Corredor', 'Laura Visor', 'Andrea Ovalo', 'Maria Andaluces'
    return random.choice(nombres)


def main():
    opc = -1
    v = [None]
    carga = False
    while opc != 6:
        menu()
        opc = int(input("ingrese una opcion: "))
        if opc == 1:
            n = validar(0, "ingresa el tamaño del vector: ")
            v = [0] * n
            read(v)
            carga = True
        else:
            if not carga:
                print("Cargue el vector")
            else:
                if opc == 2:
                    x = validar_importe(0, 200000)
                    t = validar_tipo_factura("ingrese  el tipo de factura a excluir: ", "A", "B", "C", "D")
                    ordenar(v)
                    mostrar(v, x, t)
                if opc == 3:
                    res = acumular(v)
                    z = validar_importe(1, 17)
                    print(f'El monto total facturado para el tipo de perfume {z} es ${res[z - 1]:.2f}')
                if opc == 4:
                    mostrar_datos_por_rango_perfume(v, 5, 14)
                if opc == 5:
                    n = int(input("numero de factura a buscar: "))
                    p = float(input("ingrese importe: "))
                    pos = busqueda(v, n, p)
                    if pos is None:
                        print("no existe")
                    else:
                        print(v[pos])
        if opc == 6:
            print("salir.")


if __name__ == "__main__":
    main()
