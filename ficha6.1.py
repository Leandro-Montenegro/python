"""1. Complejo de cines
Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad
 de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:

a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con
 descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones."""

print('COMPLEJO DE CINES')
print('*' * 80)

# Inicializar contadores y acumuladores
monto = 0
funciones = 0
funciones_dto = 0

# Primera carga de datos de corte antes del ciclo
espectadores = int(input('Espectadores (con 0 termina): '))

# Proceso repetitivo
while espectadores != 0:
    # Carga de datos que no determinan el corte del ciclo
    descuento = input('Descuento (S/N): ')
    # Definir precio
    if descuento == 'S':
        precio = 50
    else:
        precio = 75
    # Acumular monto recaudado por función
    monto = monto + (espectadores * precio)
    # Contar funciones con descuento y total de funciones
    if descuento == 'S':
        funciones_dto += 1
    funciones += 1
    # Nueva carga de datos de corte dentro del ciclo
    espectadores = int(input('Espectadores (con 0 termina): '))

# Resultados
print('*'*80)
print('Recaudación total $',monto)
if funciones != 0:
    porc = funciones_dto * 100 / funciones
else:
    porc = 0
print('Porcentaje de funciones con descuento:', porc, '%')
