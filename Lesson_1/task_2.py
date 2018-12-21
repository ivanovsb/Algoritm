n1 = int(input("Введите первое двоичное число: "))
n2 = int(input("Введите второе двоичное число: "))

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2
digit5_left = n1 << 1
digit5_right = n1 >> 1
digit6_left = n2 << 1
digit6_right = n2 >> 1

print(f"Первое число в двочном виде: {bin(n1)}")
print(f"Второе число в двочном виде: {bin(n2)}")
print(f"Результат побитового  OR: {bin(bit_or)}")
print(f"Результат побитового AND: {bin(bit_and)}")
print(f"Результат побитового XOR: {bin(bit_xor)}")

print(
    f"Результат побитового сдвига числа {n1} на 1 бит влево в двоичном виде: {bin(digit5_left)}, в обычном виде: {digit5_left}")
print(
    f"Результат побитового сдвига числа {n1} на 1 бит вправо в двоичном виде: {bin(digit5_right)}, в обычном виде: {digit5_right}")
print(
    f"Результат побитового сдвига числа {n2} на 1 бит влево в двоичном виде: {bin(digit6_left)}, в обычном виде: {digit6_left}")
print(
    f"Результат побитового сдвига числа {n2} на 1 бит вправо в двоичном виде: {bin(digit6_right)}, в обычном виде: {digit6_right}")
