# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from unicodedata import digit
number = input('Enter a fractional number: ')
sum = 0
for i in number:
    if i.isdigit():
        sum = sum + int(i)
        print(sum)
else:
    print('Please enter a valid value')
    