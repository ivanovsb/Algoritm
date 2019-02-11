# Иванов Сергей
# Практическое задание №8. Задание №1.
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import string, random

#stroka_s = input('ВВеди строку: ')
stroka_s = ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 10)))
print(stroka_s)
N = len(stroka_s)
count_sub = 0
h_array = []
for i in range(N):
    print()
    for j in range(i, N):
        sub_string = stroka_s[i:j + 1]
        h_sub = hash(sub_string)
        if h_sub not in h_array:
            h_array.append(h_sub)
            print(stroka_s[i:j + 1], end=',')
            count_sub += 1
print(f'\nКоличество уникальных подстрок  - {count_sub}')
print(f'Хэши подстрок - {h_array}')
