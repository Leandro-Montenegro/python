#9. Área de un rectángulo
#Desarrollar un programa que, conociendo el valor del perímetro de un rectángulo y el valor de uno de los lados de ese
#rectángulo, calcule y muestre el valor del área (o superficie) de ese rectángulo.



perimetro = float(input("ingrese perimetro del rectangulo: "))
lado1 =  float(input("ingrese valor del lado del rectangulo: "))
lado2 = (perimetro - 2*lado1) / 2
superficie = lado1 * lado2
print("la superficie es de", superficie )
