"""10. Terreno
Se ingresan las medidas de frente y fondo de un terreno.

Determinar si es cuadrado o rectangular y calcular su superficie."""


frente = float(input("ingrese medida: "))
fondo = float(input("ingrese medida: "))

if frente == fondo:
    print("es un cuadrado")
else:
    print("es un rectangulo")

superficie = frente * fondo
print(superficie)
