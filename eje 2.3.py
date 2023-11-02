#2. Fecha como cadena
#Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato
# 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016'
# el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

#datos
fecha = input("ingrese fecha:")
#procesos
dia = fecha[0] + fecha[1]
mes = int(fecha[3] + fecha[4])
meses = ("enero" , "febrero", "marzo", "abril", "mayo", "junio", "agosto", "septiembre",
         "octubre", "noviembre","diciembre")
nombre_mes = meses[mes - 1]
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]
#salida
print("la fecha es el ", dia, "de", nombre_mes, "del", anio)
