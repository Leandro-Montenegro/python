import random
random.seed(19)
n = 35000
cont_men40000 = 0
cont_men2500 = 0
cont_div7 = 0
cont_pares = 0
may = 0
cont_ultdig7 = 0
acum_ultdig7 = 0
num_1k_10k = 0
menor_num = 0
positivos = 0

for i in range(n):
    num = random.randint(-15000, 45000)
    if (num >= 0) and (num <= 40000):
        cont_men40000 += 1
    if (num <= 2500) and (num >= -10000):
        cont_men2500 += 1
    if num > 0 and num % 7 == 0:
        cont_div7 += 1

    if (num % 2 == 0) and (num >= 10000) and (num <= 45000):
        cont_pares += 1
        x = str(num)
        tercer_digito = x[2]
        if tercer_digito == "4" or tercer_digito == "9":
            if i == 0 or num > may:
                may = num

    ultimo_digito = abs(num) % 10
    if (num > -5000) and (num <= 25000) and ultimo_digito == 7:
        cont_ultdig7 += 1
        acum_ultdig7 += num

    if (num >= 1000) and (num <= 10000):
        num_1k_10k += 1
    if i == 0 or num < menor_num:
        menor_num = num

    if num > 0:
        positivos += 1

if num_1k_10k > 0:
    promedio = acum_ultdig7 // cont_ultdig7
else:
    promedio = 0

porcentaje = (num_1k_10k * 100) // positivos

print(cont_men40000)
print(cont_men2500)
print(cont_div7)
print(may)
print(promedio)
print(porcentaje)
print(menor_num)
