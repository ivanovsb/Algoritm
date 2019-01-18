# Иванов Сергей
# Домашнее задание №3. Задание №3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

maxsize = 1000
minsize = 1
array = [random.randint(minsize, maxsize) for _ in range(10)]
print(f'Исходный массив: {array}')
maxdigital = array[0]
mindigital = array[0]
posmax = 0
posmin = 0
for i, item in enumerate(array):
    if item >= maxdigital:
        maxdigital = item
        posmax = i
    elif item < mindigital:
        mindigital = item
        posmin = i

print(f'Максимальное число: {maxdigital:>5}  позиция в массиве {posmax}')
print(f'Минимальное число:  {mindigital:>5}  позиция в массиве {posmin}')
array[posmax], array[posmin] = array[posmin], array[posmax]
print(f'Результат массив с помененным макс и мин элементамми: {array}')
