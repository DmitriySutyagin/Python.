# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


number_n = input('Enter number n: ')

while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = int(number_n)
list = []

list2 = []
for i in range(0, number_n):
    n = int(input())
    list.append(n)
print(list)
if number_n // 2 != 0:
    for i in range(0, len(list) // 2 + 1):
        mul = list[i] * list[number_n - 1 - i]
        list2.append(mul)
else:
    for i in range(0, len(list) // 2):
        mul = list[i] * list[number_n - 1 - i]
        list2.append(mul)
    
print(list2)

