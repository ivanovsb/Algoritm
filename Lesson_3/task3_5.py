# Иванов Сергей
# Домашнее задание №3. Задание №5.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

maxsize = 10
minsize = -10
array = [round(random.uniform(minsize, maxsize), 2) for _ in range(20)]
print(f'Исходный массив: {array}')
element = array[0]
poselement = 0
for i, item in enumerate(array):
    if item < 0:
        if element < item or element >= 0:
            element = item
            poselement = i
print(f'Максимальное отрицательное число: {element:>5}  позиция в массиве {poselement}')
