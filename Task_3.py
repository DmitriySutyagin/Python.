# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = input('Enter coordinat x')
y = input('Enter coordinat y')
while x and y != int:
    x = input('Enter coordinat x')
    y = input('Enter coordinat y')
# if x and y == int 
    if x > 0 and y > 0:
        print('First quarter')
    elif y < 0 and x > 0:
        print('Second quarter')
    elif x < 0 and y < 0:
        print('Third quarter')
    elif x < 0 and y > 0:
        print('Fourth quarter')
    else:
        print('Please enter a valid x and y value')
        