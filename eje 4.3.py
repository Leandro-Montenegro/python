#4. Duración de un vuelo
#Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), determine cuál
#es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado,
#¿a qué hora llegara al mismo?

#entrada de datos
partida = (input("ingrese horario de partida: "))
llegada = (input("ingrese horario de llegada: "))

# procesos
horas_partida = int(partida[0:2]) #indices de horas
horas_llegada = int(llegada[0:2])
minutos_partida = int(partida[3:]) #indices  de minutos
minutos_llegada = int(llegada[3:])

#pasamos a minutos las horas de llegada y salida
horas_partida_amin = horas_partida * 60
horas_llegada_amin = horas_llegada * 60

# sumamos las horas convertidas a minutos + los minutos
partida = horas_partida_amin + minutos_partida
llegada = horas_llegada_amin + minutos_llegada

# duracion: se resta horario de llegada - horario de partida
duracion = llegada - partida

# hora que llegó al hotel:
hotel_horas = (llegada + 45) // 60
hotel_minutos = (llegada + 45) % 60
hotel = str(hotel_horas) + ":" + str(hotel_minutos)
#salidas
print("la duracion es de: ",duracion, "minutos")
print("llega al hotel a las: ",hotel)
