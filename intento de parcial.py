
class Empleado:
    def __init__(self, legajo, nombre, direccion, sueldo, antiguedad):
        self.legajo = legajo
        self.nombre = nombre
        self.direccion = direccion
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def __str__(self):
        res = "legajo: " + str(self.legajo) + ", nombre: " + str(self.nombre) + \
            ", direccion" + str(self.direccion) + ", sueldo", str(self.sueldo) + \
              ", antiguedad", str(self.antiguedad)
        return res


def validar_mayor_que(minimo, mensaje):
    n = int(input(mensaje))
    while n <= minimo:
        print('INVALIDO! INGRESE OTRO')
        n = int(input(mensaje))
    return n


def read(n, vec):
    for i in range(n):
        leg = int(input("legajo[" + str(i) + "]:"))
        nom = input("nombre: ")
        direc = input("direccion: ")
        suel = float(input("sueldo: "))
        ant = int(input("antiguedad: "))
        print()

        vec[i] = Empleado(leg, nom, direc, suel, ant)
    return vec


def mostrar_vector(v):
    n = len(v)
    for i in range(n):
        print(v[i])


def menu():
    cadena = "Menú de opciones: "
    'TREN DE LA COSTA'
    '1. Mostrar los datos'
    '2. Total de pasajeros'
    '3. Estacion con mayor cantidad de pasajeros (ida)'
    '4. Estaciones sin pasajeros'
    '5. Estaciones con mas pasajeros a la ida'
    '0. Salir'
    "ingrese su opcion: "
    return int(input(cadena))


def test():

    validar_mayor_que(0, "ingrese un numero")
    n = int(input(" ingrese una opcion a procesar:"))
    vec = [0] * n
    mostrar_vector(vec)
    opcion = menu()
    while opcion != 0:
        menu()


if __name__ == "__main__":
    test()
