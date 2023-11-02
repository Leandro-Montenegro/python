#7. Precio del boleto
#Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo del mismo se debe
#considerar el monto base (que se cobra siempre), más un valor extra calculado en base a la cantidad de kilómetros
#a recorrer:  Por cada kilómetro a recorrer se cobra $0.30 de adicional.

monto_base = int( input("ingrese el monto base: "))
km = int( input("ingrese la cantidad de km: "))
adicional = 0.30
valor_extra = km * adicional
precio = monto_base + valor_extra
print(" el precio del boleto es de:", precio, "pesos")
