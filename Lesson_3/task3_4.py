# Иванов Сергей
# Домашнее задание №3. Задание №4.
# Определить, какое число в массиве встречается чаще всего.

import random

maxsize = 10
minsize = 1
array = [random.randint(minsize, maxsize) for _ in range(20)]
# Тестовый массив
#array = [2, 1, 2, 5, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 5, 5]
print(f'Исходный массив: {array}')
lenarray = len(array)
pos = 0
count = 0
maxcount = 0
i = 0
while i <= lenarray:
    for j in range(i, lenarray):
        if array[i] == array[j]:
            count += 1
    if maxcount < count:
        maxcount = count
        pos = i
    count = 0
    i += 1
print(f'Число: {array[pos]:>5}  встречается в массиве максимальное количество раз, равное:  {maxcount}')
print(f'На позиции: {pos:>3}, отсчет с 0')
