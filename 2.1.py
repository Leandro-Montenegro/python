#Cuadrado de un binomio

#Un binomio al  cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo
#más el cuadrado del segundo.
#Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b, el valor
# del cuadrado del binomio.

a = float(input("ingrese un numero: "))
b = float(input(" ingrese un numero: "))

bin2 = (a**2) + (2*(a*b)) + (b**2)

print(bin2)
