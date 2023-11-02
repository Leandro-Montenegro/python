"""2. Suma - División - Potencia
Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir
 por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo."""


a = int(input("ingrese un num: "))
b = int(input("ingrese un num: "))
c = int(input("ingrese un num: "))

r = a + b + c

print("el resultado es: ", r)

if r > 10:
    r = r // 2
    print("el resultado es: ", r)
else:
    r = r ** 3
    print("el resultado es: ", r)

