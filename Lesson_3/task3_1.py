# Иванов Сергей.
# Домашнее задание №3. Задание №1.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

naturalarray = [i for i in range(2, 100)]
print(naturalarray)
chislo = [i for i in range(2, 10)]
count = 0
for i in range(2, 10):
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    print(f'{i} кратно количество {count}')
    count = 0
