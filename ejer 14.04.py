"""14. Tarifas de Peaje
La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y, por tal motivo, el día de hoy ofrece
 premios a a sus clientes.

Estos premios se calculan de la siguiente manera:

1) Cada vez que pasa un cliente, se sortea un número del 0 al 9. Si el número coincide con el último dígito de la
 patente del vehículo, se le cobra la tarifa promocional de $50, si no, se le cobra la tarifa estándar de $90

2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7, entonces recibe un descuento
 del 50%, en caso contrario un descuento del 10%.

Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente (únicamente los dígitos),
 simule su paso por el peaje e indique el monto a abonar."""

import random

# Programa de cálculo de peajes
print('Bienvenido a Pase-Pase')
print('=' * 20)

# Ingreso de datos
digitos_patente = int(input('Ingrese dígitos:'))

# Sorteo del dígito
sorteo = random.randint(0, 9)
print('Sorteo: ', sorteo)

# Extracción del último dígito de la patente
ultimo_digito = digitos_patente % 10

# Cálculo de la tarifa
if sorteo == ultimo_digito:
    print('Tarifa Promocional')
    # Si coincide el último dígito con lo sorteado
    # Es precio promocional
    tarifa = 50
else:
    print('Tarifa Completa')
    # Si no coincide, es precio completo
    tarifa = 90

# Cálculo del descuento
if ultimo_digito == 7:
    print('Descuento del 50%')
    # Si la patente termina en 7, el
    # descuento es de 50%
    descuento = tarifa * 0.5
else:
    print('Descuento del 10%')
    # Si la patente NO termina en 7, el
    # descuento es del 10%
    descuento = tarifa * 0.1

# Monto final a pagar
monto = tarifa - descuento

# Resultados
print('=== RESULTADOS ===')
print('Debe abonar: $', monto)
