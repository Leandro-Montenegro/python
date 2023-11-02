#4. Polinomio de segundo grado
#Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado, y calcule y
#muestre el valor del polinomio en el punto x (cargando también x por teclado). Además, para el mismo polinomio, calcule
#y muestre el valor del discriminante de la fórmula para el cálculo de las raíces de la ecuación.

#entradas
a = int(input("ingrese el coeficiente: "))
b = int(input("ingrese el coeficiente: "))
c = int(input("ingrese el coeficiente: "))
x = int(input("ingrese el valor en el punto x: "))

#procesos
y = a * (x ** 2) + b * x + c
discriminante = b ** 2 - 4 * a * c

# Presentacion de resultados
print('El valor del polinomio en el valor x=', x, 'es:', y)
print('El discriminante del polinomio es:', discriminante)
