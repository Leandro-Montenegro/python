#3. Importe como cadena
#Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma flotante
#y muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer precedida por el signo '$' y
#en el otro debe aparecer precedida por la palabra "pesos".

importe = float(input("ingrese cantidas de dinero: "))
print("$", importe)
print(importe, "pesos")
