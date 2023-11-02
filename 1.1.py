# division con resto

#Plantear un script (directamente en el shell de Python) que permita informar, para dos valores a y b el resultado de
#la división a/b y el resto de esa divisón.

a = float(input("ingrese un numero: "))
b = float(input(" ingrese un numero: "))

division = a / b
res = a % b

print("el resultado es:", division)
print("el resto es: ",res)
