#1. Cuadrados y cubos
#Leer dos números y calcular:
#La suma de sus cuadrados.
#El promedio de sus cubos.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
suma = (num1 ** 2) + (num2 ** 2)
promedio = ((num1 ** 3) + (num2 **3)) / 2
print("La suma de sus cuadrados es: ", suma)
print("El promedio de sus cubos es : ", promedio)
