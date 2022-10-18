# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
number_n = input('Enter a real number n: ')

while number_n.isalpha():
    number_n = input('Enter a real number n: ')
number_n = int(number_n)
list = []
list2 = []
for i in range(0, number_n):
    list.append(round(random.uniform(0, 10), 2))
    
print(list)
for i in range(0, number_n):
    list2.append(round((list[i] % 1), 2))
print(list2)
min(list2)
max(list2)
print(round((max(list2) - min(list2)), 2))
