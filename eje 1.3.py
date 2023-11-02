#1. Plazo fijo
#Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco
#y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3% y que el
#banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.

#entrada
dinero_depositado = float(input("ingrese cantidad de dinero depositada en plazo fijo: "))
interes = dinero_depositado * 0.023
servicios_financieros = 20
#proceso
saldo = (dinero_depositado + interes) - servicios_financieros
#salidas
print("el saldo que tendra esa cuenta al vencer el plazo fijo es de: ", saldo, "dolares")
