# Иванов Сергей
# Домашнее задание №3. Задание №7.
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

maxsize = 10
minsize = 1
array = [random.randint(minsize, maxsize) for _ in range(10)]
print(f'Исходный массив: {array}')
mindigital1 = array[0]
mindigital2 = array[0]
posmin1 = 0
posmin2 = 0
for i, item in enumerate(array):
    if item <= mindigital1:
        mindigital2 = mindigital1
        posmin2 = posmin1
        mindigital1 = item
        posmin1 = i
    elif item < mindigital2:
        mindigital2 = item
        posmin2 = i
print(f'Первое минимальное число: {mindigital1:>5}  позиция в массиве {posmin1}')
print(f'Второе минимальное число: {mindigital2:>5}  позиция в массиве {posmin2}')
