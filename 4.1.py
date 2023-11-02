#ult digito
#¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría
# los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito
# del mismo (por un lado) y los dos últimos dígitos (por otro lado) [Ayuda: ¿cuáles son los posibles restos que se
# obtienen de dividir un número cualquiera por 10?]


ult = 0
dos_ult = 0
a = int(input("ingrese un numero entero: "))
ult = a % 10   #para calcular el ult dig se usa el % 10
dos_ult = a % 100   # para calcular los 2 ult dig se usa % 100
print(ult)
print(dos_ult)
