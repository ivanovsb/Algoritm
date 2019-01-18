# Иванов Сергей.
# Домашнее задание №4. Задание №1.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# !!!! Выводит последнее натуральное число с наибольшей суммой цифр !!!!

import random

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
    length = len(massiv)
    for el in massiv:
        massiv_sum.append(sum_digit(el))
    #    print(f'Массив сумм цифр чисел {massiv_sum}')
    max_sum = max(massiv_sum)
    max_chislo = massiv[massiv_sum.index(max_sum)]
    return max_chislo, max_sum


def find3_max_s(massiv):
    dict_sum = {}
    for i, el in enumerate(massiv):
        dict_sum[sum_digit(el)] = i
    #    print(f'Словарь сумм цифр чисел и позиций в исходном массиве {dict_sum}')
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
    MAX_D = 1000000
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
