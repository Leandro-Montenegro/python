#6. Precio de venta
#Conociendo el precio de lista de un artículo, determinar:
#Precio de venta al contado (10% de descuento)
#Precio de venta con tarjeta (5% de recargo)

#Entradas

precio = float(input("ingrese el precio de lista de un artículo: "))

#procesos

descuento_contado = precio * 0.10
recargo_efectivo = precio * 0.05
precio_contado = precio - descuento_contado
precio_efectivo = precio + recargo_efectivo

#salidas

print("el precio de venta al contado es de : ", precio_contado, "dolares")
print("el precio de venta al contado es de : ", precio_efectivo, "dolares")
