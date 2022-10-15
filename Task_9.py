# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number_n = input('Enter number n: ')

while number_n.isalpha():
    number_n = input('Enter number n: ')
number_n = int(number_n)  
list = (range(-number_n, number_n))


import random
a = (random.randint(0, len(list)))
b = (random.randint(0, len(list)))
c = list[a] * list[b]  
str_a = str(a)
str_b = str(b)
print(a, b)
print(c)

list2 = [a, b]
data = open('Task_9.txt', 'w')
data.writelines(str_a)
data.writelines('\n')
data.writelines(str_b)
data.close()

path = 'Task_9.txt'
data = open (path, 'r')
for line in data:
    print(line)
data.close()
