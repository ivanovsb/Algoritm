# Иванов Сергей.
# Домашнее задание №2. Задание №3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

chislo1 = int(input("Введи число: "))
chislo2 = ''
chet = 0
nechet = 0
while chislo1 > 0:
    dig1 = chislo1 % 10
    chislo2 += str(dig1)
    chislo1 //= 10
print(f"Обратное по порядку число - {int(chislo2)}")
