#13. Triángulo Rectángulo
#Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

#Valor de la hipotenusa (redondeado a 2 decimales)
#Valor del lado mayor
#Valor del lado menor

# Titulo y carga de datos
print('Triangulo rectangulo')
print()
cat1 = int(input('Ingrese uno de los catetos: '))
cat2 = int(input('Ingrese el otro cateto: '))

#Proceso
suma = pow(cat1,2) + pow(cat2,2)
hip = round(pow(suma,0.5),2)

#Resultados
print('\nLa hipotenusa es',hip)
print('El lado mayor es',max(cat1,cat2))
print('El lado menor es',min(cat1,cat2))
