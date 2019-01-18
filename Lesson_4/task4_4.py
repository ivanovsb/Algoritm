# Иванов Сергей
# Решето Эратосфена, вводим до какого числа включительно

n = int(input('введи максимальное число: '))
massiv = [i for i in range(n+1)]
print(f'Массив {massiv}')
massiv[1] = 0
for i in range(2, n+1):
    if massiv[i] != 0:
        j = i + i
        while j <= n:
            massiv[j] = 0
            j += i
print(massiv)
result = [i for i in massiv if i != 0]
print(result)

print('Второй варииант')
massiv = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        massiv.append(i)
print(massiv)
