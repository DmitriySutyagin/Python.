# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
number_n = input('How many numbers do you want to enter?')
while number_n.isalpha():
    number_n = input('How many numbers do you want to enter?')
number_n = int(number_n)

lines = [int(input()) for _ in range(int(number_n))] 
print(lines)
list = []
for i in lines:
    if i not in list:
        list.append(i)
print(list)
