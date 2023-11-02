"""1. Generador de Dirección de Mail
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de
mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:

Componer la dirección de correo de la siguiente manera:
<primera letra del nombre><apellido>@<dominio>
Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería:
fsteffolani@frc.utn.edu.ar
Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
<nombre>.<apellido>@<dominio>
Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
soledad.steffolani@colegiorosarito.edu.ar"""

# Generador de dirección de Mail
# Entradra:
# Nombre
# Apellido
# Dominio
# Salida:
# Dirección de mail propuesta

print('#' * 30)
print('# ' + 'Generador de Mails' + \
  (' ' * (30-(len('Generador de Mails')+5))) + '#')
print('#' * 30)

print('\nIngreso de datos:')
nombre = input('\tNombre : ')
apellido = input('\tApellido: ')
dominio = input('\tDominio : ')

#transformar las cadenas ingresadas en minúscula
# independientemente de cómo se ingresaron.
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()
primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_apellido != primera_letra_nombre:
    mail_propuesto = primera_letra_nombre + apellido + '@' + \
     dominio
else:
    mail_propuesto = nombre + '.' + apellido + '@' + dominio

print()
print('Mail propuesto:\n\t', mail_propuesto)
print('#' * 30)

input('\nPresione enter para finalizar...')

