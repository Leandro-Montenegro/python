# 5. Mayores al promedio
# Ingresar por teclado un arreglo unidimensional de n números enteros, siendo n una variable que se ingresa por teclado. Se pide:
#
# Calcular el valor promedio entre los números ingresados en el vector.
# Determinar la cantidad de números del vector que son mayores al promedio.


import arreglos


def contar_mayores(vec, prom):
    cont = 0
    for i in range(len(vec)):
        if vec[i] > prom:
            cont += 1
    return cont


def read(vec):
    for i in range(len(vec)):
        vec[i] = int(input("Ingrese el elemento vec["+str(i)+"]: "))


def main():
    n = arreglos.validar_mayor_cero("ingrese un numero mayor a cero: ")
    v = n * [0]
    vec = arreglos.crear(n)

    prom = arreglos.promedio(vec)
    cont = contar_mayores(vec, prom)

    print("Promedio de valores:", prom)
    print("Cantidad de valores mayores al promedio:", cont)


if __name__ == "__main__":
    main()
