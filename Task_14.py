# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binary(number_n):
    s = ''
    while number_n > 0:
        s = str(number_n % 2) + s
        number_n //= 2
    return s
while 1:
    number_n = int(input('Enter a real number n: '))
    if number_n != 0:
        print(binary(number_n))
    else:
        break
