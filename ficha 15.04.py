# 4. Mayores con el mismo índice
# Cargar por teclado dos vectores de tamaño n y, a partir de ellos, generar un tercer vector que contenga, para cada
# componente, el mayor valor entre las componentes homólogas (mismo índice) de los otros dos vectores.
#
# Por ejemplo, si se cargan los siguientes vectores a y b:
#
# a = [3, 4, 6]
#
# b = [8, 5, 1]
#
# El resultado sería:
#
# c = [8, 5, 6]

import arreglos


def elegir_mayores(a,b):
    c = [0] * len(a)
    for i in range(len(a)):
        if a[i] > b[i]:
            c[i] = a[i]
        else:
            c[i] = b[i]
    return c

def cargar(tam):
    v = []
    for i in range(tam):
        dato = int(input('Ingrese v[' + str(i) + ']: '))
        v.append(dato)
    return v

def test ():
    n = 3
    v = [0] * n
    a = arreglos.crear(n)
    b = arreglos.crear(n)
    c = elegir_mayores(a, b)
    print("arreglo a: ", a)
    print("arreglo b: ", b)
    print("arreglo c: ", c)


if __name__ == "__main__":
    test()
