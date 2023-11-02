import random
random.seed(49)
n = 20000
elem_control = 0
mult5 = 0
mult7 = 0
mult9 = 0
may = 0
ult_digit = 0
num_pares = 0


for i in range(n):
    num = random.randint(1, 45000)
    elem_control += num

    if num % 5 == 0:
        mult5 += 1
    if num % 7 == 0:
        mult7 += 1
    if num % 9 == 0:
        mult9 += 1

    if (num % 10 >= 5) and (num % 10 <= 8) :
        ult_digit += 1
        if i == 0 or num > may:
                may = num

    if num % 2 == 0 and num < 15000:
        num_pares += 1

porc = (num_pares * 100) // n

print(elem_control)
print(mult5)
print(mult7)
print(mult9)
print(may)
print(num_pares)
print(porc)
