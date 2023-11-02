#11. Palabra enmascarada
#Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la primer
# letra y la última, pero reemplazando los caracteres intermedios por asteriscos.

#Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.

#Carga de datos

palabra = input("ingrese un palabra a enmascarar: ")
#procesos

n = len(palabra)
asteriscos = "*" * (n-2)
enmascarada = palabra[0] + asteriscos + palabra[n-1]

# Resultados
print("La palabra enmascarada es:", enmascarada)
