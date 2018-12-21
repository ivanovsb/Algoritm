# Домашнее задание 1 Задача 4
# Иванов Сергей 2018г.

import random

print("Введите границы диапазона для генерации целого числа")
d1 = int(input("\tпервое число диапазона: "))
d2 = int(input("\tвторое число диапазона: "))
if d1 > d2:
    digit = random.randint(d2, d1)
else:
    digit = random.randint(d1, d2)
print(f"Случайное число в указанном диапазоне: {digit}")

print("Введите границы диапазона для генерации вещественного числа")
d1 = float(input("\tпервое число диапазона: "))
d2 = float(input("\tвторое число диапазона: "))
if d1 > d2:
    digit = random.uniform(d2, d1)
else:
    digit = random.uniform(d1, d2)
print(f"Случайное число в указанном диапазоне: {digit}")

print("\tВведите символы для границы диапазона")
d1 = ord(input("\tначальный символ диапазона: "))
d2 = ord(input("\tвторой символ диапазона: "))
if d1 > d2:
    digit = random.randint(d2, d1)
else:
    digit = random.randint(d1, d2)
print(f"Случайный символ в указанном диапазоне: {chr(digit)}")
