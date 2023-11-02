#6. Cálculo de sueldo
#Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece.
# Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y un
# descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:

#       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx

#      Área Funcional:  xxxxxxxxxxxx

#       Salario Actual: $ xxxx

print("bienvenido")
salario = float(input("ingrese el salario:"))
nombre = input("ingrese nombre del empleado;")
area_funncional = input("ingrese area funcional a la que pertenece:")

#procesos
incremento = salario * 0.08
descuento = salario * 0.025
nuevo_salario = (salario + incremento) - descuento

#salidas
print(" Nombre Empleado:" ,nombre,"               Nuevo Salario",nuevo_salario, " pesos")
print("Área Funcional",area_funncional)
print(" Salario Actual", salario, "pesos")
