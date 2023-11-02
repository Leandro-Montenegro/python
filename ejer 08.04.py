"""8. Lanzamiento de dados
Simular un juego en el que se lanzan dos dados.

 Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina."""

import random

print("BIENVENIDO AL LANZAMIENTO DE DADOS")
print("*" * 80)

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print(dado1)
print(dado2)
if dado1 == dado2 or (dado1 + dado2) % 2 == 1:
    print("gana el usuario")
else:
    print("gana la maquina")


