#5. Conversión de medidas
#Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

#yardas
#pulgadas
#centímetros
#metros
#Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros.

pies = float(input("ingrese cantidad de pies: "))
yardas = pies / 3
pulgadas = pies * 12
centimetros = 2.54 * 12 * pies
metros = centimetros / 100

print(pies, "pies son: ", yardas, "yardas")
print(pies, "pies son: ", pulgadas, "pulgadas")
print(pies, "pies son: ",centimetros, "cm")
print(pies, "pies son: ", metros, "m")
