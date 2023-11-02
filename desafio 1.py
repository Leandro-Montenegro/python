#1
segundos = int(input("ingrese cant de segundos: "))
segundos_a_horas = segundos // 3600
segundos_a_minutos = (segundos % 3600) // 60
segs = segundos % 60

if segundos_a_horas <= 24:
    print(segundos_a_horas, ":", segundos_a_minutos, ":", segs)
else:
    print("Excedido")

#2)
hora = int(input("horas = "))
min = int(input("minutos = "))
seg = int(input("segundos = "))

hora_a_seg = hora * 3600
min_a_seg = min * 60

print(hora_a_seg + min_a_seg + seg)
