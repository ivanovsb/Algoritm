# Домашнее задание 1 Задача 1
# Иванов Сергей


dig = int(input('Введите трехзначное целое число: '))
digit3 = dig % 10
dig = dig // 10
digit2 = dig % 10
digit1 = dig // 10
sum = digit1 + digit2 + digit3
mult = digit1 * digit2 * digit3
print('Сумма чисел', sum)
print('Произведение чисел', mult)
