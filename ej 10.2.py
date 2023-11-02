#10. Calculo de Ganancias de Pelicula
#Una empresa dedicada al pago de ganancias por las películas que se realizan en los estudios, necesita un sistema que
#permita cargar el total que la película recaudó, el nombre del participante de la película que se tiene que abonar,
#el porcentaje que se le debe pagar. Con esos datos mostrar el nombre del actor y el monto que recibirá de las ganancias


#entradas
print("bienvenido/a")
actor = input("ingrese el nombre del participante de la pelicula:")
recaudacion = int(input("ingrese el dinero recudado: "))
porcentaje = float(input("ingrese el porcentaje que se le debe pagar:"))

#procesos
ganancia_actor = recaudacion * porcentaje / 100

#salidas
print(actor,"recibira de ganancia: ", ganancia_actor, "dolares")
