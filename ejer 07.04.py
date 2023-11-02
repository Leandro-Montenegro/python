"""7. Tirada de moneda
Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara
 o cruz y luego informar si acertó o no con su apuesta."""

import random

print('Tirada de la moneda')
print('=' * 80)

caras = 'cara', 'cruz'

apuesta = int(input('Seleccion que cara desea apostar (0 Cara 1 Cruz): '))
jugada = random.choice(caras)

if jugada == caras[apuesta]:
    print('El jugador ha ganado el juego, acerto, salio', jugada)
else:
    print('El jugador ha perdido el juego salio', jugada, 'y el jugador aposto a', caras[apuesta])

