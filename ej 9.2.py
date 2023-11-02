#9. Datos de un rectángulo
#Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro y la superficie
#del mismo.


#entradas

altura = int(input("ingrese el largo del rectangulo: "))
base = int(input("ingrese el ancho del rectangulo: "))

#procesos

perimetro = (2 * base) + (2 * altura)
superficie = base * altura

#salidas

print(" el perimetro es de: ", perimetro)
print(" la superficie es de: ", superficie)
