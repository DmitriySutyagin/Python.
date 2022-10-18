# Реализуйте алгоритм перемешивания списка
n = input('Enter list size: ')

while n.isalpha():
    n = input('Enter list size: ')
n = int(n) 
list =[]
import random
for i in range(1, n + 1):
    list.append(random.randint(0, 10))
print(list)
random.shuffle(list)
print(list)

