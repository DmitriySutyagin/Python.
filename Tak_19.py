# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
number_n = input('Specify natural power k: ')
while number_n.isalpha():
    number_n = input('Specify natural power k: ')
number_n = int(number_n)


import random
a = []
c = ' '
for i in range(number_n, 0, -1):
    print(i)
    a.append(str(random.randint(0, 100)))
    c = ' '
    if i != 1:
       c = a[i] 

print(a)    
print(c)

# def new_string(*params):
    
#     res: str = ''
#     for item in params:
#         res += item 
#         return res
# print(new_string(str(random.randint(0, 100))), '*x**{item} + ',)
# # b = new_string('*x** + ', number_n)
# # print(a)
# # # print(a[i] + b)
# for i 
