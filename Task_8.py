# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Enter number n: '))
list = []
for i in range(1, n + 1):
    list.append([i, 3 * i + 1])
print(dict(list))