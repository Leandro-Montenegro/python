"""2. Elecciones Presidenciales
Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas:

Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue en número de votos.

Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.

Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera, resultando electa la que
 obtenga mayor número de votos afirmativos válidamente emitidos.

Desarrollar un programa que permita ingresar, para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de
 votos obtenidos.

Luego determinar:

Qué fórmula obtuvo el mayor porcentaje.
Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes participan de la segunda vuelta."""

print('Elecciones Presidenciales')
print('*' * 80)

# Datos
formula1 = input ("Ingrese fórmula lista 1: ")
votos1 = int(input("Ingrese votos lista 1: "))
formula2 = input ("Ingrese fórmula lista 2: ")
votos2 = int(input("Ingrese votos lista 2: "))
formula3 = input ("Ingrese fórmula lista 3: ")
votos3 = int(input("Ingrese votos lista 3: "))

# Procesos
#Subproblema 1: Determinar primer y segundo lugar
if votos1 > votos2 and votos1 > votos3:
    primero = formula1, votos1
    if votos2 > votos3:
        segundo = formula2, votos2
    else:
        segundo = formula3, votos3
elif votos2 > votos3:
    primero = formula2, votos2
    if votos1 > votos3:
        segundo = formula1, votos1
    else:
        segundo = formula3, votos3
else:
    primero = formula3, votos3
    if votos1 > votos2:
        segundo = formula1, votos1
    else:
        segundo = formula2, votos2

#Subproblema 2: Definir el resultado de la elección
total = votos1 + votos2 + votos3
porcentaje1 = primero[1] * 100 / total
if porcentaje1 > 45:
    resultado = 'Ganó con más del 45% de los votos ' + primero[0]
else:
    diferencia = porcentaje1 - (segundo[1] * 100 / total)
    if porcentaje1 >= 40 and diferencia >= 10:
        resultado = 'Ganó con 40%: ' + primero[0] + ' por diferencia de más de 10 puntos con ' + segundo[0]
    else:
        resultado = "Segunda vuelta entre: " + primero[0] + " y " + segundo[0]

# Resultados
print('*' * 80)
print(resultado)

print(primero[1])
print(segundo[1])
