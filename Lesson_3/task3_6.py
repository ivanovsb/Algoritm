# Иванов Сергей
# Домашнее задание №3. Задание №6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

maxsize = 10
minsize = 1
array = [random.randint(minsize, maxsize) for _ in range(10)]
print(f'Исходный массив: {array}')
maxdigital = array[0]
mindigital = array[0]
posmax = 0
posmin = 0
sumelem = 0
for i, item in enumerate(array):
    if item >= maxdigital:
        maxdigital = item
        posmax = i
    elif item < mindigital:
        mindigital = item
        posmin = i

print(f'Максимальное число: {maxdigital:>5}  позиция в массиве {posmax}')
print(f'Минимальное число:  {mindigital:>5}  позиция в массиве {posmin}')
if posmin > posmax:
    posmin, posmax = posmax, posmin
for i in range(posmin + 1, posmax):
    sumelem += array[i]
print(f'Искомая сумма элементов: {sumelem}')
