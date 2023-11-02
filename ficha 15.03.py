# 3. Busqueda de primos
# Desarrollar un programa que permita generar un arreglo de n elementos. A partir de este arreglo, se pide lo siguiente:
#
# Generar un segundo arreglo con todos los números primos contenidos en el arreglo original.
# Determinar el promedio de los números del arreglo generado en el punto 1.


import arreglos
import math


def crear(tam):
    vec = list()
    for i in range(tam):
        dato = int(input('Ingese el valor para la posicion vec[' + str(i) + ']: '))
        vec.append(dato)
    return vec


def generar_vector_primos(vec):
    primos = []
    for item in vec:
        if es_primo(item):
            primos.append(item)
    return primos


def promedio(vec):
    tam = len(vec)
    if tam > 0:
        suma = 0
        for item in vec:
            suma += item
        return round(suma / tam, 2)
    else:
        return 0


def mostrar(vec):
    tam = len(vec)
    cadena = '['
    for pos in range(tam):
        if pos == (tam - 1):
            cadena += str(vec[pos])
        else:
            cadena += str(vec[pos]) + ' - '

    cadena += ']'
    return cadena


def validar_mayor_cero(mensage='Ingrese un numero: '):
    numero = 0
    while numero <= 0:
        numero = int(input(mensage))
        if numero <= 0:
            print('Numero incorrecto!!! El numero debe ser mayor a cero')
    return numero


def es_primo(numero):
    primo = True
    if numero % 2 == 0:
        primo = False

    else:
        tope = math.ceil(math.sqrt(numero))
        for i in range(3, tope):
            if numero % i == 0:
                primo = False
                break
    return primo



def principal():
    print('Manejo de Arreglos')
    print('=================================')

    tam = validar_mayor_cero('Ingrese el tamaño del vector: ')
    vector = crear(tam)

    print()
    print('Vector original:')
    print(mostrar(vector))

    primos = generar_vector_primos(vector)
    print()
    print('Vector con los números primos contenidos en el original:')
    print(mostrar(primos))

    prom = promedio(primos)
    print()
    print('El promedio de los números primos en el segundo vector es:', prom)


if __name__ == '__main__':
    principal()
