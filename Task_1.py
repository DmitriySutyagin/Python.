# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = input('Enter a number and the program will check whether it is output or not.\n')
while a > 7 or a < 0:
    a = input('Enter number 1 or 7\n') 
a = int(a)
if a <= 5:
    print('No')
else:
    print('Yes')
