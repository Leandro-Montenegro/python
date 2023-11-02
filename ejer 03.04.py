"""3. Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un
 determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
  (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.

La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora."""

print('Jornal de Operario')
print('=' * 80 , '\n')

#Datos
turno = int(input('Ingrese el turnos del operario (1 - Diurno, 2 - Nocturno): '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))

#Proceso
if turno == 1:
    total = horas * 35.5
else:
    total = horas * 40.60

#Resultados
print('La empresa le debe pagar al operario un jornal de $', total)
