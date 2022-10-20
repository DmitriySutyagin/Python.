# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
number_n = input('Enter number n: ')

while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = int(number_n)
def fibonachi(number_n):
    if number_n in [1, 2]:
        return 1
    else:
        return fibonachi(number_n - 1) + fibonachi(number_n - 2)
list = []
for i in range(1, number_n):
        list.append(fibonachi(i))
def fibonachi(number_n):
    if number_n in [1, 2]:
        return - 1
    else:
        return fibonachi(number_n - 1) + fibonachi(number_n -2)
list2 = []
for i in range(1, number_n):
    list2.append(fibonachi(i))
list2.reverse()
print(list2 + list)
