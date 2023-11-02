#7. Votación en el Congreso
#En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita ingresar la cantidad
#de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

#entradas

votos_favor = int(input("ingrese cantidad de votos a favor: "))
votos_contra = int(input("ingrese cantidad de votos en contra: "))

#procesos

votos_total = (votos_favor + votos_contra)
porc_favor = (votos_favor * 100) // votos_total
porc_contra = (votos_contra * 100) // votos_total

#resultados

print("la cantidad de votos es de: ", votos_total)
print("los votos a favor de la ley son de un ", porc_favor, "%")
print("los votos en contra de la ley son de un ", porc_contra, "%")
