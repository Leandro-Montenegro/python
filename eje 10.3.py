#10. Tiempos de Triatlon
#Un triatlón es una competición deportiva en que los participantes realizan tres carreras: una de natación, una ciclista
# y una pedestre.
#Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) logrados en cada etapa por uno de los
# deportistas participantes.
#Con esos datos determinar:
#Tiempo total de la prueba (en formato hh:mm:ss)
#Tiempo máximo y mínimo (en segundos)
#Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
#Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones


#-------------------entradas---------------------------------------------------
natacion = (
    int(input("ingrese el tiempo (minutos) de natacion: ")),
    int(input("ingrese el tiempo (segundos) de natacion: "))
)
ciclista = (
    int(input("ingrese el tiempo (mins) de ciclista: ")),
    int(input("ingrese el tiempo (segs) de ciclista: "))
)
pedestre = (
    int(input("ingrese el tiempo (mins) de pedestre: ")),
    int(input("ingrese el tiempo (segs) de pedestre: ")),
)
#-------------------procesos---------------------------------------------------
#en formato hh:mm:ss
minutos_asegundos = natacion[0] * 60
segundos = natacion[1]
suma_de_segundos01 = minutos_asegundos + segundos

minutos_asegundos = ciclista[0] * 60
segundos = ciclista[1]
suma_de_segundos02 = minutos_asegundos + segundos

minutos_asegundos = pedestre[0] * 60
segundos = pedestre[1]
suma_de_segundos03 = minutos_asegundos + segundos

suma_de_segundos_total = suma_de_segundos01 + suma_de_segundos02 + suma_de_segundos03

horas = suma_de_segundos_total // 3600
parte_restante = suma_de_segundos_total % 60 ** 2
minutos = parte_restante // 60
segundos = parte_restante % 60

menor = min(suma_de_segundos01, suma_de_segundos02, suma_de_segundos03)
mayor = max(suma_de_segundos01, suma_de_segundos02, suma_de_segundos03)

promedio = round(suma_de_segundos_total / 3, 2) #por 3 debido a que hay sumas seg 1,2 y 3 #el 2 despues de , indica cuantos decimales quiero

#-------------------------salidas----------------------------------------------
print("el tiempo total de la prueba es de: ", horas, ":", minutos, ":", segundos)
print("el tiempo maximo es de: ", mayor)
print("el tiempo minimo es de: ", menor)
print("el tiempo promedio es de: ", promedio)
