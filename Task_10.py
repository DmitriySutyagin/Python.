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

# list2 = []
# for i in range(1, len(list) + 1):
#     list2.append(random.randint())


# print(list2)