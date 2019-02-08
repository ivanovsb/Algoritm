# Иванов Сергей
# Урок №7. Задание №1.
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def buble_sort(array):
    min = array[0]
    length = len(array) - 1
    for i in range(0, length - 1):
        flag = True
        print(f'Проход номер:{i+1}')
        for j in range(0, length - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
            print(array)
        if flag:
            print('Алгоритм закончил работу')
            return array
    return array


min_d = -100
max_d = 99
array = [random.randint(min_d, max_d) for _ in range(10)]
#array = [-31, -90, 73, -89, 82, -85, -74, -57, 80, 8]
print(array)
print(buble_sort(array))
