import random


class Academia:
    def __init__(self, numero, cliente, tipo, monto):
        self.numero = numero
        self.cliente = cliente
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        r = "numero: " + str(self.numero) + ", cliente:" + str(self.cliente)
        r += ", tipo:" + str(self.tipo) + ", monto: " + str(self.monto)
        return r


def clientes():
    nombres = "Juan", "pepito", "raul", "jhoana"
    return random.choice(nombres)


def busqueda(v, nom):
    for i in range(len(v)):
        if v[i].cliente == nom:
            print("numero de identificacion:", v[i].numero, "monto", v[i].monto)
            break
        else:
            print("no existe")
            break



def menu():
    print("MENU DE OPCIONES: ")
    print("opcion 1 - ")
    print("opcion 2 - ")
    print("opcion 3 - ")
    print("opcion 4 - ")
    print("opcion 5 - ")


def mostrar(v):
    acum = 0
    for i in range(len(v)):
        print(v[i])
        acum += v[i].monto
    print("a suma de los montos a pagar de todos los paseos que se mostraron: ", acum)


def validar(minimo, mensaje= "ingrese tamaño"):
    n = int(input(mensaje))
    while n <= minimo:
        print("error")
        if n <= minimo:
            int(input(mensaje))
    return n


def read(v):
    for i in range(len(v)):
        numero = i + 1
        cliente = clientes()
        tipo = random.randint(0, 19)
        monto = random.uniform(1000, 10000)
        v[i] = Academia(numero, cliente, tipo, monto)
    return v


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].numero > v[j].numero:
                v[i], v[j] = v[j], v[i]


def acum(v):
    acumulador = [0] * 20
    for i in range(len(v)):
        pos = v[i].tipo
        acumulador[pos] += v[i].monto
    return acumulador


def mostrar_acum(v, c):
    for i in range(len(v)):
        if v[i] > c:
            print("pos ", i, ":", v[i])


def main():
    opc = -1
    v = [None]
    while opc != 5:
        menu()
        opc = int(input("ingrese una opcion: "))
        if opc == 1:
            n = validar(0, "ingrese tamaño del vec:")
            v = [0] * n
            read(v)
        if opc == 2:
            ordenar(v)
            mostrar(v)
        if opc == 3:
            c = int(input("ingresa num: "))
            res = acum(v)
            mostrar_acum(res, c)
        if opc == 4:
            nom = input("ingrese nombre: ")
            busqueda(v, nom)
        if opc == 5:
            print("salir")


if __name__ == "__main__":
    main()
