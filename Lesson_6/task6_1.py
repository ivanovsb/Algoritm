# Иванов Сергей.
# Домашнее задание №6 на основе Домашнего задания №3. Задание №1.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
# ОС Windows 8.1 x32 Значение 338.
import sys


def count_size(x):
    size_el = sys.getsizeof(x)
    print(sys.getsizeof(x), type(x))
    if hasattr(x, '__iter__'):
        for item in x:
            size_el += sys.getsizeof(item)
            print(sys.getsizeof(x), type(x))
    return size_el


digit = [i for i in range(2, 10)]
for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    print(f'{i} кратно количество {count}')

local_var = dict(locals())
#print(f'Local: {local_var}')
mem_sum = 0
for key in local_var:
    if key[:1] != '_':
        print(f'Переменная: {local_var[key]}')
        mem_sum += count_size(local_var[key])
print(f'Занимаемая память {mem_sum}')
