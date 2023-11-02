car_ant = ""
cl = ctp = r1 = 0
com_h = False
palabras_oh = 0
tiene_oh = False

texto = input("ingrese texto")
for car in texto:
    if car == " " or car == ".":
        if cl > 0:
            ctp += 1
        if com_h and car_ant == "a":
            r1 += 1

        if tiene_oh:
            palabras_oh += 1
        # reiniciar variables
        cl = 0
        com_h = tiene_oh = False
    else:
        cl += 1
        # empieza con h
        if cl == 1 and car == "h":
            com_h = True
        # tiene oh
        if car_ant == 'o' and car == 'h':
            tiene_oh = True

    car_ant = car

print(r1)
print(palabras_oh)



"""Consigna 4: Desarrollar un programa en Python que permita cargar
por teclado un texto y determine la cantidad de expresiones “ta” que se
presente en todo el texto. Siempre se supone que el usuario cargará un
punto para finalizar el texto y que cada palabra de ese texto esta
separado por un espacio en blanco."""
# car_ant = None
# pal_ta = 0
# cadena = input('Ingrese una cadena:')
# for car in cadena:
#  if car != ' ' and car != '.':
#  if car_ant == 't' and car == 'a':
#  pal_ta = pal_ta + 1
#  car_ant = car
# print('La cantidad de expresiones ta es:', ta)
