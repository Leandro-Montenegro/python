#8. Perímetro de un cuadrado
#Desarrollar un programa que, conociendo el valor del área (o superficie) de un cuadrado, obtenga y muestre el valor del
#perímetro de ese cuadrado.

area = float(input("ingrese valor del area: "))
lado = pow(area, 0.5)
perimetro = 4 * lado
print(" el valor del perimetro es de: ", perimetro)
