"""12. Cartas de Truco
Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:

   1) Informar si entre las cartas se encuentra el as de espadas

   2) Verificar si las tres cartas son del mismo palo. Si es así, identificar cuál fue la mayor carta.
   En caso contrario, informarlo."""

import random

palos = ('Oro', 'Basto', 'Espada', 'Copa')
numeros = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

print('CARTAS DE TRUCO')
carta1 = random.choice(numeros), random.choice(palos)
carta2 = random.choice(numeros), random.choice(palos)
carta3 = random.choice(numeros), random.choice(palos)

print(carta1, carta2, carta3)

if (carta1[0] == 1 and carta1[1] == 'Espada') \
        or (carta2[0] == 1 and carta2[1] == 'Espada') \
        or (carta3[0] == 1 and carta3[1] == 'Espada'):
    print('Tiene el as de espadas')
else:
    print('NO Tiene el as de espadas')

if carta1[1] == carta2[1] and carta1[1] == carta3[1]:
    may = max(carta1[0], carta2[0], carta3[0])
    print('La carta mayor es ', may, 'de', carta1[1])
else:
    print('No hay tres cartas del mismo palo')
