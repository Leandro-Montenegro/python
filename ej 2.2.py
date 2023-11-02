#2. Descuento en medicinas
#Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
#(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento del 35%.
#Mostrar el precio actual, el monto del descuento y el monto final a pagar.

medicamento = float(input(" ingrese el precio del medicamento: "))
descuento = (medicamento * 0.35)
precio_final = medicamento - descuento
print("el precio de ese medicamento es de", medicamento)
print("el descuento es de: ", descuento)
print("el precio final es de: ", precio_final )
