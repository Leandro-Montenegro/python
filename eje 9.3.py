#9. Costos del Proyecto
#Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene un presupuesto de
#x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% por el proyecto,
#determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.

#entrada
presupuesto = float(input("ingrese el presupuesto: "))
#proceso
ganancia = presupuesto * 0.17
valor_max = presupuesto - ganancia
#salida
print("el valor máximo que pueden alcanzar los costos del proyecto es de: ", valor_max)
