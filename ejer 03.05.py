"""3. Mantenimiento Informático
El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa que facilite la
 gestión de las tareas realizadas en el día.

El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de identificación de la PC,
tiempo de reparación (expresado en minutos) y la causa de mantenimiento (1- Problema de Hardware 2-Problema de Software)

Los requerimientos funcionales son:

a)  ¿Cuál es el tiempo total de las tareas de mantenimiento?

b)  ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?

c)  Tiempo promedio de tareas de mantenimiento.

d)  Informar con un mensaje si todas las PC (Número de identificación) que se les ha realizado mantenimiento tuvieron
problemas de Hardware."""

print('Mantenimiento informatico')
print('='* 80)

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo1 = numero_pc, tiempo_reparacion, causa

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo2 = numero_pc, tiempo_reparacion, causa

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo3 = numero_pc, tiempo_reparacion, causa

# procesos

total_mant = equipo1[1] + equipo2[1] + equipo3[1]
prom_mant = total_mant / 3

if equipo1[1] > equipo2[1] and equipo1[1] >  equipo3[1]:
    mayor = equipo1
else:
    if equipo2[1] > equipo3[1]:
        mayor = equipo2
    else:
        mayor = equipo3

mant_por_hardware = False
if equipo1[2] == 1 and equipo2[2] == 1 and equipo3[2] == 1:
    mant_por_hardware = True

# Salidas
print('El tiempo total de reparacion de las tres PC fue de', total_mant,'minutos')
print('La PC con mayor tiempo de reparacion fue la numero', mayor[0])
print('El tiempo promedio de reparacion fue de', prom_mant, 'minutos')

if mant_por_hardware:
    print('Todas las PC recibiron mantenimiento por problemas de harware')
else:
    print('Las PC recibieron distintos tipos de mantenimiento')
