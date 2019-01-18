# Иванов Сергей.
# Домашнее задание №4. Задание №1.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# !!!! Выводит последнее натуральное число с наибольшей суммой цифр !!!!

import random, cProfile

NUMBER_DIGITAL = 20000


def test_find1():
    return find1_max_s(massiv)


def test_find2():
    return find2_max_s(massiv)


def test_find3():
    return find3_max_s(massiv)


def find1_max_s(massiv):
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
    return max_chislo, max_sum


def find2_max_s(massiv):
    massiv_sum = []
    for el in massiv:
        massiv_sum.append(sum_digit(el))
    max_sum = max(massiv_sum)
    max_chislo = massiv[massiv_sum.index(max_sum)]
    return max_chislo, max_sum


def find3_max_s(massiv):
    dict_sum = {}
    for i, el in enumerate(massiv):
        dict_sum[sum_digit(el)] = i
    lst_sum = list(dict_sum.keys())
    max_sum = max(lst_sum)
    max_chislo = massiv[dict_sum[max_sum]]
    return max_chislo, max_sum


def sum_digit(chislo):
    sum_d = 0
    for j in str(chislo):
        sum_d += int(j)
    return sum_d


def generate_spisok(n):
# Максимальная разрядность
    MAX_D = 1000
    massiv = [random.randint(1, MAX_D) for _ in range(n)]
    return massiv


massiv = generate_spisok(NUMBER_DIGITAL)
#print(f'Исходный массив чисел {massiv}')
max_digit, max_sum = test_find1()
print(f'Наибольшее число по сумме элементов. Алгоритм 1. {max_digit}')
print(f'Сумма элементов {max_sum}\n')
max_digit, max_sum = test_find2()
print(f'Наибольшее число по сумме элементов. Алгоритм 2. {max_digit}')
print(f'Сумма элементов {max_sum}\n')
max_digit, max_sum = test_find3()
print(f'Наибольшее число по сумме элементов. Алгоритм 3. {max_digit}')
print(f'Сумма элементов {max_sum}')

cProfile.run('test_find1()')
# Вывод:
#
# Python_Algoritm\Task4>python -m timeit -n 100 -s "import task4_3" "task4_3.test_find1()"
# Python_Algoritm\Task4>python -m timeit -n 100 -s "import task4_3" "task4_3.test_find2()"
# Python_Algoritm\Task4>python -m timeit -n 100 -s "import task4_3" "task4_3.test_find3()"
#
# MAX_D = 1000
# NUMBER_DIGITAL = 20
# Алгоритм 1 100 loops, best of 3: 43.8 usec per loop
# Алгоритм 2 100 loops, best of 3: 180 usec per loop
# Алгоритм 3 100 loops, best of 3: 159 usec per loop
#
# NUMBER_DIGITAL = 200
# 100 loops, best of 3: 432 usec per loop
# 100 loops, best of 3: 1.62 msec per loop
# 100 loops, best of 3: 1.45 msec per loop
#
# NUMBER_DIGITAL = 20000
# 100 loops, best of 3: 50.3 msec per loop
# 100 loops, best of 3: 188 msec per loop
# 100 loops, best of 3: 175 msec per loop
#
# Сложность алгоритма линейная: O(n)
# увеличение количества чисел в 10 раз увеличивает время выполнения алгоритма в 10 раз
# увеличение количества чисел в 1000 раз увеличивает время выполнения алгоритма в 1000 раз

# Алгоритм 1
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.026    0.026 <string>:1(<module>)
#         1    0.000    0.000    0.026    0.026 task4_3.py:12(test_find1)
#         1    0.026    0.026    0.026    0.026 task4_3.py:24(find1_max_s)
#         1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Алгоритм 2
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.079    0.079 <string>:1(<module>)
#         1    0.000    0.000    0.079    0.079 task4_3.py:16(test_find2)
#         1    0.015    0.015    0.079    0.079 task4_3.py:40(find2_max_s)
#     20000    0.060    0.000    0.060    0.000 task4_3.py:59(sum_digit)
#         1    0.000    0.000    0.079    0.079 {built-in method builtins.exec}
#         1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
#     20000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
# Алгоритм 3
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.074    0.074 <string>:1(<module>)
#         1    0.000    0.000    0.074    0.074 task4_3.py:20(test_find3)
#         1    0.013    0.013    0.074    0.074 task4_3.py:49(find3_max_s)
#     20000    0.061    0.000    0.061    0.000 task4_3.py:59(sum_digit)
#         1    0.000    0.000    0.074    0.074 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
#
# Алгоритмы одинаковые по сложности, но разные по быстродействию, решение задачи не совсем получилось.
# Скорость работы первого алгоритма выше. Второй  и третий алгоритмя одинаковые,
# но Во втором используется функция append.
# в третьем алгоритме используется поиск по множеству на основе хэша.
