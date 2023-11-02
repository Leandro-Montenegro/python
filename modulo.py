from tp4 import *


def principal():
    op = -1
    usuario = input("Ingrese su nombre porfavor: ")
    print("Bienvenido/a", usuario)
    generar_archivo()
    while op != 0:
        op = menu()
        if op == 1:
            generar_archivo()
            print("Archivo binario creado con exito.")
        elif op == 2:
            algo = cargar_ticket()
            agregar_ticket(algo)
        elif op == 3:
            mostrar_archivo()
        elif op == 4:
            pass
        elif op == 5:
            pass


if __name__ == "__main__":
    principal()

"""def es_num(car):
    num = "1234567890"
    return car in num


def cargar_ticket():
    codigo = 0
    while codigo <= 0:
        codigo = int(input("ingrese un codigo:"))
        if codigo <= 0:
            print("el codigo debe ser mayor a 0")

    patente = input("ingrese patente: ")
    while len(patente) < 0:
        print("error")
        patente = input("ingrese patente: ")
        if len(patente) < 6 or len(patente) > 7:
            print("la patente es de otro pais.")

    tip = input('ingrese el tipo de vehiculo (1 digito entre el 0 y el 2): ', )
    while tip != '0' and tip != '1' and tip != '2':
        tip = input('ingrese el tipo de vehiculo adecuado (1 digito entre el 0 y el 2): ', )
        tip = int(tip)

    fdp = input('ingrese la forma de pago (un digito, 1 o 2): ', )
    while fdp != 1 and fdp != 2:
        fdp = input('ingrese la forma de pago adecuada (un digito, 1 o 2): ', )
        
    pais = input('ingrese el pais (un digito entre 0 y 4): ', )
    while pais != '0' and pais != '1' and pais != '2' and pais != '3' and pais != '4':
        pais = input('ingrese el pais adecuadamente (un digito entre 0 y 4): ', )

    dist = str(input('ingrese los kilometros: ', ))
    while not es_num(dist):
        dist = input('ingrese los kilometros adecuadamente (maximo 3 digitos): ', )"""


