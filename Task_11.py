# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
number_n = input('Enter number n: ')

while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = int(number_n)
list = []
sum = 0
for i in range(0, number_n):
    n = int(input())
    list.append(n)
    if i % 2 != 0:
        sum = sum + list[i]

print(list)
print(sum)