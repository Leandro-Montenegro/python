#5. Control electoral
#Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato:
#apellido, nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
#cantidad de votos entre paréntesis, y debajo una línea con tantas  "x" como votos obtenidos
#(por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x")
#(Asumimos que en el centro vecinal no hay demasiados electores, de forma que podamos estar seguros que no habrá miles o
#millones de votos... sólo unos pocos para darle sentido al enunciado).

nombre = input("ingrese el nombre del candidato: ")
apellido = input("ingrese el apellido del candidato: ")
cant_votos = int(input("ingrese la cantidad de votos: "))
iniciales = nombre[0] + apellido [0]
cantidad_x = "x" * cant_votos
print("las iniciales de los candidatos son: ", iniciales)
print("(", cant_votos, "votos )")
print(cantidad_x)
