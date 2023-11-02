# 3. Multas de tránsito
# Se necesita desarrollar un programa que permita procesar n multas de tránsito labradas durante el último fin de semana
# en las diferentes rutas de la provincia. De las multas solo se necesita conocer un código el cual es un valor comprendido
# entre 1 y 20  (ambos incluidos). Por lo tanto cada elemento del arreglo contendrá un valor numérico de ese rango.
# Adicionalmente se sabe que a la hora de sacar estadísticas e importes a cobrar las multas se dividen en cinco categorías
# o cinco tipos de multas, por lo tanto los código de las multas se distribuyen en las cinco categorías de la siguiente manera:
#
# Los códigos que terminen en 1 y 6 pertenecen a la categoría 1
# Los códigos que terminen en 2 y 7 pertenecen a la categoría 2
# Los códigos que terminen en 3 y 8 pertenecen a la categoría 3
# Los códigos que terminen en 4 y 9 pertenecen a la categoría 4
# Los códigos que terminen en 5 y 0 pertenecen a la categoría 0
# Antes de realizar cualquier operación usted debe cargar el vector de infracciones con los n códigos de multas labradas
# y el vector con los importes que cada tipo de multa (5 valores), una vez cargados:
#
# Generar un tercer vector con los Importes totales facturados por tipo de infracción.
# Determinar el código de infracción que más apareció en las multas y la cantidad de multas labradas para dicho código.
# Informar el importe total facturado durante el fin de semana.


import random

class Trabajo:
    def __init__(self, numero, descripcion, tipo, importe,cantidad):
        self.numero = numero
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.cantidad = cantidad

    def __str__(self):
        r = "numero: " + str(self.numero) + ", descripcion: " + str(self.descripcion) + ", tipo: " + str(self.tipo)
        r += ", importe: " + str(self.importe) + ", personal: " + str(self.cantidad)
        return r


# definicion de funciones
def mostrar_menu():
    print("\nMenu: ")
    print("-" * 20)
    print("1. Cargar datos")
    print("2. Listado ordenado")
    print("3. Conteo por tipo")
    print("4. Mayores al promedio")
    print("5. Búsqueda por número")
    print("6. Salir ")


# -----------------------------------------------------
# validar un valor positivo
def validar_n():
    n = int(input("Ingrese la cantidad de elementos: "))
    while n <= 0:
        n = int(input("ERROR, Ingrese la cantidad de elementos: "))
    return n


# -----------------------------------------------------
# cargar el vector
def cargar_vector(n, vec):
    for i in range(n):
        # generar datos
        numero = (i+1)
        descripcion = "trabajo "+ str(numero)
        tipo = random.randint(0,19)
        importe = round(random.uniform(1000, 10000),2)
        cantidad = random.randint(1,5)

        # crear el registro
        trabajo = Trabajo(numero, descripcion, tipo, importe, cantidad)

        # grabarlo en el vector
        vec.append(trabajo)


# -----------------------------------------------------
# ordenar el vector de mayor a menor por numero
def ordenar(vec):
    n = len(vec)
    # ciclo del orden del pivot
    for i in range(0, n-1):
        # ciclo para comparar con el pivot
        for j in range(i+1, n):
            # comparar los numeros de cada registro para ver si hay que intercambiar
            if vec[i].numero < vec[j].numero:
                # intercambiar los registros completos, (cuidado con cambiar solo un campo que está mal)
                vec[i], vec[j] = vec[j], vec[i]


# -----------------------------------------------------------------------------------------------------------
# mostrar el vector
def mostrar_vector(vec):
    # sumatoria de importes
    suma = 0
    # ordenar vector
    ordenar(vec)
    # recorrer y mostrar
    print("Trabajos con cantidad de personal mayor a 3")
    for trabajo in vec:
        # validar que la cantidad sea mayor 3
        if trabajo.cantidad > 3:
            # mostrar el trabajo
            print(trabajo)
            # acumular el valor del importe del trabajo
            suma += trabajo.importe

    # mostrar el resultado
    print("La suma de los importes es:", suma)
    print()


# -----------------------------------------------------------------------------------------------------------
# conteo por tipo.
def punto_3(vec):
    # definir el vector de contadores
    vec_conteo = [0] * 20

    for i in range(len(vec)):
        # obtener la posicion a donde contar
        pos = vec[i].tipo
        # conteo
        vec_conteo[pos] += 1

    print("Cantidad de trabajos por tipo")
    for i in range(len(vec_conteo)):
        if vec_conteo[i] > 0:
            print("Tipo de trabajo:", i, " - Cantidad:", vec_conteo[i])
    print()


# -----------------------------------------------------------------------------------------------------------
# mayores al promedio
def promedio(vec):
    prom = 0
    suma = 0
    cant = len(vec)
    for trabajo in vec:
        suma += trabajo.importe

    if cant != 0:
        prom = suma / cant

    return prom


def punto_4(vec):
    prom = promedio(vec)
    # recorrer el vector para comparar con el promedio
    for trabajo in vec:
        if trabajo.importe > prom:
            print(trabajo)
    print()


# -----------------------------------------------------------------------------------------------------------
# búsqueda
def punto_5(vec, num, t):
    # busqueda secuencial
    # resultado de busqueda: el indice
    res = None

    for i in range(len(vec)):
        if vec[i].numero == num and vec[i].tipo == t:
            res = i
            break

    return res


# -----------------------------------------------------------------------------------------------------------
# funcion principal
def main():
    vec = []
    # menu de 6 opciones
    op = 0
    while op != 6:
        mostrar_menu()
        op = int(input("Ingrese su opción: "))
        # evaluar las opciones
        if op == 1:
            # pedir la cantidad de elementos
            n = validar_n()
            # cargar el arreglo
            cargar_vector(n, vec)

        elif op == 2:
            if vec != []:
                mostrar_vector(vec)
            else:
                print("El vector no esta cargado")

        elif op == 3:
            if vec != []:
                punto_3(vec)
            else:
                print("El vector no esta cargado")

        elif op == 4:
            if vec != []:
                punto_4(vec)
            else:
                print("El vector no esta cargado")

        elif op == 5:
            if vec != []:
                # ingresar la clave de busqueda
                numero = int(input("Ingrese un numero a buscar: "))
                t = int(input("Ingrese el tipo a buscar: "))
                # buscar
                res = punto_5(vec, numero, t)

                # mostrar el resultado de la busqueda
                if res is None:
                    print("No se encontro lo buscado")
                else:
                    print("Se encontro el trabajo ", str(vec[res]))

            else:
                print("El vector no esta cargado")

        elif op == 6:
            print("Salir del programa")


# invocacion a la funcion principal
if __name__ == '__main__':
    main()
