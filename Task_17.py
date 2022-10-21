# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number_n = input('Enter number n: ')
while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = int(number_n)
	
list = [i for i in range(1, number_n + 1)]
list2 = []
for i in range(0, len(list)):
    if number_n % (i + 1) == 0:
        list2.append(list[i])
print(list2)

