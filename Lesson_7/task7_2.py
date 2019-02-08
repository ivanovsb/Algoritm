# Иванов Сергей
# Урок №7. Задание №2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge(array_1, array_2, array_m):
    i = 0
    j = 0
    k = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            array_m[k] = array_1[i]
            i += 1
        else:
            array_m[k] = array_2[j]
            j += 1
        k += 1
    while i < len(array_1):
        array_m[k] = array_1[i]
        i += 1
        k += 1
    while j < len(array_2):
        array_m[k] = array_2[j]
        j += 1
        k += 1
    return array_m


def merge_sort(array_s):
    if len(array_s) < 2:
        return array_s
    pos = len(array_s) // 2
    l_array = merge_sort(array_s[:pos])
    r_array = merge_sort(array_s[pos:])
    return merge(l_array, r_array, array_s)


array = [random.uniform(0, 49) for _ in range(10)]
# array = [7, 37, 41, 6, 6, 9, 40, 49, 12, 8]
print(array)
print(merge_sort(array))
