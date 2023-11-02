#8. Rinde de un Campo Agricola
#Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. Se pide ingresar el largo
#y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.


#Entradas
largo = int(input("ingrese el largo de la parcela: "))
ancho = int(input("ingrese el ancho de la parcela: "))

#procesos
quintal = 10 // 2
superficie = largo * ancho
rinde = superficie // quintal

#salidas

print('El rinde que obtiene el productor en', superficie, 'm2')
print('es de', rinde, 'quintales')

