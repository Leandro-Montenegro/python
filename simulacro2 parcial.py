import random
random.seed(20220512)
n = 25000
mult3 = 0
mult5 = 0
mult0 = 0
may = 0
acum_pares = 0
num_pares = 0

for i in range(n):
    num = random.randint(1, 45000)

    if num % 3 == 0:
        mult3 += 1
    else:
        if num % 5 == 0:
            mult5 += 1
        else:
            mult0 += 1

    cadena_num = str(num)
    primer_digito = cadena_num[0]
    if primer_digito == "1":
        if i == 0 or num > may:
            may = num

    if num % 2 == 0 and num % 11 == 0:
        num_pares += 1
        acum_pares += num

if num_pares > 0:
    promedio = acum_pares // num_pares
else:
    promedio = 0

porc_mult3 = (mult3 * 100) // n
porc_mult5 = (mult5 * 100) // n
porc_mult0 = (mult0 * 100) // n

print(mult3)
print(mult5)
print(mult0)
print(may)
print(promedio)
print(porc_mult3)
print(porc_mult5)
print(porc_mult0)
