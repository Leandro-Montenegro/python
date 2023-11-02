#Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero
# sabiendo que su altura es igual al cuadrado de la base.


base = float(input("ingrese base: "))
altura = base ** 2

área = (base * altura) / 2
print(f"el area es de{área}")
