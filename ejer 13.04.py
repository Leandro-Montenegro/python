"""13. Calculo de Precios con Descuento
Una empresa nos solicito un programa que nos permita calcular los precios de los productos que vende al publico
para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendio y si se pago en efectivo o no.
En base a esto determinar

    1) El Precio final sin descuentos del articulo (precio unitario por cantidad)

    2) Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del 15%
    caso contrario solo aplicar un 5% de descuento"""

print('Calculo de Precio de Venta')
print('=' * 60)

precio_unitario = float(input('Ingrese el precio unitario del articulo: '))
cantidad = int(input('Ingrese la cantidad que se vendio del producto: '))
es_efectivo = input('La venta del articulo, se abono en efectivo? (Responda S o N): ')

print('...Procesando')
precio = precio_unitario * cantidad

if es_efectivo == 'S' and cantidad > 10:
    descuento = precio * 0.15
else:
    descuento = (precio * 0.05)

precio_final = precio - descuento

print('\nSalidas')
print('-' * 60, '\n')
print('El Precio Final que se cobro del articulo fue de $', round(precio_final, 2))
print('se le aplico un ', descuento, '% de descuento a la operacion')
