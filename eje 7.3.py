#7. Cálculo presupuestario
#En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital se
#reparte de la siguiente manera:

#Área          Presupuesto

#Urgencias        37%

#Pediatría        42%

#Traumatología    21%



#Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.


presupuesto_total = float(input("ingrese el presupuesto total: "))

urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

print("el monto en urgencias es de: ", urgencias)
print("el monto en pediatria es de: ", pediatria)
print("el monto en traumatologia es de: ", traumatologia)
