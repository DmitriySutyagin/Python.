# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number_n = input('Eneter number n: ')
while number_n.isalpha():
    number_n = input('Eneter number n: ')
number_n = int(number_n)    
mul = 1
i = 1
while i != number_n + 1:
    mul = mul * i
    print(mul)
    i += 1
