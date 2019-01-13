import random

MAX_SIZE = 10
MAX_D = 100
massiv = [random.randint(1, MAX_D) for _ in range(MAX_SIZE)]
print(f'Исходный массив чисел {massiv}')
max_sum = 0
max_chislo = 0
for chislo in massiv:
    temp_sum = 0
    current = chislo
    while chislo > 0:
        dig1 = chislo % 10
        temp_sum += dig1
        chislo //= 10
    if max_sum < temp_sum:
        max_sum = temp_sum
        max_chislo = current
print(f'Число {max_chislo} является наибольшим числом по сумме цифр. \nСумма цифр равна {max_sum}')
