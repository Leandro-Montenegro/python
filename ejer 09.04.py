"""9. Edad mínima
Ingresar por teclado las edades de 3 participantes de un concurso.

Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado."""


participante1 = int(input("ingrese edad: "))
participante2 = int(input("ingrese edad: "))
participante3 = int(input("ingrese edad: "))

edad_minima = int(input("ingrese edad minima: "))

if participante1 >= edad_minima and participante2 >= edad_minima and participante3 >= edad_minima:
    print("cumplen con la ecad minima para el concurso")
else:
    print("no cumplen con la edad minima requerida para el concurso")
